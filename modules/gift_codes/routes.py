"""Route đổi Gift Code và quản lý mã trong Admin."""


def register_routes(context):
    globals().update(context)

    @app.route("/zcoin/gift-code/redeem", methods=["POST"])
    @login_required
    def redeem_gift_code_route():
        user = current_user()
        code = request.form.get("code")
        request_key = request.form.get("request_token")
        try:
            result = redeem_gift_code(user.get("id"), code, request_key)
        except ValueError as exc:
            flash(str(exc), "danger")
            return redirect(url_for("zcoin_rewards") + "#gift-code")
        except Exception as exc:
            message = str(exc).lower()
            app.logger.exception("Đổi Gift Code thất bại user=%s code=%s: %s", user.get("id"), code, exc)
            errors = {
                "gift_code_not_found": "Gift Code không tồn tại.",
                "gift_code_inactive": "Gift Code đã bị tắt.",
                "gift_code_not_started": "Gift Code chưa đến thời gian sử dụng.",
                "gift_code_expired": "Gift Code đã hết hạn.",
                "gift_code_depleted": "Gift Code đã hết lượt sử dụng.",
                "gift_code_user_limit": "Bạn đã sử dụng hết số lượt cho Gift Code này.",
            }
            matched = next((text for key, text in errors.items() if key in message), None)
            if matched:
                flash(matched, "danger")
            elif "redeem_zcoin_gift_code" in message or "pgrst202" in message or "schema cache" in message:
                flash("Hệ thống Gift Code chưa được cài đặt đầy đủ. Hãy chạy SQL của V1.14.38.", "danger")
            else:
                flash("Không thể đổi Gift Code lúc này. Hãy kiểm tra dòng lỗi cuối trong Vercel Logs.", "danger")
            return redirect(url_for("zcoin_rewards") + "#gift-code")

        ttl_cache_delete(f"user:{user.get('id')}")
        cache_delete("_rz_current_user")
        session["zcoin_balance"] = int(result.get("balance_after") or 0)
        if result.get("duplicate"):
            flash("Yêu cầu này đã được xử lý trước đó.", "warning")
        else:
            reward = int(result.get("reward_amount") or 0)
            session["zcoin_reward_effect"] = {
                "type": "gift_code",
                "title": "Đổi Gift Code thành công!",
                "amount": reward,
                "code": result.get("code"),
                "balance_after": int(result.get("balance_after") or 0),
            }
            flash(f"Bạn nhận được {format_zcoin(reward)} Zcoin từ Gift Code.", "success")
        return redirect(url_for("zcoin_rewards") + "#gift-code")

    @app.route("/admin/gift-codes/create", methods=["POST"])
    @login_required
    @admin_required
    @admin_permission_required("zcoin_manage")
    def admin_create_gift_code():
        actor = current_user()
        try:
            item = create_gift_code(actor, request.form)
        except ValueError as exc:
            flash(str(exc), "danger")
            return redirect_admin("zcoin")
        except Exception as exc:
            app.logger.exception("Tạo Gift Code thất bại: %s", exc)
            message = str(exc).lower()
            if "duplicate" in message or "unique" in message:
                flash("Gift Code này đã tồn tại. Hãy chọn mã khác.", "danger")
            else:
                flash("Không thể tạo Gift Code. Hãy kiểm tra dòng lỗi cuối trong Vercel Logs.", "danger")
            return redirect_admin("zcoin")

        log_admin_action(
            "Tạo Gift Code",
            "gift_code",
            item.get("id"),
            item.get("code"),
            f"{item.get('reward_amount', 0)} Zcoin × {item.get('max_redemptions', 0)} lượt",
        )
        flash(f"Đã tạo Gift Code {item.get('code')}.", "success")
        return redirect_admin("zcoin")

    @app.route("/admin/gift-codes/<code_id>/toggle", methods=["POST"])
    @login_required
    @admin_required
    @admin_permission_required("zcoin_manage")
    def admin_toggle_gift_code(code_id):
        enabled = str(request.form.get("enabled") or "0").strip() == "1"
        try:
            toggle_gift_code(code_id, enabled)
        except Exception as exc:
            app.logger.exception("Bật/tắt Gift Code thất bại id=%s: %s", code_id, exc)
            flash("Không thể thay đổi trạng thái Gift Code.", "danger")
            return redirect_admin("zcoin")
        log_admin_action(
            "Bật Gift Code" if enabled else "Tắt Gift Code",
            "gift_code",
            code_id,
            code_id,
            "enabled" if enabled else "disabled",
        )
        flash("Đã cập nhật trạng thái Gift Code.", "success")
        return redirect_admin("zcoin")
