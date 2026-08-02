# PES Arena V1.14.41.62

- Nút **Remember this account** gửi lựa chọn lên máy chủ, giữ phiên đăng nhập tối đa 30 ngày.
- Tích hợp Password Manager của trình duyệt để trình duyệt có thể lưu cả tài khoản và mật khẩu; không lưu mật khẩu dạng rõ trong localStorage.
- Tài khoản do Admin tạo nhanh hoặc import CSV được phép dùng mật khẩu tối thiểu 1 ký tự, ví dụ `1`.
- Tài khoản do Admin tạo/import không bị khóa bởi liên kết thiết bị và không bị đưa vào cảnh báo trùng IP.
- Ngoại lệ thiết bị/IP không ảnh hưởng thi đấu: các tài khoản này vẫn tính trận, W/H/B và RP như người chơi bình thường.

File sửa: `app.py`, `modules/admin_account_routes.py`, `templates/admin.html`, `templates/login.html`, `Log.md`.
