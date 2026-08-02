# PES Arena V1.14.41.66

## Lỗi đã sửa

- Sửa lỗi khách đã vào phòng nhưng chủ phòng vẫn thấy trạng thái “Đang chờ đối thủ”.
- Nguyên nhân: khóa trạng thái phòng không chứa `guest_user_id`. Khi khách tham gia, `status` vẫn là `waiting_ready` và `guest_ready` vẫn là `false`, nên API trả `204 Unchanged` và trình duyệt chủ phòng không tải lại giao diện.
- Bổ sung `host_user_id` và `guest_user_id` vào `build_room_state_key()` để mọi thay đổi thành viên phòng đều kích hoạt làm mới giao diện.
- Không thêm polling mới và không tăng tần suất request.

## File thay đổi

- `app.py`
- Các bài test phiên bản
- `test_room_guest_visibility_v1144166.py`
