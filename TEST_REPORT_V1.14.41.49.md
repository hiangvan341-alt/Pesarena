# TEST REPORT · V1.14.41.49

- Python compile: thành công.
- Pytest: **77 passed / 0 failed**.
- Jinja: **48 template hợp lệ / 0 lỗi**.
- Không cần SQL migration.

## Phạm vi kiểm tra

- Huy hiệu `profile_badge` được tải theo lô cùng khung Avatar và màu tên.
- Cộng đồng Player hiển thị huy hiệu đang trang bị cạnh tên.
- Phòng đấu hiển thị huy hiệu của chủ phòng và khách ở cả trang đầy đủ lẫn nội dung polling.
- Route kick chỉ cho chủ phòng sử dụng khi `waiting_ready`, có khách và khách chưa Sẵn sàng.
- Kick dọn dữ liệu khách/đội, không trừ RP, xóa cache phòng và gửi thông báo cho khách.
