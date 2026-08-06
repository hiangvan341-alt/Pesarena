from pathlib import Path

ROOT = Path(__file__).resolve().parent
html = (ROOT / "templates/room_detail.html").read_text(encoding="utf-8")
css = (ROOT / "static/css/arena_room_v2.css").read_text(encoding="utf-8")

assert "room-center-primary-actions-three" in html
assert "room-quick-match-row" not in html
assert ":has(.room-quick-match-row)" not in css
assert not (ROOT / "static/css/room_master.css").exists()
assert not (ROOT / "static/icons/rank_modes").exists()
assert not (ROOT / "static/assets/room_v2/source_user_logo").exists()
for code in ["rank_random", "random3_pick1", "tactical_bo3", "bo3", "ban_pick_bo3", "home_away"]:
    assert (ROOT / f"static/assets/room_v2/modes/{code}.webp").exists()
    assert (ROOT / f"static/assets/room_v2/emblems/{code}.webp").exists()
print("V1.3.8 room UI cleanup: PASS")
