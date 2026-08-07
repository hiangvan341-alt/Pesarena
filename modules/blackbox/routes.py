"""Routes for PES Arena Black Box client ingest + admin detail."""
from __future__ import annotations


def register_routes(context):
    globals().update(context)
    from .safety import run_server_safety_audit

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
    @login_required
    @admin_required
    def api_admin_blackbox_safety():
        report = run_server_safety_audit(context, blackbox_config(), blackbox_store_batch)
        return jsonify({"ok": True, "report": report})

    @app.route("/admin/blackbox/incident/<incident_id>")
    @login_required
    @admin_required
    def admin_blackbox_incident(incident_id):
        incident = blackbox_get_incident(incident_id)
        if not incident:
            flash("Không tìm thấy Incident hoặc chưa chạy migration Black Box.", "warning")
            return redirect(url_for("admin", tab="blackbox") + "#blackbox")
        return render_template("admin/blackbox_incident.html", incident=incident)
