# Báo cáo tối ưu Polling / Request — V1.14.41.32

## Sau tối ưu

| Luồng | Trước | Sau |
|---|---:|---:|
| Heartbeat | 30 giây | Sự kiện thao tác + dự phòng 60 giây |
| Pending invites | 20–30 giây | Sự kiện focus/tab + dự phòng 30 giây |
| Active room | 45–60 giây | Không polling; chỉ theo sự kiện |
| Announcement | 30 giây | Sự kiện focus/tab + dự phòng 5 phút |
| Online count | 3 phút | Không polling; tải trang/focus/presence event |
| Quick Match pending | 3 giây | 5 giây, chỉ khi có invite pending |
| Room state | 4–10 giây | 6–15 giây, gọi ngay sau thao tác |
| Room chat | 15 giây | 30 giây, chỉ khi panel hiển thị |
| Lobby chat | 30 giây | 45 giây, chỉ khi panel mở |

## Ghi chú kỹ thuật

Không thể loại bỏ hoàn toàn mọi polling trong kiến trúc HTTP hiện tại vì lời mời và thay đổi phòng có thể phát sinh từ thiết bị khác. Bản này chuyển phần lớn luồng sang gọi theo sự kiện và chỉ giữ polling thưa làm lớp dự phòng. Muốn 100% realtime không polling cần triển khai Supabase Realtime/WebSocket cho presence, invites, room state và chat.

## Hoạt ảnh

Đã tắt các animation trang trí chạy vô hạn: hạt nền sân, orbit bảo trì, icon nhấp nhô, pulse nút Tìm Nhanh. Giữ các animation chỉ xuất hiện khi có sự kiện thật như thưởng Zcoin hoặc thành tích.
