"""Supabase repository for Lucky Box backend core."""


def configure(context):
    globals().update(context)


def _payload(data):
    if isinstance(data, list):
        return dict(data[0]) if data else {}
    return dict(data) if isinstance(data, dict) else {}


def list_boxes():
    require_db()
    result = execute_query(
        db.table("lucky_boxes")
        .select("*")
        .order("created_at"),
        "luckybox_list_boxes",
        attempts=2,
    )
    return [dict(row) for row in (result.data or [])]


def list_rate_versions(box_id=None, include_archived=False):
    require_db()
    query = (
        db.table("lucky_box_rate_versions")
        .select("*")
        .order("version_number", desc=True)
    )
    if box_id:
        query = query.eq("box_id", str(box_id))
    if not include_archived:
        query = query.neq("status", "archived")
    result = execute_query(query, "luckybox_list_rate_versions", attempts=2)
    return [dict(row) for row in (result.data or [])]


def list_rewards(rate_version_id):
    require_db()
    result = execute_query(
        db.table("lucky_box_rewards")
        .select("*,shop_items(id,code,name,item_type,category,rarity,image_path,is_unique,is_consumable,is_active)")
        .eq("rate_version_id", str(rate_version_id))
        .order("counts_as_item", desc=True)
        .order("sort_order")
        .order("reward_code"),
        "luckybox_list_rewards",
        attempts=2,
    )
    return [dict(row) for row in (result.data or [])]


def preview_rate_version(actor_user_id, rate_version_id, iterations):
    require_db()
    result = execute_query(
        db.rpc(
            "preview_lucky_box_rate_version",
            {
                "p_actor_user_id": str(actor_user_id),
                "p_rate_version_id": str(rate_version_id),
                "p_iterations": int(iterations),
            },
        ),
        "luckybox_preview_rate_version_rpc",
        attempts=2,
    )
    payload = _payload(result.data)
    if not payload:
        raise RuntimeError("Supabase không trả về kết quả mô phỏng Lucky Box.")
    return payload


def open_box(user_id, box_code, request_id):
    require_db()
    result = execute_query(
        db.rpc(
            "open_lucky_box",
            {
                "p_user_id": str(user_id),
                "p_box_code": str(box_code),
                "p_request_id": str(request_id),
            },
        ),
        "luckybox_open_rpc",
        attempts=2,
    )
    payload = _payload(result.data)
    if not payload:
        raise RuntimeError("Supabase không trả về kết quả mở Lucky Box.")
    return payload


def list_user_openings(user_id, limit=30):
    require_db()
    safe_limit = max(1, min(int(limit or 30), 100))
    result = execute_query(
        db.table("lucky_box_openings")
        .select("id,request_id,box_code,rate_version,zcoin_cost,balance_before,balance_after,opened_at,status,metadata")
        .eq("user_id", str(user_id))
        .order("opened_at", desc=True)
        .limit(safe_limit),
        "luckybox_user_history",
        attempts=2,
    )
    return [dict(row) for row in (result.data or [])]


def get_opening(opening_id):
    require_db()
    result = execute_query(
        db.table("lucky_box_openings")
        .select("*")
        .eq("id", str(opening_id))
        .limit(1),
        "luckybox_get_opening",
        attempts=2,
    )
    opening = dict(result.data[0]) if result.data else None
    if not opening:
        return None
    rewards = execute_query(
        db.table("lucky_box_opening_rewards")
        .select("*")
        .eq("opening_id", str(opening_id))
        .order("reward_slot"),
        "luckybox_get_opening_rewards",
        attempts=2,
    )
    opening["rewards"] = [dict(row) for row in (rewards.data or [])]
    return opening
