"""Truy cập dữ liệu dành riêng cho Hồ sơ cá nhân."""


def configure(context):
    globals().update(context)


def update_avatar_record(user_id, avatar_url, avatar_path):
    return execute_query(
        db.table("users").update({
            "avatar_url": avatar_url,
            "avatar_path": avatar_path,
            "avatar_updated_at": now_iso(),
        }).eq("id", user_id),
        "profile_update_avatar",
    )


def clear_avatar_record(user_id):
    return execute_query(
        db.table("users").update({
            "avatar_url": None,
            "avatar_path": None,
            "avatar_updated_at": now_iso(),
        }).eq("id", user_id),
        "profile_delete_avatar",
    )


def find_display_name_duplicates(display_name):
    try:
        result = execute_query(
            db.table("users").select("id,display_name").ilike("display_name", display_name).limit(5),
            "profile_check_display_name_duplicate",
        )
        return result.data or []
    except Exception:
        return []


def update_display_name_record(user_id, display_name, change_count):
    return execute_query(
        db.table("users").update({
            "display_name": display_name,
            "display_name_change_count": change_count,
            "display_name_changed_at": now_iso(),
        }).eq("id", user_id),
        "profile_update_display_name",
    )
