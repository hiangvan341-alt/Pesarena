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
        """Giải phóng phòng để người chơi tạo phòng mới, không thay đổi RP.

        - Luôn giữ bản ghi phòng, trận, tỷ số, báo cáo và bằng chứng tranh chấp.
        - Trận đang chơi/chờ xác nhận/tranh chấp được chuyển sang cancelled để
          không tiếp tục khóa người chơi ở active_match_for_user().
        - Trận confirmed giữ nguyên confirmed và toàn bộ delta/RP đã tính.
        """
        room = get_room(room_id)
        if not room:
            flash("Không tìm thấy phòng.", "danger")
            return redirect_admin("rooms")

        if room.get("status") == "cancelled":
            flash("Phòng này đã được hủy trước đó.", "warning")
            return redirect_admin("rooms")

        linked_match = get_match(room.get("match_id")) if room.get("match_id") else None
        updated_at = now_iso()
        old_match_status = linked_match.get("status") if linked_match else None

        # Không gọi hàm hoàn tác kết quả: Hủy phòng chỉ nhằm giải
        # phóng trạng thái để người chơi tạo phòng mới, tuyệt đối không đổi RP.
        if linked_match and old_match_status in {"playing", "waiting_confirm", "disputed"}:
            previous_note = str(linked_match.get("note") or "").strip()
            cancellation_note = "Admin đã hủy phòng để giải phóng người chơi; RP không thay đổi."
            if previous_note:
                cancellation_note = previous_note + " | " + cancellation_note
            db.table("matches").update({
                "status": "cancelled",
                "note": cancellation_note,
                "updated_at": updated_at,
            }).eq("id", linked_match.get("id")).execute()

        # Với trận confirmed hoặc các trạng thái lịch sử khác, không sửa match:
        # giữ nguyên trạng thái, tỷ số và delta để BXH/lịch sử không thay đổi.
        db.table("match_rooms").update({
            "status": "cancelled",
            "note": "Admin đã hủy phòng để người chơi có thể tạo phòng mới. RP và dữ liệu trận được giữ nguyên.",
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
            details=(
                f"Trạng thái phòng cũ: {room.get('status')}; "
                f"trạng thái trận cũ: {old_match_status or 'không có trận'}; "
                "giữ lịch sử/báo cáo/tranh chấp; không thay đổi RP"
            ),
        )
        flash("Đã hủy phòng. Người chơi có thể tạo phòng mới; RP và lịch sử không thay đổi.", "success")
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

