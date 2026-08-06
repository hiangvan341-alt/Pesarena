from pathlib import Path

ROOT = Path(__file__).resolve().parent
TEMPLATE = (ROOT / "templates" / "room_detail.html").read_text(encoding="utf-8")
CSS = (ROOT / "static" / "css" / "arena_room_v2.css").read_text(encoding="utf-8")
APP = (ROOT / "app.py").read_text(encoding="utf-8")


def test_version_and_namespace():
    assert 'APP_VERSION = "V1.3.5"' in APP
    assert 'class="room-view-shell arena-room-v2"' in TEMPLATE
    assert "css/arena_room_v2.css" in TEMPLATE
    assert "css/room_master.css" not in TEMPLATE


def test_four_column_master_grid():
    assert "grid-template-columns:minmax(0,31fr) minmax(250px,24fr) minmax(0,31fr) minmax(218px,14fr)" in CSS
    assert "grid-template-areas:'home center away rail'" in CSS
    assert "height:440px" in CSS


def test_mode_cards_and_names():
    assert "repeat(6,minmax(0,1fr))" in CSS
    assert "Cấm chọn CLB" in TEMPLATE
    assert "Cấm chọn BO3" not in TEMPLATE
    for code in ("rank_random", "random3_pick1", "tactical_bo3", "bo3", "ban_pick_bo3", "home_away"):
        assert (ROOT / "static" / "icons" / "rank_modes" / f"{code}.svg").exists()


def test_css_is_scoped_and_clean():
    assert "!important" not in CSS
    assert "inline-style" not in CSS
    for forbidden in ("\n.card{", "\n.button{", "\n.panel{", "\nh2{", "\ninput{"):
        assert forbidden not in CSS
    selectors = [line.strip() for line in CSS.splitlines() if line.strip().endswith("{")]
    assert all(line.startswith(".arena-room-v2") or line.startswith("@") or line.startswith("/*") for line in selectors)


def test_existing_room_actions_preserved():
    for endpoint in (
        "quick_match_invite",
        "room_leave",
        "room_guest_ready",
        "room_guest_unready",
        "room_submit_result",
        "room_select_ranked_mode",
    ):
        assert endpoint in TEMPLATE
