"""Điểm nối trang bị hồ sơ cho Shop/Kho đồ ở các phiên bản sau.

Phiên bản hiện tại chỉ chuẩn hóa trạng thái từ dữ liệu người chơi nếu các trường
đã tồn tại. Không truy vấn bảng mới và không yêu cầu migration SQL.
"""

PROFILE_EQUIPMENT_SLOTS = (
    "avatar_frame",
    "profile_banner",
    "profile_badge",
    "name_style",
    "profile_card_theme",
)


def build_equipment_state(player):
    """Trả về trạng thái trang bị an toàn, tương thích ngược với schema hiện tại."""
    player = dict(player or {})
    raw = player.get("equipped_cosmetics")
    raw = dict(raw) if isinstance(raw, dict) else {}
    return {slot: raw.get(slot) for slot in PROFILE_EQUIPMENT_SLOTS}
