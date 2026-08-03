# PES Arena V1.14.41.78 – Room Session Guard Fix

## Lỗi đã sửa
- Người chơi đang thi đấu nhưng chuyển sang cửa sổ PES/Parsec có thể bị phòng tự đóng sau 60 phút không có thao tác trên web.
- Khi phòng vừa bị đóng, bộ kiểm tra phiên 60 phút có thể đưa người chơi về trang đăng nhập.

## Thay đổi
- Kéo thời gian bảo vệ phòng đang thi đấu từ 60 phút lên 4 giờ.
- Request của trang/API phòng đấu được tính là hoạt động hợp lệ trước khi bộ lọc idle xử lý.
- Trang phòng tiếp tục đồng bộ phiên khi tab nằm nền để người chơi có thể thi đấu trong PES/Parsec.
- Vẫn giữ timeout 60 phút cho người dùng không ở phòng đấu.

## Phạm vi
- Không thay đổi RP, kết quả trận, Shop, Lucky Box, Profile, BXH hoặc Admin.
- Không cần chạy SQL.
