"""Route Hồ sơ cá nhân, giữ nguyên endpoint để tương thích toàn app."""

from . import repository
from . import service


def register_routes(context):
    globals().update(context)
    repository.configure(context)
    service.configure(context)

    @app.route("/profile")
    @login_required
    def my_profile():
        return redirect(url_for("profile", user_id=current_user().get("id")))

    @app.route("/profile/avatar", methods=["POST"])
    @login_required
    def update_profile_avatar():
        user = current_user()
        avatar_file = request.files.get("avatar")
        new_path = None
        try:
            avatar_bytes = service.prepare_avatar_bytes(avatar_file)
            new_path, new_url = service.upload_avatar_to_storage(user.get("id"), avatar_bytes)
            old_path = user.get("avatar_path")
            repository.update_avatar_record(user.get("id"), new_url, new_path)
            session["avatar_url"] = new_url
            if old_path and old_path != new_path:
                service.remove_avatar_object(old_path)
            flash("Ảnh đại diện đã được cập nhật và sẽ hiển thị trên toàn app.", "success")
        except ValueError as exc:
            flash(str(exc), "danger")
        except Exception as exc:
            if new_path:
                service.remove_avatar_object(new_path)
            app.logger.exception("update_profile_avatar error: %s", exc)
            flash("Không thể cập nhật ảnh đại diện lúc này. Hãy kiểm tra đã chạy SQL V1.6.1 rồi thử lại.", "danger")
        return redirect(url_for("profile", user_id=user.get("id")))

    @app.route("/profile/avatar/delete", methods=["POST"])
    @login_required
    def delete_profile_avatar():
        user = current_user()
        old_path = user.get("avatar_path")
        try:
            repository.clear_avatar_record(user.get("id"))
            session["avatar_url"] = None
            service.remove_avatar_object(old_path)
            flash("Đã xóa ảnh đại diện. App sẽ dùng chữ cái mặc định.", "success")
        except Exception as exc:
            app.logger.exception("delete_profile_avatar error: %s", exc)
            flash("Không thể xóa ảnh đại diện lúc này.", "danger")
        return redirect(url_for("profile", user_id=user.get("id")))

    @app.route("/profile/display-name", methods=["POST"])
    @login_required
    def update_display_name():
        user = current_user()
        if not user:
            return redirect(url_for("login"))

        new_name = " ".join(request.form.get("display_name", "").strip().split())
        current_name = str(user.get("display_name") or "").strip()
        change_count = int(user.get("display_name_change_count", 0) or 0)

        if change_count >= 2:
            flash("Bạn đã sử dụng hết 2 lần đổi tên hiển thị.", "danger")
            return redirect(url_for("profile", user_id=user.get("id")))
        if len(new_name) < 2 or len(new_name) > 40:
            flash("Tên hiển thị phải có từ 2 đến 40 ký tự.", "danger")
            return redirect(url_for("profile", user_id=user.get("id")))
        if new_name.casefold() == current_name.casefold():
            flash("Tên hiển thị mới không khác tên hiện tại.", "warning")
            return redirect(url_for("profile", user_id=user.get("id")))

        duplicate = repository.find_display_name_duplicates(new_name)
        if any(row.get("id") != user.get("id") and str(row.get("display_name") or "").casefold() == new_name.casefold() for row in duplicate):
            flash("Tên hiển thị này đã được người khác sử dụng.", "danger")
            return redirect(url_for("profile", user_id=user.get("id")))

        try:
            repository.update_display_name_record(user.get("id"), new_name, change_count + 1)
            session["display_name"] = new_name
            remaining = max(0, 2 - (change_count + 1))
            flash(f"Đã đổi tên hiển thị. Bạn còn {remaining} lần đổi tên.", "success")
        except Exception as exc:
            app.logger.exception("update_display_name error: %s", exc)
            flash("Không thể đổi tên lúc này. Hãy kiểm tra đã chạy file SQL cập nhật V1.8.47.", "danger")
        return redirect(url_for("profile", user_id=user.get("id")))

    @app.route("/profile/<user_id>")
    @login_required
    def profile(user_id):
        viewer = current_user()
        context_data = service.build_profile_context(user_id, viewer)
        if context_data is None:
            flash("Không tìm thấy player.", "danger")
            return redirect(url_for("players"))
        return render_template("profile.html", **context_data)
