# Rà soát cuối dự án — V1.14.41.19

## Đã sửa trực tiếp

1. **Loại 2 ảnh kiểm thử không được gọi ở giao diện**
   - `static/rank_contact_test.png`
   - `static/rank_icons_contact_test.png`
   - Giảm khoảng 1,53 MB dữ liệu nguồn/ZIP.

2. **Không tải CSS module trên mọi trang**
   - `rank_mode_toggle.css`: chỉ tải ở `room_detail` và `admin`.
   - `parsec_room.css`: chỉ tải ở `room_detail` và `profile`.
   - Các trang BXH, lịch sử, cửa hàng, hướng dẫn… giảm 2 request CSS không cần thiết.

3. **Sửa lỗi gọi nhầm hàm polling online**
   - Đổi `updateOnlineFloatingCountSmart` (không tồn tại) thành `updateOnlineFloatingCount`.
   - Tránh lỗi JavaScript làm bộ đếm online không chạy ở trang người chơi.

4. **Không tạo timer bảo trì khi trang không có bộ đếm**
   - Trước đây mọi trang đều chạy `setInterval(..., 1000)` dù không có phần tử đếm ngược.
   - Hiện chỉ tạo timer khi tồn tại `[data-maintenance-countdown]`.

## Kết quả rà soát

### CSS
- Không phát hiện lỗi ngoặc/cú pháp làm hỏng file CSS.
- `style.css` còn nhiều selector được khai báo ở nhiều breakpoint và nhiều giai đoạn giao diện cũ.
- Không xóa hàng loạt tự động vì nhiều khai báo là override có chủ đích theo `@media`, theme và trạng thái phòng; xóa mù có nguy cơ làm sai giao diện hiếm.
- Module Parsec vẫn được cô lập trong `.parsec-room-panel`, không dùng class `.btn`, nên không còn bị nút vàng toàn cục ghi đè.

### Request và polling
- Polling dùng `PESNet.createPoller` với key riêng và single-flight, hạn chế vòng lặp trùng.
- Tab ẩn không tiếp tục polling ở các luồng chính (`runWhenHidden: false`).
- Phòng đấu có polling riêng cho trạng thái và chat; đây là request cần thiết cho đồng bộ thời gian thực.
- Không thấy hai poller cùng key được tạo đồng thời trên cùng trang.

### Tải tài nguyên
- Ảnh trong `SUPABASE_ASSET_MANIFEST.csv` không được đóng gói lại.
- CSS/JS cửa hàng và hiệu ứng chuỗi thắng đang được tải theo template sử dụng, không tải toàn cục.
- Giữ `ranks/rank_icons_v1846_sheet.png` vì đây là tài nguyên nguồn chưa có bằng chứng chắc chắn có thể xóa an toàn.

### Lệnh trùng và gọi thừa
- Không phát hiện route Flask trùng tên endpoint gây ghi đè.
- Không phát hiện file JavaScript giống hệt nhau.
- Các nút copy dùng một listener ủy quyền toàn cục; không gắn listener riêng cho từng nút.

## Khuyến nghị sau deploy
- Mở DevTools → Network → Disable cache → tải lại từng trang chính để xác nhận số request thực tế.
- Không tiếp tục nối CSS vá vào cuối `style.css`; các module mới nên có file CSS riêng và selector gốc riêng.
