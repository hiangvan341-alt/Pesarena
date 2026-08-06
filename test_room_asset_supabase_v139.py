from pathlib import Path

ROOT = Path(__file__).parent
UPLOAD = ROOT / "UPLOAD_SUPABASE" / "UPLOAD_VAO_BUCKET_public-assets" / "room-assets" / "v1.3.9"

def test_upload_bundle_has_20_webp():
    assert len(list(UPLOAD.rglob("*.webp"))) == 20

def test_room_asset_helper_exists():
    text = (ROOT / "modules" / "static_asset_service.py").read_text(encoding="utf-8")
    assert "def room_asset_url" in text
    assert "ROOM_ASSET_BASE_URL" in text

def test_room_template_uses_helper():
    text = (ROOT / "templates" / "room_detail.html").read_text(encoding="utf-8")
    assert "room_asset(" in text
