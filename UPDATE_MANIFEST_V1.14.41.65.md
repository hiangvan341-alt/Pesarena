# V1.14.41.65

- Sửa bảo vệ phiên khi đang chơi, chờ xác nhận hoặc tranh chấp bằng truy vấn trực tiếp bảng phòng, không phụ thuộc cache serverless.
- Dùng chung `PROTECTED_ROOM_STATUSES`; vẫn bảo vệ khi một phía vừa mất kết nối nhưng phòng đang ở trạng thái cần hoàn tất.
- Admin hiển thị trạng thái tải bảng `user_devices`, số bản ghi IP, số tài khoản có IP và số nhóm trùng; không còn âm thầm báo “không trùng” khi truy vấn lỗi.
- Thêm nút tải lại dữ liệu IP.
- Đổi “Remember this account” thành “Ghi nhớ đăng nhập trên thiết bị này” và giải thích rõ mật khẩu do trình duyệt quản lý.
- Cập nhật kiểm thử nguồn cho phiên bản mới.
