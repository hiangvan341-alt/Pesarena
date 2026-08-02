# PES Arena V1.14.41.63

## Thay đổi
- Thêm công tắc Admin bật/tắt hiển thị cảnh báo IP dùng chung.
- Mặc định bỏ qua Admin và tài khoản do Admin tạo/import.
- Cho phép đánh dấu từng tài khoản là tin cậy để bỏ cảnh báo IP, không ảnh hưởng RP.
- Random 3 chọn 1 tiếp tục lấy tỷ lệ Tier riêng theo RP/Rank của từng người; lưu thêm snapshot RP, Rank và tỷ lệ Tier vào trạng thái random để kiểm tra.
- Sửa phiên đăng nhập: tab đang hiển thị được gia hạn định kỳ; nhận thêm chuột di chuyển, cuộn, bàn phím, chạm và submit là hoạt động thật.
- Endpoint đồng bộ hoạt động có thể gia hạn phiên trước khi bộ lọc 60 phút ép đăng xuất.
- Khởi tạo mốc hoạt động ngay khi player hoặc Admin đăng nhập.

## File chính
- app.py
- modules/admin_system_routes.py
- modules/admin_player_routes.py
- templates/admin.html
- static/js/session-timeout.js
- static/style.css
