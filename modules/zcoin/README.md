# Module Zcoin

- `service.py`: đọc lịch sử, định dạng số dư, cộng/trừ qua RPC và thống kê.
- `routes.py`: route ví người chơi và route điều chỉnh Zcoin của Admin.
- `admin.py`: chuẩn bị dữ liệu riêng cho tab Zcoin trong trang Admin.
- `templates/zcoin/`: giao diện ví và panel quản trị.
- `static/css/zcoin.css`: toàn bộ CSS của Zcoin.
- `static/js/zcoin.js`: tìm kiếm người chơi trong tab Zcoin.

Module vẫn dùng cột `users.zcoin_balance`, bảng `zcoin_transactions` và RPC `adjust_zcoin_balance` hiện có; không yêu cầu chạy lại SQL nếu database đã có đủ các thành phần này.
