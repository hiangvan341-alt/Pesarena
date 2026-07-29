"""URL tài nguyên tĩnh có thể chuyển sang Supabase Storage.

Thiết lập STATIC_ASSET_BASE_URL thành URL public của thư mục assets, ví dụ:
https://PROJECT.supabase.co/storage/v1/object/public/pes-assets/v1
Khi chưa thiết lập, hệ thống tự dùng file trong thư mục /static.
"""
from __future__ import annotations

import os
from urllib.parse import quote

from flask import url_for


def asset_base_url() -> str:
    return (os.getenv("STATIC_ASSET_BASE_URL") or "").strip().rstrip("/")


def asset_url(filename: str) -> str:
    clean = str(filename or "").strip().lstrip("/")

    # Shop Phase 3 assets are shipped inside the application package under
    # ``static/shop``. They must stay on Flask/Vercel static URLs even when
    # STATIC_ASSET_BASE_URL points legacy assets to Supabase Storage.
    # Otherwise the app generates Supabase URLs for objects that were never
    # uploaded there, causing broken Shop cards and preview images.
    if clean == "shop" or clean.startswith("shop/"):
        return url_for("static", filename=clean)

    base = asset_base_url()
    if base:
        return f"{base}/{quote(clean, safe='/')}"
    return url_for("static", filename=clean)
