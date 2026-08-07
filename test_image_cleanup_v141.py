from pathlib import Path
ROOT = Path(__file__).parent

def test_room_images_are_remote_only():
    assert not (ROOT / "static/assets/room_v2").exists()

def test_upload_staging_removed_from_runtime_project():
    assert not (ROOT / "UPLOAD_SUPABASE").exists()

def test_unused_trophies_removed():
    for name in ("trophy_gold.svg", "trophy_silver.svg", "trophy_bronze.svg"):
        assert not (ROOT / "static" / name).exists()

def test_mode_helper_points_only_to_supabase_v140():
    text=(ROOT / "modules/static_asset_service.py").read_text(encoding="utf-8")
    assert "pes-assets/room-assets/v1.3.40/modes" in text
    assert "assets/room_v2/modes/{filename}" not in text

def test_room_helper_points_to_supabase_v1318():
    text=(ROOT / "modules/static_asset_service.py").read_text(encoding="utf-8")
    assert "pes-assets/room-assets/v1.3.18" in text
    assert 'url_for("static", filename=f"assets/room_v2/' not in text

def test_room_css_has_no_local_room_image_fallback():
    css = "\n".join(p.read_text(encoding="utf-8") for p in (ROOT / "static/css/room").glob("*.css"))
    assert "assets/room_v2/" not in css
    assert "room-texture-blue.webp" not in css
