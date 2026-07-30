# UPDATE MANIFEST V1.14.41.33

## Sửa lỗi Tìm Nhanh chọn Admin đang Offline

- Tìm Nhanh nay bắt buộc `users.is_online = true` và `last_seen_at` còn hạn.
- Admin chọn Offline không còn được đưa vào danh sách ứng viên dù vừa thao tác.
- Tránh trạng thái người gửi thấy “đã gửi” nhưng phía Admin không nhận lời mời.
- Giữ kiểm tra lần hai ở API trạng thái để hủy lời mời nếu đối thủ Offline sau khi gửi.
- Không thay đổi CSS; lỗi nằm ở bộ lọc presence phía backend.
