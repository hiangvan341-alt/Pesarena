# Collap_V1.14.35

- `modules/zcoin/` (toàn bộ thư mục): thêm module Zcoin độc lập gồm service, route ví, thao tác cộng/trừ và dữ liệu quản trị.
- `templates/zcoin/`, `static/css/zcoin.css`, `static/js/zcoin.js` (toàn bộ file): thêm giao diện ví, tab Admin Zcoin, CSS và tìm kiếm người chơi.
- `app.py` (khu vực quyền Admin, session người dùng, đăng ký service/route): kết nối module Zcoin; thêm quyền `zcoin_view`, `zcoin_manage`; đồng bộ số dư Zcoin vào session.
- `modules/admin_dashboard_routes.py` (khoảng dòng 165–230): tải dữ liệu thống kê và giao dịch cho tab Zcoin.
- `templates/base.html` (head và topbar): hiển thị số dư, menu ví và lịch sử Zcoin.
- `templates/admin.html` (tab, phân quyền và panel): thêm khu vực quản trị Zcoin mà không làm mất cấu hình RP hiện tại.
- Không chạy SQL; tiếp tục dùng `users.zcoin_balance`, `zcoin_transactions` và RPC `adjust_zcoin_balance` đã có trên Supabase.

Khác V1.14.34: module Zcoin đã được ghép vào bản chính; giữ nguyên toàn bộ nâng cấp phòng đấu, giới hạn Rank và quy tắc RP gặp lại đối thủ.
