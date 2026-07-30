# UPDATE MANIFEST V1.14.41.5

## Mục tiêu
Tích hợp module bật/tắt riêng hai chế độ Rank thường và Random 3 chọn 1 vào nền V1.14.41.4 mà không làm mất logic giới hạn Rank công bằng.

## Chức năng
- Admin có công tắc `Rank thường` độc lập với `Random 3 chọn 1`.
- Khi tắt Rank thường, hệ thống bắt buộc bật Random 3 chọn 1.
- Phòng Rank mới mặc định dùng Random 3 chọn 1 khi Rank thường đang tắt.
- Phòng Rank thường đang `waiting_ready` được chuyển sang Random 3 chọn 1.
- Không đổi trận đang `playing`, chờ kết quả hoặc chờ xác nhận.
- Luồng đá tiếp và sau xác nhận giữ đúng trạng thái công tắc hiện tại.
- Thẻ Rank thường bị ẩn khỏi giao diện người chơi khi đã tắt.
- Khi chỉ còn một chế độ, khối chọn chế độ tự căn giữa một cột.

## File chính thay đổi
- `app.py`
- `modules/admin_system_routes.py`
- `modules/room_rematch_routes.py`
- `modules/room_result_routes.py`
- `modules/room_team_routes.py`
- `modules/rank_mode_toggle/service.py`
- `templates/admin.html`
- `templates/room_detail.html`
- `templates/_room_live_content.html`
- `templates/partials/room_dynamic_state.html`
- `templates/base.html`
- `static/css/rank_mode_toggle.css`
- `test_rank_mode_toggle.py`

## Database
Không cần chạy SQL mới. Công tắc được lưu trong `system_settings` hiện có.

## Kiểm tra sau deploy
1. Bật cả hai chế độ và xác nhận phòng hiển thị hai lựa chọn.
2. Tắt Rank thường và lưu; Random 3 chọn 1 phải tự bật.
3. Tạo phòng mới; phòng phải mặc định Random 3 chọn 1.
4. Phòng Rank thường đang chờ phải chuyển sang Random 3 chọn 1.
5. Trận đang chơi phải giữ nguyên và hoàn thành bình thường.
6. Bật lại Rank thường; giao diện phải hiển thị lại hai lựa chọn.
