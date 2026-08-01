"""Route Admin xóa trận, hủy/xóa phòng và xóa lời mời.

Module đăng ký route theo dependency của app.py để giữ nguyên endpoint và tránh import vòng.
"""

def register_routes(context):
    """Đăng ký nhóm route vào Flask app hiện tại."""
    globals().update(context)

    @app.route("/admin/match/<match_id>/delete", methods=["POST"])
    @login_required
    @admin_required
    @admin_permission_required("matches_delete")
    def admin_delete_match(match_id):
        """Giữ endpoint cũ nhưng khóa xóa trực tiếp để tránh làm lệch lịch sử."""
        flash(
            "Collap_V1.13.3a đã tắt xóa trực tiếp trận đấu. Admin chỉ được chuyển trạng thái sang Đã hủy.",
            "warning",
        )
        return redirect_admin("matches")


    @app.route("/admin/room/<room_id>/cancel", methods=["POST"])
    @login_required
    @admin_required
    @admin_permission_required("rooms_manage")
    def admin_cancel_room(room_id):
        """Hủy phòng nhưng giữ nguyên bản ghi phòng/trận để phục vụ lịch sử và kiểm toán."""
        room = get_room(room_id)
        if not room:
            flash("Không tìm thấy phòng.", "danger")
            return redirect_admin("rooms")

        if room.get("status") == "cancelled":
            flash("Phòng này đã được hủy trước đó.", "warning")
            return redirect_admin("rooms")

        linked_match = get_match(room.get("match_id")) if room.get("match_id") else None
        reversed_rp = False

        # Phải hoàn tác RP thành công trước khi đổi trạng thái phòng. Tránh tình trạng
        # phòng đã bị hủy nhưng RP vẫn còn nguyên nếu thao tác hoàn tác gặp lỗi.
        if linked_match and linked_match.get("status") == "confirmed":
            if not reverse_confirmed_match_result(linked_match):
                flash("Không thể hoàn tác RP của trận đã xác nhận; phòng và trận được giữ nguyên.", "danger")
                return redirect_admin("rooms")
            reversed_rp = True

        updated_at = now_iso()
        if linked_match:
            db.table("matches").update({
                "status": "cancelled",
                "delta1": 0,
                "delta2": 0,
                "note": "Admin đã hủy phòng/trận; lịch sử được giữ nguyên."
                        + (" RP đã được hoàn tác." if reversed_rp else " Trận chưa cộng RP."),
                "updated_at": updated_at,
            }).eq("id", linked_match.get("id")).execute()

        db.table("match_rooms").update({
            "status": "cancelled",
            "note": "Admin đã hủy phòng; dữ liệu phòng và trận được giữ lại.",
            "state_expires_at": None,
            "updated_at": updated_at,
        }).eq("id", room_id).execute()

        if room.get("invite_id"):
            db.table("match_invites").update({
                "status": "cancelled",
                "updated_at": updated_at,
            }).eq("id", room.get("invite_id")).execute()

        cache_delete("_rz_rooms_all")
        cache_delete("_rz_matches_all")
        cache_delete("_rz_invites_all")
        cache_delete("_rz_current_pending_invites")
        ttl_cache_delete("rooms_raw")
        ttl_cache_delete("matches_raw")
        ttl_cache_delete("invites_raw")

        log_admin_action(
            "Hủy phòng",
            "room",
            room_id,
            details=f"Trạng thái cũ: {room.get('status')}; giữ lịch sử; hoàn tác RP: {'có' if reversed_rp else 'không cần'}",
        )
        flash("Đã hủy phòng và giữ nguyên lịch sử." + (" RP của trận đã được hoàn tác." if reversed_rp else ""), "success")
        return redirect_admin("rooms")


    @app.route("/admin/room/<room_id>/delete", methods=["POST"])
    @login_required
    @admin_required
    @admin_permission_required("rooms_manage")
    def admin_delete_room(room_id):
        """Chỉ xóa vật lý phòng chờ chưa có trận; phòng có trận phải dùng Hủy."""
        room = get_room(room_id)
        if not room:
            flash("Không tìm thấy phòng.", "danger")
            return redirect_admin("rooms")

        if room.get("match_id"):
            flash("Không thể xóa phòng đã có trận. Hãy dùng Hủy để giữ lịch sử và hoàn tác RP an toàn.", "warning")
            return redirect_admin("rooms")

        # Phòng chờ chưa phát sinh trận/RP mới được phép dọn vật lý.
        db.table("chat_messages").delete().eq("room_id", room_id).execute()
        if room.get("invite_id"):
            db.table("match_invites").update({
                "status": "cancelled",
                "updated_at": now_iso(),
            }).eq("id", room.get("invite_id")).execute()
        db.table("match_rooms").delete().eq("id", room_id).execute()

        cache_delete("_rz_rooms_all")
        cache_delete("_rz_invites_all")
        cache_delete("_rz_current_pending_invites")
        ttl_cache_delete("rooms_raw")
        ttl_cache_delete("invites_raw")

        log_admin_action("Xóa phòng chờ", "room", room_id, details=f"{room.get('host_name')} vs {room.get('guest_name')}; chưa có trận")
        flash("Đã xóa phòng chờ. Không có trận hoặc RP nào bị ảnh hưởng.", "success")
        return redirect_admin("rooms")


    @app.route("/admin/invite/<invite_id>/delete", methods=["POST"])
    @login_required
    @admin_required
    @admin_permission_required("invites_manage")
    def admin_delete_invite(invite_id):
        invite = get_invite(invite_id)
        if not invite:
            flash("Không tìm thấy lời mời.", "danger")
            return redirect_admin("rooms")

        db.table("match_invites").delete().eq("id", invite_id).execute()
        log_admin_action("Xóa lời mời", "invite", invite_id, details=f"{invite.get('from_name', '-')} → {invite.get('to_name', '-')}")
        flash("Đã xóa lời mời.", "success")
        return redirect_admin("rooms")

