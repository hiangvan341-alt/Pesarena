"""Đọc trạng thái trang bị hồ sơ từ Shop/Kho đồ Giai đoạn 3.

Nếu migration Shop chưa được chạy, dịch vụ tự quay về dữ liệu
``users.equipped_cosmetics`` cũ để trang Hồ sơ vẫn hoạt động bình thường.
"""

PROFILE_EQUIPMENT_SLOTS = (
    "avatar_frame",
    "profile_banner",
    "profile_badge",
    "name_style",
    "profile_card_theme",
)


def configure(context):
    globals().update(context)


def _safe_dict(value):
    return dict(value) if isinstance(value, dict) else {}




def _cache_keys(user_id):
    normalized = str(user_id or "").replace("-", "_")
    return f"_rz_profile_equipment_{normalized}", f"profile_equipment:{user_id}"


def invalidate_equipment_cache(user_id):
    request_key, ttl_key = _cache_keys(user_id)
    try:
        cache_delete(request_key)
    except Exception:
        pass
    try:
        ttl_cache_delete(ttl_key)
    except Exception:
        pass

def _fallback_state(player):
    player = dict(player or {})
    raw = _safe_dict(player.get("equipped_cosmetics"))
    return {slot: (dict(raw.get(slot)) if isinstance(raw.get(slot), dict) else None) for slot in PROFILE_EQUIPMENT_SLOTS}


def _decorate_item(item):
    item = dict(item or {})
    item["metadata"] = _safe_dict(item.get("metadata"))
    image_path = item.get("image_path")
    preview_path = item.get("preview_path") or image_path
    item["image_url"] = asset_url(image_path) if image_path else None
    item["preview_url"] = asset_url(preview_path) if preview_path else item.get("image_url")
    return item


def build_equipment_state(player):
    """Trả về dict slot -> thông tin vật phẩm đang trang bị."""
    player = dict(player or {})
    user_id = player.get("id")
    fallback = _fallback_state(player)
    if not user_id:
        return fallback

    request_key, ttl_key = _cache_keys(user_id)
    try:
        cached = cache_get(request_key)
        if cached is not None:
            return cached
        shared = ttl_cache_get(ttl_key)
        if shared is not None:
            return cache_set(request_key, shared)
    except Exception:
        pass

    try:
        equipment_result = execute_query(
            db.table("user_equipment")
            .select("*")
            .eq("user_id", str(user_id)),
            "profile_equipment_rows",
            attempts=2,
        )
        equipment_rows = [dict(row) for row in (equipment_result.data or [])]
        item_ids = sorted({str(row.get("item_id")) for row in equipment_rows if row.get("item_id")})
        if not item_ids:
            state = {slot: None for slot in PROFILE_EQUIPMENT_SLOTS}
            try:
                ttl_cache_set(ttl_key, state, 15)
                cache_set(request_key, state)
            except Exception:
                pass
            return state

        item_result = execute_query(
            db.table("shop_items").select("*").in_("id", item_ids),
            "profile_equipment_items",
            attempts=2,
        )
        items_by_id = {
            str(item.get("id")): _decorate_item(item)
            for item in (item_result.data or [])
        }
        state = {slot: None for slot in PROFILE_EQUIPMENT_SLOTS}
        for equipment in equipment_rows:
            slot = str(equipment.get("slot") or "")
            if slot not in state:
                continue
            item = items_by_id.get(str(equipment.get("item_id")))
            if item:
                item = dict(item)
                item["inventory_id"] = equipment.get("inventory_id")
                item["equipped_at"] = equipment.get("equipped_at")
                state[slot] = item
        try:
            ttl_cache_set(ttl_key, state, 15)
            cache_set(request_key, state)
        except Exception:
            pass
        return state
    except Exception as exc:
        try:
            app.logger.debug("Profile equipment fallback: %s", exc)
        except Exception:
            pass
        return fallback
