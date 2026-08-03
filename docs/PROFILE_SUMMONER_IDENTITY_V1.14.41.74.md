# PES Arena V1.14.41.74 — Profile Summoner Identity

## Mục tiêu
Làm mới riêng phần nhận diện đầu trang hồ sơ theo tinh thần hồ sơ game cạnh tranh cao cấp: avatar, tên, huy hiệu, rank và danh hiệu trở thành trọng tâm; vẫn giữ bản sắc PES Arena và không sao chép asset của trò chơi khác.

## Phạm vi
- Chỉ thay đổi `templates/profile.html` và `static/css/profile_showcase.css`.
- Giữ nguyên route, dữ liệu, biểu mẫu, lịch sử đấu, thành tích, Shop, Lucky Box, BXH và phòng đấu.
- Banner dùng `object-fit: contain`, không cắt mặt hoặc chi tiết quan trọng.
- Không cần SQL.

## Thay đổi giao diện
- Avatar lớn với bảng hạng nhỏ phía dưới.
- Tên người chơi, huy hiệu và trạng thái online nổi bật trực tiếp trên banner.
- Đường crest vàng và hàng thông tin ID/RP/rank.
- Bốn ô dấu ấn: danh hiệu, huy hiệu, chuỗi thắng, xếp hạng.
- Thống kê và hành động giữ ở bên phải hero.
- Responsive cho desktop, tablet và mobile.
