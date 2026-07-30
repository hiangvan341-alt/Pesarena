# V1.14.41.32 — Event-driven request & static motion optimization

- Heartbeat: 60 giây dự phòng; gọi ngay khi có thao tác thật, giới hạn tối đa 1 lần/30 giây.
- Pending invites: 30 giây dự phòng; gọi ngay khi focus/quay lại tab/sự kiện lời mời.
- Active room: bỏ polling định kỳ; chỉ gọi khi tải trang, focus, quay lại tab hoặc sự kiện phòng.
- Announcement: giảm từ 30 giây xuống 5 phút; vẫn gọi ngay khi focus/quay lại tab.
- Online count: bỏ polling 3 phút; chỉ gọi khi tải trang/focus/thay đổi presence.
- Quick Match status: 3 giây -> 5 giây, chỉ tồn tại khi có lời mời đang pending.
- Room state: 4–10 giây -> 6–15 giây tùy trạng thái; vẫn hỗ trợ gọi ngay sau thao tác.
- Room chat: 15 giây -> 30 giây và chỉ khởi động khi panel chat đang hiển thị.
- Lobby chat: 30 giây -> 45 giây, chỉ chạy khi khung chat mở.
- Tắt các hoạt ảnh trang trí chạy vô hạn: hạt nền sân, orbit bảo trì, icon nhấp nhô, pulse tìm nhanh.
- Giữ hoạt ảnh phản hồi sự kiện thật như thông báo thành tích/Zcoin.
