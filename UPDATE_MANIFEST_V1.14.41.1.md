# Collap_V1.14.41.1_GLOBAL_NAME_STYLE_TICKET_ONLY_HOTFIX

## Sửa lỗi
- Màu tên đã trang bị hiển thị tại Cộng đồng Player, BXH đăng nhập, BXH công khai, bục Top 3 và tên trên avatar góc phải.
- Màu tên được tải theo lô cùng hệ thống mỹ phẩm hồ sơ, không tạo truy vấn N+1.
- Số Zcoin của vật phẩm hiển thị rõ trong giao diện sáng.
- Tắt hoàn toàn 2 lượt đổi tên miễn phí. Route mới dùng RPC riêng và mọi lần đổi tên bắt buộc tiêu thụ 1 Vé đổi tên.

## File SQL bắt buộc chạy
`docs/update_global_name_style_ticket_only_v1_14_41_1.sql`

## File code thay đổi
- app.py
- modules/profile/equipment_service.py
- modules/profile/repository.py
- modules/profile/routes.py
- templates/base.html
- templates/players.html
- templates/profile.html
- templates/ranking.html
- templates/public_ranking.html
- static/style.css
- static/css/shop_phase3.css
