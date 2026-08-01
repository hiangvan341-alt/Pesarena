# UPDATE MANIFEST V1.14.41.51

## Sửa lỗi xóa tài khoản làm tụt RP người khác

### Nguyên nhân
- `delete_player_safe()` xóa toàn bộ trận liên quan bằng `delete_match_safe()`.
- `delete_match_safe()` mặc định gọi `reverse_confirmed_match_result()`, nên hoàn tác RP và thống kê của cả tài khoản bị xóa lẫn mọi đối thủ từng gặp.
- Trận gắn với phòng có thể bị xử lý lại lần hai do danh sách trận/phòng đã được cache trước khi xóa.

### Thay đổi
- Thêm tham số `reverse_result` cho `delete_room_safe()` và `delete_match_safe()`.
- Khi Admin xóa riêng một trận/phòng, hành vi hoàn tác RP cũ vẫn được giữ nguyên.
- Khi Admin xóa tài khoản, các trận liên quan bị xóa nhưng không hoàn tác RP/thống kê của đối thủ.
- Dùng `related_match_ids` để tránh xử lý cùng một trận hai lần.

### File sửa
- `app.py`
- `modules/data_cleanup_service.py`
- `TEST_DELETE_PLAYER_RP_V1.14.41.51.py`
