"""Lucky Box backend routes and Admin Draft preview."""

from . import repository
from . import service


def register_routes(context):
    globals().update(context)
    service.configure(context)

    @app.route("/admin/lucky-box/preview", methods=["GET", "POST"], endpoint="admin_luckybox_preview")
    @login_required
    @admin_required
    def admin_luckybox_preview_route():
        actor = current_user()
        selected_rate_id = str(
            request.values.get("rate_version_id") or ""
        ).strip()
        result = None
        error = None
        if request.method == "POST":
            try:
                result = service.run_preview(
                    actor,
                    selected_rate_id,
                    request.form.get("iterations") or 1000,
                )
            except ValueError as exc:
                error = str(exc)
            except Exception as exc:
                app.logger.exception(
                    "Lucky Box preview failed actor=%s rate=%s: %s",
                    actor.get("id"), selected_rate_id, exc,
                )
                error = service.error_message(exc)
        return render_template(
            "admin_luckybox/preview.html",
            **service.build_admin_preview_context(
                actor, selected_rate_id, result=result, error=error
            ),
        )

    @app.route("/api/lucky-box/open", methods=["POST"], endpoint="luckybox_open")
    @login_required
    def luckybox_open_route():
        user = current_user()
        payload = request.get_json(silent=True) or request.form
        try:
            result = service.open_for_user(
                user,
                payload.get("request_id") or payload.get("request_key"),
                payload.get("box_code") or service.BOX_CODE,
            )
        except ValueError as exc:
            return jsonify({"ok": False, "message": str(exc)}), 400
        except Exception as exc:
            app.logger.exception("Lucky Box open failed user=%s: %s", user.get("id"), exc)
            return jsonify({"ok": False, "message": service.error_message(exc)}), 409

        new_balance = int(result.get("balance_after") or 0)
        session["zcoin_balance"] = new_balance
        ttl_cache_delete(f"user:{user.get('id')}")
        cache_delete("_rz_current_user")
        cache_delete("_rz_players_all")
        cache_delete("_rz_users_map")
        return jsonify({"ok": True, **result})

    @app.route("/lucky-box/history", endpoint="luckybox_history")
    @login_required
    def luckybox_history_route():
        user = current_user()
        openings = repository.list_user_openings(user.get("id"), request.args.get("limit") or 30)
        return render_template("luckybox/history.html", openings=openings)

    @app.route("/lucky-box/openings/<opening_id>", endpoint="luckybox_opening_detail")
    @login_required
    def luckybox_opening_detail_route(opening_id):
        user = current_user()
        opening = repository.get_opening(opening_id)
        if not opening:
            return "Không tìm thấy lượt mở Lucky Box.", 404
        if str(opening.get("user_id")) != str(user.get("id")) and not is_admin_user(user):
            return "Bạn không có quyền xem lượt mở này.", 403
        return render_template("luckybox/opening_detail.html", opening=opening)
