# PES Arena V1.14.41.76 — Profile Full-Bleed Banner

## Mục tiêu

Cho banner đang trang bị phủ toàn bộ khung Profile Arena Overview, thay vì chỉ hiển thị như một dải ảnh ở phần trên.

## Thay đổi

- Dùng banner làm background của toàn bộ `profile-v2-banner-stage`.
- Dùng `background-size: cover` để phủ kín khung.
- Giữ cụm avatar, tên, huy hiệu, RP, thành tích và Rank đặt trực tiếp trên banner.
- Bổ sung gradient tối có kiểm soát để chữ và nút luôn dễ đọc.
- Giữ ảnh `<img>` trong HTML nhưng làm trong suốt ở chế độ full-bleed để không thay đổi cấu trúc template.
- Trường hợp chưa trang bị banner vẫn dùng nền PES Arena mặc định.

## Phạm vi an toàn

- Chỉ chỉnh CSS trang Profile và tăng APP_VERSION.
- Không sửa Shop, Lucky Box, BXH, Admin, Room hoặc dữ liệu.
- Không cần SQL.

## Lưu ý hiển thị

`cover` sẽ cắt nhẹ hai mép ngang của banner 4:1 để phủ kín hero có tỷ lệ cao hơn. Chủ thể ở khu vực trung tâm vẫn được ưu tiên hiển thị.
