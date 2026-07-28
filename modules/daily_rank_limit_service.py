"""Giới hạn số trận Rank và RP dương theo ngày Việt Nam.

Số trận trong ngày được tính ngay từ lúc trận Rank được tạo, không chờ xác nhận
kết quả. Vì vậy các trạng thái playing, waiting_confirm, disputed và confirmed
đều chiếm một lượt. Trận bỏ cuộc hợp lệ cũng chiếm một lượt Rank.
"""
from datetime import datetime, timedelta, timezone

EXPORTED_NAMES = [
    "daily_rank_limits_enabled",
    "set_daily_rank_limits_enabled",
    "current_daily_game_limit",
    "ranked_games_today",
    "positive_rp_today",
    "rank_daily_status",
    "user_reached_daily_rank_limit",
    "daily_rank_block_message",
    "assert_can_start_ranked_match",
    "apply_daily_positive_rp_cap",
]

SETTING_KEY = "rank_daily_limits_config"
WEEKDAY_GAME_LIMIT = 10
WEEKEND_GAME_LIMIT = 15
DAILY_POSITIVE_RP_LIMIT = 150
VN_TZ = timezone(timedelta(hours=7))
COUNTED_MATCH_STATUSES = {"playing", "waiting_confirm", "disputed", "confirmed"}


def configure(context):
    globals().update(context)


def _now_vn():
    return datetime.now(VN_TZ)


def current_daily_game_limit(moment=None):
    """Trả về giới hạn trận theo ngày Việt Nam: T2-T6 là 10, T7-CN là 15."""
    current = moment or _now_vn()
    return WEEKEND_GAME_LIMIT if current.weekday() in {5, 6} else WEEKDAY_GAME_LIMIT


def _day_bounds_utc_iso(moment=None):
    current = moment or _now_vn()
    start_vn = current.replace(hour=0, minute=0, second=0, microsecond=0)
    end_vn = start_vn + timedelta(days=1)
    return start_vn.astimezone(timezone.utc).isoformat(), end_vn.astimezone(timezone.utc).isoformat()


def daily_rank_limits_enabled():
    try:
        result = execute_query(
            db.table("system_settings").select("setting_value")
            .eq("setting_key", SETTING_KEY).limit(1),
            "get_rank_daily_limits_config",
            attempts=2,
        )
        row = (result.data or [{}])[0]
        raw = row.get("setting_value")
        if isinstance(raw, dict):
            return bool(raw.get("enabled", True))
        if isinstance(raw, bool):
            return raw
    except Exception as exc:
        print(f"daily_rank_limits_enabled warning: {exc}")
    return True


def set_daily_rank_limits_enabled(enabled, actor_id=None):
    payload = {
        "enabled": bool(enabled),
        "weekday_game_limit": WEEKDAY_GAME_LIMIT,
        "weekend_game_limit": WEEKEND_GAME_LIMIT,
        "daily_positive_rp_limit": DAILY_POSITIVE_RP_LIMIT,
        "updated_by": actor_id,
        "updated_at": now_iso(),
    }
    execute_query(
        db.table("system_settings").upsert({
            "setting_key": SETTING_KEY,
            "setting_value": payload,
            "updated_at": now_iso(),
        }, on_conflict="setting_key"),
        "set_rank_daily_limits_config",
        attempts=2,
    )
    return payload


def _matches_today(user_id):
    if not user_id:
        return []
    start_iso, end_iso = _day_bounds_utc_iso()
    result = execute_query(
        db.table("matches")
        .select("id,player1_id,player2_id,delta1,delta2,status,note,loser_id,created_at")
        .gte("created_at", start_iso)
        .lt("created_at", end_iso)
        .or_(f"player1_id.eq.{user_id},player2_id.eq.{user_id}"),
        "rank_daily_matches_started",
        attempts=2,
    )
    return list(result.data or [])


def _is_counted_rank_match(match):
    status = str((match or {}).get("status") or "").strip().lower()
    if status in COUNTED_MATCH_STATUSES:
        return True
    if status == "cancelled":
        checker = globals().get("is_forfeit_match")
        if callable(checker):
            try:
                return bool(checker(match))
            except Exception:
                pass
        note = str((match or {}).get("note") or "").casefold()
        return "[forfeit:" in note or "bỏ cuộc" in note
    return False


def _ranked_matches_started_today(user_id):
    return [match for match in _matches_today(user_id) if _is_counted_rank_match(match)]


def ranked_games_today(user_id):
    """Đếm mọi trận Rank đã bắt đầu trong ngày, kể cả chưa xác nhận."""
    return len(_ranked_matches_started_today(user_id))


def positive_rp_today(user_id, exclude_match_id=None):
    """Chỉ RP dương đã chốt ở trận confirmed mới được cộng vào trần +150."""
    total = 0
    for match in _matches_today(user_id):
        if str(match.get("status") or "") != "confirmed":
            continue
        if exclude_match_id and str(match.get("id")) == str(exclude_match_id):
            continue
        if str(match.get("player1_id")) == str(user_id):
            delta = int(match.get("delta1") or 0)
        else:
            delta = int(match.get("delta2") or 0)
        if delta > 0:
            total += delta
    return total


def rank_daily_status(user_id):
    enabled = daily_rank_limits_enabled()
    games = ranked_games_today(user_id) if enabled else 0
    positive = positive_rp_today(user_id) if enabled else 0
    return {
        "enabled": enabled,
        "games": games,
        "game_limit": current_daily_game_limit(),
        "games_remaining": max(0, current_daily_game_limit() - games),
        "is_weekend": _now_vn().weekday() in {5, 6},
        "positive_rp": positive,
        "positive_rp_limit": DAILY_POSITIVE_RP_LIMIT,
        "positive_rp_remaining": max(0, DAILY_POSITIVE_RP_LIMIT - positive),
    }



def user_reached_daily_rank_limit(user_id):
    """True khi người chơi đã chạm giới hạn trận Rank của ngày hiện tại."""
    if not user_id or not daily_rank_limits_enabled():
        return False
    return ranked_games_today(user_id) >= current_daily_game_limit()


def daily_rank_block_message(*user_ids):
    """Trả về thông báo chặn thân thiện, hoặc None nếu tất cả còn lượt."""
    if not daily_rank_limits_enabled():
        return None
    game_limit = current_daily_game_limit()
    blocked = []
    for user_id in user_ids:
        if not user_id:
            continue
        games = ranked_games_today(user_id)
        if games >= game_limit:
            user = get_user(user_id) or {}
            blocked.append((user.get("display_name") or "Người chơi", games))
    if not blocked:
        return None
    names = ", ".join(name for name, _ in blocked)
    return (
        f"{names} đã đủ {game_limit} trận Rank hôm nay. "
        "Không thể tạo phòng, nhận lời mời, Sẵn Sàng hoặc bắt đầu trận Rank mới. "
        "Bạn có thể rời phòng hiện tại an toàn, không bị trừ RP. Giới hạn làm mới lúc 00:00."
    )

def assert_can_start_ranked_match(*user_ids):
    message = daily_rank_block_message(*user_ids)
    if message:
        raise ValueError(message)


def apply_daily_positive_rp_cap(user_id, delta, exclude_match_id=None):
    delta = int(delta or 0)
    if delta <= 0 or not daily_rank_limits_enabled():
        return delta, None
    earned = positive_rp_today(user_id, exclude_match_id=exclude_match_id)
    remaining = max(0, DAILY_POSITIVE_RP_LIMIT - earned)
    applied = min(delta, remaining)
    detail = {
        "enabled": True,
        "earned_before": earned,
        "formula_delta": delta,
        "applied_delta": applied,
        "remaining_before": remaining,
        "limit": DAILY_POSITIVE_RP_LIMIT,
        "capped": applied < delta,
    }
    return applied, detail
