# Collap_V1.14.36_ZCOIN_UI_FIX

- Dựa trên source `Collap_V1.14.35`.
- Khôi phục menu tài khoản xổ xuống khi bấm tên người chơi.
- Menu tự đóng khi bấm ra ngoài hoặc nhấn phím Esc.
- Tinh gọn Ví Zcoin: chỉ giữ logo, số dư và lịch sử giao dịch.
- Xóa khung “Giai đoạn 1” và toàn bộ roadmap nội bộ khỏi giao diện người chơi.
- Xóa các nhãn/mô tả lặp lại không cần thiết.
- Không thay đổi database, công thức RP, phòng đấu hoặc các chức năng khác.
- Không cần chạy SQL.

---

# Collap_V1.14.35

- `modules/zcoin/` (toàn bộ thư mục): thêm module Zcoin độc lập gồm service, route ví, thao tác cộng/trừ và dữ liệu quản trị.
- `templates/zcoin/`, `static/css/zcoin.css`, `static/js/zcoin.js` (toàn bộ file): thêm giao diện ví, tab Admin Zcoin, CSS và tìm kiếm người chơi.
- `app.py` (khu vực quyền Admin, session người dùng, đăng ký service/route): kết nối module Zcoin; thêm quyền `zcoin_view`, `zcoin_manage`; đồng bộ số dư Zcoin vào session.
- `modules/admin_dashboard_routes.py` (khoảng dòng 165–230): tải dữ liệu thống kê và giao dịch cho tab Zcoin.
- `templates/base.html` (head và topbar): hiển thị số dư, menu ví và lịch sử Zcoin.
- `templates/admin.html` (tab, phân quyền và panel): thêm khu vực quản trị Zcoin mà không làm mất cấu hình RP hiện tại.
- Không chạy SQL; tiếp tục dùng `users.zcoin_balance`, `zcoin_transactions` và RPC `adjust_zcoin_balance` đã có trên Supabase.

## Collap_V1.14.38_ZCOIN_REWARDS_MODULE
- Tách `modules/daily_checkin/` và `modules/gift_codes/`; không đưa nghiệp vụ mới vào `app.py`.
- Điểm danh 7 ngày nhận lần lượt 100 / 120 / 150 / 180 / 220 / 280 / 450 Zcoin.
- Gift Code hỗ trợ thời gian bắt đầu, hết hạn theo phút/giờ/ngày, tổng lượt dùng và giới hạn mỗi tài khoản.
- Admin quản lý Gift Code ngay trong tab Zcoin.
- Member mở Điểm danh và Gift Code từ menu tài khoản.
- Hiệu ứng nhận Zcoin dùng confetti, không phát âm thanh và chỉ chạy một lần.
- Cần chạy `docs/update_zcoin_rewards_v1_14_38.sql`; SQL không xóa dữ liệu cũ.

## Collap_V1.14.39_ADMIN_ZCOIN_TAB_FIX
- Sửa tab Zcoin/Gift Code bị ẩn với các tài khoản Admin không mang `admin_level=owner`.
- Mọi tài khoản Admin hợp lệ đều được xem và quản lý Zcoin/Gift Code.
- Đồng bộ giới hạn tạo Gift Code và điều chỉnh Zcoin cho toàn bộ Admin.
- Không thay đổi quyền của player, không thay đổi schema và không cần chạy SQL.

