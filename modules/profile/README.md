# Module Profile

- `routes.py`: endpoint hồ sơ, đổi tên hiển thị, tải/xóa avatar.
- `service.py`: xử lý ảnh và tổng hợp dữ liệu trang hồ sơ.
- `repository.py`: toàn bộ truy vấn cập nhật dữ liệu hồ sơ.
- `equipment_service.py`: điểm nối an toàn cho khung avatar, banner, huy hiệu, màu tên và theme hồ sơ ở Shop/Kho đồ sau này.

Các endpoint cũ được giữ nguyên nên template và liên kết trong app không phải thay đổi.
Bản V1.14.37 không thêm bảng/cột và không yêu cầu chạy SQL.
