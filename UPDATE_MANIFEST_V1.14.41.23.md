# V1.14.41.23

- Sửa lỗi HTTP 500 khi Admin tắt Random 3 chọn 1, bật Rank thường rồi lưu.
- Việc lưu công tắc hệ thống được tách khỏi bước dọn trạng thái phòng cũ; lỗi hậu xử lý không còn làm hỏng toàn bộ yêu cầu.
- Phòng Random 3 đang chờ được chuyển về `Smart Tier Random` khi Random 3 bị tắt.
- Giảm payload cập nhật phòng để tương thích schema production cũ.
- Thêm chốt kiểm tra cuối: Random 3 chỉ hợp lệ khi tạo đủ 6 CLB khác nhau.
- Giữ cơ chế cấm trùng CLB giữa chủ và khách bằng tên đã chuẩn hóa.
- Kiểm thử: 33/33 thành công.
