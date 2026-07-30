# UPDATE MANIFEST V1.14.41.27

## Nội dung sửa

- Cho phép gửi lời mời thủ công tới người chơi đang ở một mình trong phòng chờ.
- Dashboard hiển thị nút Mời đấu cho người chơi đang ở phòng một mình, đồng bộ với Tìm Nhanh.
- Tìm Nhanh nhận diện cả tài khoản Admin/Owner khi Admin chọn Online.
- Bộ đếm Online tính cả Admin đang chọn Online.
- Trang Players hiển thị Admin/Owner để người chơi có thể nhận diện và gửi lời mời khi Admin Online.
- Di chuyển lựa chọn Online/Offline của Admin vào menu tài khoản ở mũi tên cạnh avatar.
- Sửa lỗi chuyển trang hoặc gửi form làm beacon đánh dấu Admin Offline ngay sau khi vừa chọn Online.
- Giữ timeout presence làm lớp dự phòng khi đóng trình duyệt hoặc mất kết nối.

## File thay đổi

- `app.py`
- `templates/base.html`
- `templates/dashboard.html`
- `static/style.css`
- `Log.md`

## Kiểm tra

- Python compile: thành công.
- Pytest: 33/33 thành công.
