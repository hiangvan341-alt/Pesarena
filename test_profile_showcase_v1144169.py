from pathlib import Path

ROOT = Path(__file__).resolve().parent


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


def test_profile_showcase_release_version():
    assert 'APP_VERSION = "V1.14.41.71"' in read("app.py")


def test_profile_banner_uses_real_image_and_preserves_full_artwork():
    template = read("templates/profile.html")
    css = read("static/css/profile_showcase.css")
    assert 'class="profile-showcase-banner-image"' in template
    assert 'src="{{ equipped_banner.image_url }}"' in template
    assert "height:clamp(220px,16vw,290px)" in css
    assert ".profile-showcase-banner-image" in css
    assert "object-fit:contain" in css
    assert "background:transparent" in css
    assert "opacity:.86" in css
    assert "blur(30px)" in css
    assert "profile-header-card profile-header-with-avatar" not in template
    assert 'grid-template-areas:"identity stats" "identity actions"' in css
    assert "margin-top:-58px" in css
    assert ".profile-account-panel:only-child{grid-column:1/-1}" in css


def test_profile_showcase_includes_identity_stats_and_share_action():
    template = read("templates/profile.html")
    script = read("static/js/profile_showcase.js")
    for token in (
        "profile-showcase-identity",
        "profile-showcase-quick-stats",
        "profile-showcase-actions",
        "data-profile-share",
        "Quản lý trang bị",
        "Mở Cửa hàng",
    ):
        assert token in template
    assert "navigator.clipboard" in script
    assert "Đã sao chép liên kết" in script


def test_profile_showcase_assets_are_versioned():
    template = read("templates/profile.html")
    assert "css/profile_showcase.css" in template
    assert "js/profile_showcase.js" in template
    assert template.count("APP_VERSION|urlencode") >= 3
