# Collap_V1.14.40.6_TOPBAR_AVATAR_FRAME

## Mục tiêu
Hiển thị Khung Avatar đang trang bị trong nút tài khoản ở góc trên bên phải.

## Thay đổi
- Bổ sung equipment context dùng chung cho `base.html`.
- Mở rộng macro `player_avatar` để hỗ trợ lớp khung trang trí.
- Giữ avatar và huy hiệu thành tựu rõ ràng ở kích thước nhỏ.
- Thêm cache 15 giây cho trạng thái trang bị và xóa cache ngay khi trang bị/gỡ.

## Không yêu cầu
- Không cần chạy thêm SQL.
- Không thay đổi dữ liệu Shop/Kho đồ.
