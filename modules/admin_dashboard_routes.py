# HOTFIX V1.14.39.1: legacy Zcoin context removed from /admin
"""Route trang tổng quan Admin và tải dữ liệu quản trị an toàn.

Module đăng ký route theo dependency của app.py để giữ nguyên endpoint và tránh import vòng.
"""

def register_routes(context):
    """Đăng ký nhóm route vào Flask app hiện tại."""
    globals().update(context)

    @app.route("/admin/rank-modes", methods=["POST"])
    @login_required
    @admin_required
    def admin_save_rank_modes():
        configs = get_rank_mode_configs()
        int_fields = ("min_rp", "min_matches", "max_rp_gap", "pool_size", "bans_per_player", "ban_seconds", "pick_seconds")
        rp_fields = ("win_2_0", "lose_0_2", "win_2_1", "lose_1_2", "forfeit_win", "forfeit_loss", "draw_1_1", "draw_all", "one_win_one_draw_win", "one_win_one_draw_loss", "win_both", "lose_both", "draw")
        for code, mode in configs.items():
            enabled_key = f"{code}__enabled"
            if enabled_key in request.form:
                mode["enabled"] = request.form.get(enabled_key) == "1"
            for field in int_fields:
                key = f"{code}__{field}"
                if key in request.form:
                    try: mode[field] = max(0, int(request.form.get(key) or 0))
                    except (TypeError, ValueError): pass
            rp = dict(mode.get("rp") or {})
            for field in rp_fields:
                key = f"{code}__rp__{field}"
                if key in request.form:
                    try: rp[field] = int(request.form.get(key) or 0)
                    except (TypeError, ValueError): pass
            mode["rp"] = rp
        save_rank_mode_configs(configs)
        flash("Đã lưu cấu hình 6 chế độ Rank.", "success")
        return redirect(url_for("admin", tab="rank-modes") + "#rank-modes")

    @app.route("/admin/rank-modes/user-unlocks/<user_id>", methods=["POST"])
    @login_required
    @admin_required
    def admin_save_user_rank_mode_unlocks(user_id):
        user = get_user_by_id(user_id)
        if not user:
            flash("Không tìm thấy tài khoản.", "error")
            return redirect(url_for("admin", tab="rank-modes") + "#rank-modes")
        selected = [code for code in MODE_ORDER if request.form.get(f"mode__{code}") == "1"]
        actor = current_user() or {}
        save_user_rank_mode_unlocks(user_id, selected, actor.get("id"))
        display_name = user.get("display_name") or user.get("username") or user_id
        flash(f"Đã cập nhật quyền chế độ Rank cho {display_name}.", "success")
        return redirect(url_for("admin", tab="users") + "#users")

    @app.route("/admin")
    @login_required
    @admin_required
    def admin():
        admin_started_at = time.perf_counter()
        allowed_admin_tabs = {"overview", "users", "passwords", "rooms", "matches", "match-report", "rank-modes", "test-data", "system", "economy", "rp-tools", "logs"}
        active_admin_tab = str(request.args.get("tab") or "overview").strip().lower()
        if active_admin_tab not in allowed_admin_tabs:
            active_admin_tab = "overview"

        needs_rooms = active_admin_tab == "rooms"
        needs_matches = active_admin_tab == "matches"
        needs_users = active_admin_tab in {"overview", "users", "system", "match-report"}
        needs_passwords = active_admin_tab in {"overview", "passwords"}
        needs_rank_modes = active_admin_tab in {"users", "rank-modes", "system", "match-report"}

        # Trang Admin chứa nhiều khối dữ liệu độc lập. Một truy vấn phụ lỗi không được
        # làm sập toàn bộ trang; khối lỗi sẽ tạm trả danh sách rỗng và ghi log Vercel.
        def admin_safe_load(label, loader, default):
            try:
                value = loader()
                return default if value is None else value
            except Exception as exc:
                app.logger.exception("Admin load failed [%s]: %s", label, exc)
                return default

        all_rooms = admin_safe_load("rooms", list_rooms, []) if needs_rooms else []

        # Không thực hiện thao tác ghi/xóa dữ liệu trong request mở tab Admin.
        # Bản cũ quét từng người chơi rồi gọi cleanup_duplicate_waiting_rooms(),
        # tạo N+1 truy vấn Supabase và là nguyên nhân lớn khiến tab phản hồi rất chậm.

        all_matches = admin_safe_load("matches", list_matches, []) if needs_matches else []

        if active_admin_tab == "overview":
            # Tổng quan chỉ cần số lượng/trạng thái. Không enrich toàn bộ phòng,
            # không auto-confirm từng trận và không tải các cột lớn như rp_details.
            all_rooms = admin_safe_load(
                "overview_rooms",
                lambda: execute_query(
                    db.table("match_rooms").select("id,status,note").order("created_at", desc=True).limit(2000),
                    "admin_overview_rooms",
                    attempts=1,
                ).data or [],
                [],
            )
            all_matches = admin_safe_load(
                "overview_matches",
                lambda: execute_query(
                    db.table("matches").select("id,status").order("created_at", desc=True).limit(5000),
                    "admin_overview_matches",
                    attempts=1,
                ).data or [],
                [],
            )

        # Báo cáo số trận theo múi giờ Việt Nam. Dùng dữ liệu matches đã tải để
        # tránh phát sinh thêm nhiều truy vấn và giữ kết quả thống nhất với tab Trận đấu.
        from datetime import datetime, timedelta, timezone

        vn_tz = timezone(timedelta(hours=7))
        now_vn = datetime.now(vn_tz)
        today_vn = now_vn.date()
        report_range = str(request.args.get("match_report_range") or "today").strip().lower()
        allowed_ranges = {"today", "yesterday", "3days", "7days", "30days", "all"}
        if report_range not in allowed_ranges:
            report_range = "today"

        report_range_labels = {
            "today": "Hôm nay",
            "yesterday": "Hôm qua",
            "3days": "3 ngày gần đây",
            "7days": "1 tuần",
            "30days": "1 tháng",
            "all": "Toàn thời gian",
        }

        if report_range == "today":
            report_start_date = report_end_date = today_vn
        elif report_range == "yesterday":
            report_start_date = report_end_date = today_vn - timedelta(days=1)
        elif report_range == "3days":
            report_start_date, report_end_date = today_vn - timedelta(days=2), today_vn
        elif report_range == "7days":
            report_start_date, report_end_date = today_vn - timedelta(days=6), today_vn
        elif report_range == "30days":
            report_start_date, report_end_date = today_vn - timedelta(days=29), today_vn
        else:
            report_start_date = report_end_date = None

        def _match_vn_date(match):
            raw = (match or {}).get("created_at")
            if not raw:
                return None
            try:
                value = str(raw).strip().replace("Z", "+00:00")
                parsed = datetime.fromisoformat(value)
                if parsed.tzinfo is None:
                    parsed = parsed.replace(tzinfo=timezone.utc)
                return parsed.astimezone(vn_tz).date()
            except Exception:
                return None

        report_matches = []
        if active_admin_tab == "match-report":
            # Chỉ lấy các cột báo cáo và lọc ngay tại Supabase. Không gọi list_matches()
            # vì hàm đó tải toàn bộ trận, enrich user và kiểm tra auto-confirm từng dòng.
            report_columns = "id,created_at,status,player1_id,player2_id,score1,score2,delta1,delta2,rp_details,note"
            report_query = db.table("matches").select(report_columns).order("created_at", desc=True)
            if report_start_date:
                start_dt = datetime.combine(report_start_date, datetime.min.time(), tzinfo=vn_tz).astimezone(timezone.utc)
                end_dt = datetime.combine(report_end_date + timedelta(days=1), datetime.min.time(), tzinfo=vn_tz).astimezone(timezone.utc)
                report_query = report_query.gte("created_at", start_dt.isoformat()).lt("created_at", end_dt.isoformat())
            else:
                # Giới hạn an toàn để tránh một request serverless tải dữ liệu vô hạn.
                report_query = report_query.limit(10000)
            report_rows = admin_safe_load(
                "match_report_rows",
                lambda: execute_query(report_query, "admin_match_report_rows", attempts=2).data or [],
                [],
            )
        else:
            report_rows = all_matches

        for match in report_rows:
            match_date = _match_vn_date(match)
            if match_date is None:
                continue
            row = dict(match)
            row["_report_date"] = match_date
            report_matches.append(row)

        report_status_keys = ("playing", "waiting_confirm", "waiting_result_confirm", "disputed", "confirmed", "cancelled")
        report_status_counts = {key: 0 for key in report_status_keys}
        report_unique_players = set()
        report_confirmed_goals = 0
        report_positive_rp = 0
        report_mode_counts = {code: 0 for code in ("rank_random", "random3_pick1", "tactical_bo3", "bo3", "ban_pick_bo3", "home_away")}

        # Khi kết quả được xác nhận, các phiên bản cũ ghi đè note của trận thành
        # "Đã xác nhận.", làm mất dấu Random 3 chọn 1. Ưu tiên đọc team_tier
        # của phòng liên kết để thống kê đúng cả các trận lịch sử đã bị mất note.
        room_mode_by_match_id = {}
        report_room_rows = all_rooms
        if active_admin_tab == "match-report" and report_matches:
            room_query = db.table("match_rooms").select("match_id,team_tier,created_at")
            if report_start_date:
                start_dt = datetime.combine(report_start_date, datetime.min.time(), tzinfo=vn_tz).astimezone(timezone.utc)
                end_dt = datetime.combine(report_end_date + timedelta(days=1), datetime.min.time(), tzinfo=vn_tz).astimezone(timezone.utc)
                room_query = room_query.gte("created_at", start_dt.isoformat()).lt("created_at", end_dt.isoformat())
            else:
                room_query = room_query.limit(10000)
            report_room_rows = admin_safe_load(
                "match_report_rooms",
                lambda: execute_query(room_query, "admin_match_report_rooms", attempts=1).data or [],
                [],
            )
        for room in report_room_rows:
            match_id = str((room or {}).get("match_id") or "").strip()
            if not match_id:
                continue
            team_tier = str((room or {}).get("team_tier") or "").strip().lower()
            room_mode_by_match_id[match_id] = team_tier

        def _report_match_mode(match):
            match = match or {}
            match_id = str(match.get("id") or "").strip()
            if room_mode_by_match_id.get(match_id) == "random3_pick1":
                return "random3_pick1"

            details = match.get("rp_details")
            if isinstance(details, str):
                try:
                    import json as _json
                    details = _json.loads(details)
                except Exception:
                    details = {}
            if isinstance(details, dict):
                stored_mode = normalize_rank_mode_code(details.get("match_mode") or details.get("mode_code"))
                if stored_mode in report_mode_counts:
                    return stored_mode
            room_mode = normalize_rank_mode_code(room_mode_by_match_id.get(match_id))
            if room_mode in report_mode_counts and room_mode != "rank_random":
                return room_mode
            note = str(match.get("note") or "").casefold()
            aliases = {"random3_pick1": ("random 3 chọn 1", "random3_pick1"), "tactical_bo3": ("đấu chiến thuật bo3", "tactical_bo3"), "ban_pick_bo3": ("cấm chọn clb bo3", "ban_pick_bo3"), "home_away": ("lượt đi", "home_away"), "bo3": (" bo3", "bo3")}
            for code, tokens in aliases.items():
                if any(token in note for token in tokens): return code
            return "rank_random"

        for match in report_matches:
            status = str(match.get("status") or "").strip().lower()
            if status in report_status_counts:
                report_status_counts[status] += 1
            report_mode_counts[_report_match_mode(match)] += 1
            for key in ("player1_id", "player2_id"):
                if match.get(key):
                    report_unique_players.add(str(match.get(key)))
            if status == "confirmed":
                report_confirmed_goals += int(match.get("score1") or 0) + int(match.get("score2") or 0)
                report_positive_rp += max(0, int(match.get("delta1") or 0)) + max(0, int(match.get("delta2") or 0))

        daily_map = {}
        for match in report_matches:
            day = match.get("_report_date")
            if day is None:
                continue
            bucket = daily_map.setdefault(day, {
                "date": day,
                "total": 0,
                "confirmed": 0,
                "playing": 0,
                "waiting": 0,
                "disputed": 0,
                "cancelled": 0,
                "rank_random": 0,
                "random3_pick1": 0,
                "tactical_bo3": 0,
                "bo3": 0,
                "ban_pick_bo3": 0,
                "home_away": 0,
                "players": set(),
            })
            bucket["total"] += 1
            bucket[_report_match_mode(match)] += 1
            status = str(match.get("status") or "").strip().lower()
            if status == "confirmed":
                bucket["confirmed"] += 1
            elif status == "playing":
                bucket["playing"] += 1
            elif status in {"waiting_confirm", "waiting_result_confirm"}:
                bucket["waiting"] += 1
            elif status == "disputed":
                bucket["disputed"] += 1
            elif status == "cancelled":
                bucket["cancelled"] += 1
            for key in ("player1_id", "player2_id"):
                if match.get(key):
                    bucket["players"].add(str(match.get(key)))

        match_report_daily = []
        for day in sorted(daily_map.keys(), reverse=True):
            bucket = daily_map[day]
            bucket["player_count"] = len(bucket.pop("players"))
            bucket["date_label"] = day.strftime("%d/%m/%Y")
            match_report_daily.append(bucket)

        series_rows = []
        series_games = []
        if active_admin_tab == "match-report":
            series_query = db.table("match_series").select("*")
            games_query = db.table("match_series_games").select("*")
            if report_start_date:
                start_iso = datetime.combine(report_start_date, datetime.min.time(), tzinfo=vn_tz).astimezone(timezone.utc).isoformat()
                end_iso = datetime.combine(report_end_date + timedelta(days=1), datetime.min.time(), tzinfo=vn_tz).astimezone(timezone.utc).isoformat()
                series_query = series_query.gte("created_at", start_iso).lt("created_at", end_iso)
                games_query = games_query.gte("created_at", start_iso).lt("created_at", end_iso)
            else:
                series_query = series_query.limit(5000)
                games_query = games_query.limit(15000)
            series_rows = admin_safe_load("rank_series", lambda: execute_query(series_query, "admin_rank_series", attempts=1).data or [], [])
            series_games = admin_safe_load("rank_series_games", lambda: execute_query(games_query, "admin_rank_series_games", attempts=1).data or [], [])
        games_by_series = {}
        for game in series_games:
            games_by_series.setdefault(str(game.get("series_id") or ""), []).append(game)
        series_stats = {code: {"series": 0, "completed": 0, "score_2_0": 0, "score_2_1": 0, "draw": 0, "forfeit": 0, "disputed": 0, "rp_added": 0, "rp_removed": 0, "games": 0, "comebacks": 0} for code in report_mode_counts}
        for row in series_rows:
            code = normalize_rank_mode_code(row.get("mode_code"))
            stat = series_stats.setdefault(code, {})
            stat["series"] = stat.get("series", 0) + 1
            status = str(row.get("status") or "").lower()
            if status == "completed": stat["completed"] += 1
            if status == "disputed": stat["disputed"] += 1
            score = str(row.get("result_code") or row.get("series_score") or row.get("score") or "")
            if score in {"2-0", "0-2"}: stat["score_2_0"] += 1
            elif score in {"2-1", "1-2"}: stat["score_2_1"] += 1
            if str(row.get("result_code") or "").lower() == "draw": stat["draw"] += 1
            if row.get("forfeit_user_id") or str(row.get("result_code") or "").lower() == "forfeit": stat["forfeit"] += 1
            deltas = [int(row.get("rp_player1") or 0), int(row.get("rp_player2") or 0)]
            stat["rp_added"] += sum(max(0, x) for x in deltas)
            stat["rp_removed"] += abs(sum(min(0, x) for x in deltas))
            sgames = games_by_series.get(str(row.get("id") or ""), [])
            stat["games"] += len(sgames)
            winners = [g.get("winner_side") for g in sorted(sgames, key=lambda x: int(x.get("game_no") or 0))]
            if len(winners) >= 3 and winners[0] in {"player1", "player2"} and winners[-2:] == (["player2", "player2"] if winners[0] == "player1" else ["player1", "player1"]): stat["comebacks"] += 1
        for code, stat in series_stats.items():
            stat["completion_rate"] = round(stat["completed"] * 100 / stat["series"], 1) if stat["series"] else 0
            stat["avg_rp"] = round(stat["rp_added"] / stat["completed"], 1) if stat["completed"] else 0

        report_mode_configs = admin_safe_load("rank_mode_configs_report", get_rank_mode_configs, {}) if active_admin_tab == "match-report" else {}
        mode_rows = []
        for code in MODE_ORDER:
            mode_cfg = dict(report_mode_configs.get(code) or get_rank_mode(code))
            mode_rows.append({
                **mode_cfg,
                "match_count": report_mode_counts.get(code, 0),
                "percent": round(report_mode_counts.get(code, 0) * 100 / len(report_matches), 1) if report_matches else 0,
                **series_stats.get(code, {}),
            })
        popular_code = max(report_mode_counts, key=report_mode_counts.get) if report_matches else None
        match_report = {
            "range": report_range,
            "range_label": report_range_labels[report_range],
            "range_labels": report_range_labels,
            "total": len(report_matches),
            "confirmed": report_status_counts.get("confirmed", 0),
            "playing": report_status_counts.get("playing", 0),
            "waiting": report_status_counts.get("waiting_confirm", 0) + report_status_counts.get("waiting_result_confirm", 0),
            "disputed": report_status_counts.get("disputed", 0),
            "cancelled": report_status_counts.get("cancelled", 0),
            "unique_players": len(report_unique_players),
            "confirmed_goals": report_confirmed_goals,
            "positive_rp": report_positive_rp,
            "mode_counts": report_mode_counts,
            "mode_rows": mode_rows,
            "popular_mode": (report_mode_configs.get(popular_code) or {}).get("label", popular_code) if popular_code else "Chưa có dữ liệu",
        }

        raw_users = admin_safe_load("users", list_all_users, []) if needs_users else []
        if active_admin_tab == "match-report":
            # Tính số người mở khóa hoàn toàn trong RAM. Bản cũ gọi
            # check_rank_mode_eligibility cho từng user x từng mode, kéo theo hàng
            # trăm/hàng nghìn truy vấn get_rank_mode + get_user_unlocks.
            unlock_map = admin_safe_load("rank_mode_unlock_map", list_rank_mode_user_unlocks, {})
            for mode_row in match_report.get("mode_rows", []):
                code = mode_row.get("code")
                min_rp = int(mode_row.get("min_rp") or 0)
                min_matches = int(mode_row.get("min_matches") or 0)
                enabled = bool(mode_row.get("enabled", True))
                unlocked = 0
                for user in raw_users:
                    if str(user.get("role") or "player") != "player":
                        continue
                    uid = str(user.get("id") or "")
                    manual = code in set(unlock_map.get(uid) or ())
                    rp = int(user.get("rank_points") or 0)
                    played = int(user.get("wins") or 0) + int(user.get("draws") or 0) + int(user.get("losses") or 0)
                    if enabled and (manual or (rp >= min_rp and played >= min_matches)):
                        unlocked += 1
                mode_row["unlocked_players"] = unlocked
        admin_users = admin_safe_load(
            "decorate_users", lambda: decorate_admin_users(raw_users), []
        )

        # Ưu tiên nhóm IP trùng lên đầu và đặt các tài khoản cùng IP cạnh nhau.
        admin_users.sort(key=lambda item: (
            0 if item.get("duplicate_ips") else 1,
            (item.get("duplicate_ips") or [item.get("latest_ip") or "~"])[0],
            (item.get("username") or "").lower(),
        ))
        players = [u for u in admin_users if u.get("role") == "player"]
        admins = [u for u in admin_users if is_admin_user(u)]
        pending_users = [u for u in players if u.get("account_status") == "pending"]

        password_reset_requests = admin_safe_load(
            "password_resets", lambda: list_password_reset_requests("pending"), []
        ) if needs_passwords else []
        raw_disputes = admin_safe_load(
            "match_disputes", lambda: list_match_disputes("pending"), []
        ) if active_admin_tab in {"overview", "matches"} else []
        pending_disputes = []
        for item in raw_disputes:
            try:
                pending_disputes.append(decorate_match_dispute(item, all_matches))
            except Exception as exc:
                app.logger.exception("Admin dispute decoration failed: %s", exc)

        audit_logs = (
            admin_safe_load("audit_logs", list_admin_activity_logs, [])
            if active_admin_tab == "logs" and is_owner_user(current_user()) else []
        )
        duplicate_ip_groups = admin_safe_load(
            "duplicate_ips", lambda: build_duplicate_ip_groups(admin_users), []
        ) if active_admin_tab in {"overview", "users"} else []
        duplicate_ip_user_count = len({
            str(account.get("id"))
            for group in duplicate_ip_groups
            for account in group.get("accounts", [])
            if account.get("id")
        })
        ip_device_status = dict(getattr(list_user_devices, "last_status", {}) or {})
        ip_device_status.setdefault("ok", None)
        ip_device_status.setdefault("row_count", 0)
        ip_device_status["account_ip_count"] = sum(1 for user in admin_users if user.get("known_ips"))
        ip_device_status["duplicate_group_count"] = len(duplicate_ip_groups)

        rendered_admin = render_template(
            "admin.html",
            admin_users=admin_users,
            players=players,
            admins=admins,
            pending_users=pending_users,
            all_matches=all_matches[:80],
            disputed=[m for m in all_matches if m.get("status") == "disputed"],
            playing=[m for m in all_matches if m.get("status") == "playing"],
            rooms=[r for r in all_rooms if r.get("status") in ["waiting_ready", "playing", "friendly_playing", "waiting_result_confirm", "waiting_confirm", "disputed"]],
            recent_closed_rooms=[
                r for r in all_rooms
                if r.get("status") == "cancelled"
                and (
                    "đóng trình duyệt" in str(r.get("note") or "").casefold()
                    or "host_browser_offline" in str(r.get("note") or "").casefold()
                    or "chủ phòng" in str(r.get("note") or "").casefold()
                )
            ][:30],
            all_rooms=all_rooms[:80],
            invites=admin_safe_load("invites", lambda: list_invites("pending"), []) if active_admin_tab in {"overview", "rooms"} else [],
            active_announcement=admin_safe_load("announcement", get_active_announcement, None) if active_admin_tab in {"overview", "system"} else None,
            password_reset_requests=password_reset_requests,
            audit_logs=audit_logs,
            duplicate_ip_groups=duplicate_ip_groups,
            duplicate_ip_user_count=duplicate_ip_user_count,
            ip_device_status=ip_device_status,
            pending_disputes=pending_disputes,
            can_create_test_account=has_admin_permission(current_user(), "users_edit"),
            can_import_accounts_csv=has_admin_permission(current_user(), "accounts_import"),
            admin_permission_groups=ADMIN_PERMISSION_GROUPS,
            admin_permission_labels=ADMIN_PERMISSION_LABELS,
            current_admin_permissions=_admin_permissions(current_user()),
            system_features=admin_safe_load("system_features", get_system_features, dict(SYSTEM_FEATURE_DEFAULTS)) if active_admin_tab == "system" else dict(SYSTEM_FEATURE_DEFAULTS),
            maintenance_config=admin_safe_load("maintenance_config", get_maintenance_config, _maintenance_default_config()) if active_admin_tab == "system" else _maintenance_default_config(),
            maintenance_status=admin_safe_load("maintenance_status", get_maintenance_status, {"closed": False, "countdown": None}) if active_admin_tab == "system" else {"closed": False, "countdown": None},
            match_report=match_report,
            match_report_daily=match_report_daily,
            rank_mode_configs=admin_safe_load("rank_mode_configs", get_rank_mode_configs, {}) if needs_rank_modes else {},
            rank_mode_order=MODE_ORDER,
            rank_mode_user_unlocks=admin_safe_load("rank_mode_user_unlocks", list_rank_mode_user_unlocks, {}) if active_admin_tab == "users" else {},
            active_admin_tab=active_admin_tab,
        )
        app.logger.info(
            "ADMIN_PERF tab=%s range=%s duration_ms=%d rooms=%d matches=%d users=%d report_matches=%d",
            active_admin_tab,
            report_range,
            int((time.perf_counter() - admin_started_at) * 1000),
            len(all_rooms),
            len(all_matches),
            len(raw_users),
            len(report_matches),
        )
        return rendered_admin

