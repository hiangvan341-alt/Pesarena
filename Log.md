# Collap_V1.14.3

- `templates/room_detail.html`: đổi khối Thông tin phòng đấu + Lịch sử đấu từ hàng dưới thành cột bên phải.
- `templates/_room_live_content.html`: đồng bộ cột phải khi polling cập nhật phòng.
- `templates/partials/room_dynamic_state.html`: đồng bộ cột phải và bổ sung Lịch sử đấu trong phần trạng thái động.
- `static/style.css`: làm gọn khung chủ/khách, cụm trung tâm; tạo bố cục 4 cột trên desktop và tự hạ xuống dưới trên tablet/mobile.
- Khác V1.14.2: chỉ thay bố cục giao diện phòng, giữ nguyên API, RP, xử lý kết quả và polling.
