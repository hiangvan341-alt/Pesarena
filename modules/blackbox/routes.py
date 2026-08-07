"""Routes for PES Arena Black Box client ingest + admin detail."""
from __future__ import annotations


def register_routes(context):
    globals().update(context)
    try:
        from .safety import run_server_safety_audit
    except Exception as exc:
        # Safety Lab is optional. A diagnostics import error must never crash app startup.
        def run_server_safety_audit(_context, _cfg, _store_batch):
            return {
                "overall": "WARNING",
                "counts": {"PASS": 0, "WARNING": 1, "FAIL": 0, "NOT_TESTED": 1},
                "checks": [{
                    "name": "Safety Lab import",
                    "status": "NOT_TESTED",
                    "detail": f"Safety Lab disabled: {type(exc).__name__}",
                }],
            }

    @app.route("/api/blackbox/config", methods=["GET"])
    @login_required
    def api_blackbox_config():
        cfg = blackbox_config()
        return jsonify({"ok": True, **cfg})

    @app.route("/api/blackbox/events", methods=["POST"])
    @login_required
    def api_blackbox_events():
        # Always return quickly/fail-open. Storage errors never break the user flow.
        payload = request.get_json(silent=True) or {}
        events = payload.get("events") if isinstance(payload.get("events"), list) else []
        if len(events) > 80:
            events = events[:80]
        result = blackbox_store_batch(
            user_id=session.get("user_id"),
            session_id=payload.get("session_id"),
            page=payload.get("page") or request.referrer or "",
            events=events,
            client=payload.get("client") or {},
            request_id=request.headers.get("X-Request-ID"),
        )
        # Intentionally 202 even when persistence is unavailable.
        return jsonify({"ok": True, "accepted": len(events), "stored": result.get("stored", 0)}), 202


    @app.route("/api/admin/blackbox/safety", methods=["GET"])
    def api_admin_blackbox_safety():
        # API-specific auth keeps every outcome JSON. Generic page decorators may
        # redirect to HTML, which makes diagnostics ambiguous for fetch clients.
        user_id = session.get("user_id")
        if not user_id:
            return jsonify({"ok": False, "error": "authentication_required"}), 401
        try:
            user = current_user()
        except Exception as exc:
            try:
                app.logger.exception("Black Box Safety auth lookup failed: %s", exc)
            except Exception:
                pass
            return jsonify({"ok": False, "error": "authentication_lookup_failed"}), 500
        if not user or not is_admin_user(user):
            return jsonify({"ok": False, "error": "admin_required"}), 403

        # Diagnostics must report their own failure as JSON instead of letting Flask
        # return the generic HTML 500 page (which the Safety Lab cannot parse).
        try:
            report = run_server_safety_audit(context, blackbox_config(), blackbox_store_batch)
            response = jsonify({"ok": True, "report": report})
            response.headers["Cache-Control"] = "no-store"
            return response
        except Exception as exc:
            try:
                app.logger.exception("Black Box Safety API failed: %s", exc)
            except Exception:
                pass
            report = {
                "overall": "FAIL",
                "counts": {"PASS": 0, "WARNING": 0, "FAIL": 1, "NOT_TESTED": 0},
                "checks": [{
                    "name": "Safety API runtime",
                    "status": "FAIL",
                    "detail": f"{type(exc).__name__}: {str(exc)[:300]}",
                }],
            }
            response = jsonify({"ok": False, "error": "safety_audit_failed", "report": report})
            response.headers["Cache-Control"] = "no-store"
            return response, 500

    @app.route("/admin/blackbox/incident/<incident_id>")
    @login_required
    @admin_required
    def admin_blackbox_incident(incident_id):
        incident = blackbox_get_incident(incident_id)
        if not incident:
            flash("Không tìm thấy Incident hoặc chưa chạy migration Black Box.", "warning")
            return redirect(url_for("admin", tab="blackbox") + "#blackbox")
        return render_template("admin/blackbox_incident.html", incident=incident)
