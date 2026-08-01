# UPDATE MANIFEST · V1.14.41.42

## Phạm vi

Lucky Box Giai đoạn 2A: database, backend core, Admin Draft Preview và lịch sử tối thiểu. Không làm animation và không mở Lucky Box cho người chơi.

## File mới

- `modules/luckybox/__init__.py`
- `modules/luckybox/repository.py`
- `modules/luckybox/service.py`
- `modules/luckybox/routes.py`
- `templates/admin_luckybox/preview.html`
- `templates/luckybox/history.html`
- `templates/luckybox/opening_detail.html`
- `docs/update_luckybox_core_v1_14_41_42.sql`
- `docs/LUCKYBOX_PHASE2A_V1.14.41.42.md`
- `docs/LUCKYBOX_ASSET_MAPPING_V1.14.41.42.csv`
- `test_luckybox_core_source.py`

## File sửa

- `app.py`: tăng version và đăng ký module Lucky Box.
- `modules/static_asset_service.py`: thêm `LUCKYBOX_ASSET_BASE_URL`, không đổi `SHOP_ASSET_BASE_URL`.
- `templates/admin.html`: thêm liên kết Admin Preview.
- `.env.example`: thêm biến môi trường Lucky Box.

## Database mới

- `lucky_boxes`
- `lucky_box_rate_versions`
- `lucky_box_exclusive_items`
- `lucky_box_rewards`
- `lucky_box_openings`
- `lucky_box_opening_rewards`
- `lucky_box_admin_audit_logs`

## RPC mới

- `preview_lucky_box_rate_version`
- `publish_lucky_box_rate_version`
- `open_lucky_box`
- các helper chọn reward phía server.

## Rollback ứng dụng

Có thể rollback source về V1.14.41.41. Các bảng mới không ảnh hưởng luồng cũ và không cần xóa. Lucky Box mặc định tắt.
