# TEST REPORT V1.14.41.50

- Python compile: thành công (`app.py`, `modules/room_access_routes.py`, `modules/profile/equipment_service.py`).
- Jinja parse: thành công (`templates/room_detail.html`, `templates/_room_live_content.html`).
- Hotfix source tests: `5 passed / 0 failed`.
- Kiểm tra route: chỉ chủ phòng, chỉ trước khi trận bắt đầu, cho phép kick dù khách đã Sẵn sàng.
- Không có thao tác trừ RP trong route kick; trạng thái khách được đặt lại và khách nhận thông báo không bị trừ RP.
- Nút kick được chuyển vào ngay thẻ đối thủ, bên dưới trạng thái Sẵn sàng/Chưa sẵn sàng.
- Không cần SQL mới.

Lưu ý: đây là patch overlay; bộ test toàn repo cần chạy sau khi dán vào source đầy đủ.
