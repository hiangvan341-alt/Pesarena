"""Validation and presentation helpers for Lucky Box core."""

from __future__ import annotations

import uuid

from . import repository

BOX_CODE = "lucky_box_pes_arena"
MAX_PREVIEW_ITERATIONS = 10000


def configure(context):
    globals().update(context)
    repository.configure(context)


def _safe_int(value, default=0):
    try:
        return int(value)
    except (TypeError, ValueError, OverflowError):
        return default


def parse_iterations(value):
    iterations = _safe_int(value, 1000)
    if iterations < 1 or iterations > MAX_PREVIEW_ITERATIONS:
        raise ValueError(f"Số lượt mô phỏng phải từ 1 đến {MAX_PREVIEW_ITERATIONS}.")
    return iterations


def validate_request_id(value):
    clean = str(value or "").strip()
    if not clean or len(clean) > 120:
        raise ValueError("Mã chống mở trùng không hợp lệ. Hãy tải lại trang.")
    try:
        uuid.UUID(clean)
    except (ValueError, TypeError, AttributeError):
        raise ValueError("Mã chống mở trùng không hợp lệ. Hãy tải lại trang.")
    return clean


def build_admin_preview_context(actor, selected_rate_version_id=None, result=None, error=None):
    boxes = repository.list_boxes()
    selected_box = boxes[0] if boxes else None
    versions = repository.list_rate_versions(selected_box.get("id") if selected_box else None)
    selected_id = str(selected_rate_version_id or "")
    selected = next((row for row in versions if str(row.get("id")) == selected_id), None)
    if selected is None and versions:
        selected = versions[0]
        selected_id = str(selected.get("id"))
    rewards = repository.list_rewards(selected_id) if selected_id else []
    return {
        "actor": actor,
        "boxes": boxes,
        "selected_box": selected_box,
        "rate_versions": versions,
        "selected_rate_version": selected,
        "rewards": rewards,
        "preview_result": result,
        "preview_error": error,
        "max_preview_iterations": MAX_PREVIEW_ITERATIONS,
    }


def run_preview(actor, rate_version_id, iterations):
    clean_rate_id = str(rate_version_id or "").strip()
    if not clean_rate_id:
        raise ValueError("Chưa chọn phiên bản tỷ lệ Draft.")
    return repository.preview_rate_version(
        actor.get("id"), clean_rate_id, parse_iterations(iterations)
    )


def open_for_user(user, request_id, box_code=BOX_CODE):
    clean_key = validate_request_id(request_id)
    return repository.open_box(user.get("id"), box_code, clean_key)


def error_message(exc):
    text = str(exc or "")
    mapping = {
        "LUCKY_BOX_DISABLED": "Lucky Box hiện chưa được mở.",
        "LUCKY_BOX_NO_ACTIVE_RATE": "Lucky Box chưa có phiên bản tỷ lệ chính thức.",
        "LUCKY_BOX_INVALID_PRICE": "Giá mở Lucky Box chưa được cấu hình.",
        "LUCKY_BOX_DUPLICATE_POLICY_PENDING": "Cách xử lý vật phẩm trùng chưa được chốt.",
        "INSUFFICIENT_ZCOIN": "Bạn không đủ Zcoin để mở Lucky Box.",
        "LUCKY_BOX_REQUEST_CONFLICT": "Mã lượt mở đã được sử dụng cho yêu cầu khác.",
        "LUCKY_BOX_REWARD_POOL_INVALID": "Pool phần thưởng hiện không hợp lệ.",
        "LUCKY_BOX_DUPLICATE_ITEM": "Lượt mở gặp vật phẩm đã sở hữu nhưng chưa có quy tắc quy đổi.",
    }
    for code, message in mapping.items():
        if code in text:
            return message
    return "Không thể xử lý Lucky Box lúc này. Vui lòng thử lại sau."
