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
    base = asset_base_url()
    if base:
        return f"{base}/{quote(clean, safe='/')}"
    return url_for("static", filename=clean)
