import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def read(path):
    return (ROOT / path).read_text(encoding="utf-8")

def test_version_and_python_parse():
    assert 'APP_VERSION = "V1.14.41.49"' in read("app.py")
    for path in ("app.py", "modules/profile/equipment_service.py", "modules/room_access_routes.py"):
        ast.parse(read(path), filename=path)

def test_profile_badge_is_loaded_in_public_player_maps():
    equipment = read("modules/profile/equipment_service.py")
    app = read("app.py")
    assert 'PUBLIC_PROFILE_SLOTS = ("avatar_frame", "name_style", "profile_badge")' in equipment
    assert "def build_profile_badge_map" in equipment
    assert "profile_badge_map = profile_equipment_service.build_profile_badge_map(safe)" in app
    assert 'item["profile_badge"] = profile_badge_map.get(user_id)' in app

def test_badge_is_rendered_in_players_and_room():
    players = read("templates/players.html")
    room = read("templates/room_detail.html")
    live = read("templates/_room_live_content.html")
    assert "p.profile_badge.image_url" in players
    for template in (room, live):
        assert "room.host_profile_badge.image_url" in template
        assert "room.guest_profile_badge.image_url" in template

def test_host_kick_route_is_guarded_and_resets_guest():
    routes = read("modules/room_access_routes.py")
    assert 'endpoint="room_kick_guest"' in routes
    assert 'room.get("status") != "waiting_ready"' in routes
    assert 'bool(room.get("guest_ready"))' in routes
    assert '"guest_user_id": None' in routes
    assert '"guest_ready": False' in routes
    assert '"host_kick_room_guest"' in routes
    assert 'create_user_notification(' in routes

def test_kick_button_exists_in_full_and_live_room_views():
    for path in ("templates/room_detail.html", "templates/_room_live_content.html"):
        template = read(path)
        assert "url_for('room_kick_guest'" in template
        assert "Đưa đối thủ ra khỏi phòng" in template
        assert "not room.guest_ready" in template
