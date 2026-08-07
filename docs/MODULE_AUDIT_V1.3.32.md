# Báo cáo tách module V1.3.32

## 1. Admin đã tách theo tab

`templates/admin.html` chỉ còn khung chung: tiêu đề, thanh tab và một lệnh include tab đang mở.

Các tab độc lập nằm tại:

- `templates/admin/tabs/overview.html`
- `templates/admin/tabs/users.html`
- `templates/admin/tabs/passwords.html`
- `templates/admin/tabs/rooms.html`
- `templates/admin/tabs/matches.html`
- `templates/admin/tabs/match-report.html`
- `templates/admin/tabs/rank-modes.html`
- `templates/admin/tabs/test-data.html`
- `templates/admin/tabs/system.html`
- `templates/admin/tabs/economy.html`
- `templates/admin/tabs/rp-tools.html`
- `templates/admin/tabs/logs.html`

## 2. Route `/admin` tải theo nhu cầu

Route nhận `?tab=<ten-tab>` và chỉ tải nhóm dữ liệu cần cho tab đó.

- `overview`: user, phòng, trận, lời mời, yêu cầu mật khẩu.
- `users`: user, IP trùng, mở khóa chế độ.
- `passwords`: yêu cầu đặt lại mật khẩu.
- `rooms`: phòng và lời mời.
- `matches`: trận và tranh chấp.
- `match-report`: trận, phòng liên quan và dữ liệu series.
- `rank-modes`: cấu hình chế độ Rank.
- `system`: người chơi cần cho reset lượt, cấu hình hệ thống và chế độ.
- `logs`: nhật ký Admin.
- Các tab còn lại không gọi các truy vấn phòng/trận/user không cần thiết.

## 3. JavaScript Admin

`static/js/admin_dashboard.js` không còn ẩn/hiện toàn bộ panel đã dựng sẵn. Khi bấm tab, trình duyệt chuyển tới URL của module tương ứng. Nút được đánh dấu đang tải để người dùng thấy lệnh đã được nhận.

## 4. Parsec và lịch sử phòng

- Form Link Parsec chuyển sang một hàng: ô link + Lưu + Xóa.
- Panel Parsec dùng chiều cao theo nội dung, không còn `flex: 1` tạo khoảng trống.
- Lịch sử đấu được tăng vùng cuộn tối đa.

## 5. CSS

- `parsec_room.css`: style nền tảng cho module Parsec.
- `arena_room_v2.css`: override cuối cùng chỉ trong `.arena-room-v2` để đồng bộ phòng đấu.
- Nút Mời đấu / Tìm nhanh / Thoát phòng dùng selector riêng, tránh thay đổi tất cả nút toàn hệ thống.

## 6. Phần còn nên tách tiếp

- Hàm `admin()` vẫn chứa khối tính báo cáo trận khá dài. Nên chuyển toàn bộ phép tổng hợp sang `modules/admin_reports/service.py` trong bản sau.
- `room_detail.html` và `_room_live_content.html` còn nhiều đoạn giao diện trùng nhau. Nên tiếp tục chuyển từng trạng thái phòng sang partial chung để tránh sửa hai nơi.
