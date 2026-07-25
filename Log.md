# Collap_V1.14.4

- `app.py` (khoảng dòng 65): cập nhật `APP_VERSION` từ `Collap_V1.14.2` lên `Collap_V1.14.4` để URL CSS/JS đổi phiên bản và trình duyệt/Vercel tải giao diện mới thay vì dùng cache cũ.
- `templates/room_detail.html`: giữ bố cục Thông tin phòng đấu + Lịch sử đấu ở cột bên phải.
- `templates/_room_live_content.html`: giữ đồng bộ cột phải sau mỗi lần polling.
- `static/style.css`: giữ bố cục gọn 4 cột trên desktop; không thay API, RP hoặc xử lý kết quả.
- Khác `Collap_V1.14.3`: sửa nguyên nhân giao diện không thay đổi do biến phiên bản vẫn còn là `Collap_V1.14.2`, trong khi CSS/JS được cache `immutable` 1 năm.
