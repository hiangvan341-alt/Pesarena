# UPDATE MANIFEST · V1.14.41.43

## Phạm vi

Lucky Box Giai đoạn 2B: trang quản trị Draft/Publish, chỉnh tỷ lệ từng reward, đồng bộ Shop, validator và audit log. Không làm UI mở hộp cho người chơi và không làm animation.

## File mới

- `templates/admin_luckybox/index.html`
- `static/css/luckybox_admin.css`
- `docs/update_luckybox_admin_v1_14_41_43.sql`
- `docs/LUCKYBOX_PHASE2B_V1.14.41.43.md`
- `test_luckybox_admin_source.py`

## File sửa

- `app.py`: tăng `APP_VERSION` thành `V1.14.41.43`.
- `modules/luckybox/repository.py`: bổ sung RPC Admin và audit log.
- `modules/luckybox/service.py`: validate form, chuẩn hóa ngày giờ và context Admin.
- `modules/luckybox/routes.py`: thêm route quản trị, clone, sync, save và publish.
- `templates/admin.html`: nút mở Quản trị Lucky Box.
- `templates/admin_luckybox/preview.html`: liên kết trở lại trang quản trị tỷ lệ.
- `test_luckybox_core_source.py`: cập nhật version kỳ vọng.

## RPC mới/thay thế

- `lucky_box_validate_rate_payload`
- `validate_lucky_box_rate_version`
- `save_lucky_box_config`
- `save_lucky_box_rate_version`
- `save_lucky_box_reward`
- `clone_lucky_box_rate_version`
- `sync_lucky_box_rewards`
- `publish_lucky_box_rate_version` được thay bằng bản dùng validator chung.

## Trạng thái Production

- Không tự bật Lucky Box.
- Không tự publish Draft hiện tại.
- Chưa promote Production trước khi kiểm tra Vercel Preview.
