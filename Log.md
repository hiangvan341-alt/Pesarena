# Collap_V1.14.39.2

- `app.py` khoảng dòng 64, 580–610: đồng bộ phiên bản; lưu và đọc hai bộ hệ số người thắng/người thua, tương thích dữ liệu cấu hình cũ.
- `modules/admin_system_routes.py` khoảng dòng 91–125: Admin nhập, kiểm tra và lưu riêng 4 hệ số thắng cùng 4 hệ số thua.
- `templates/admin.html` khoảng dòng 575–600: thêm tám ô cấu hình, mặc định thắng `100–60–30–0%`, thua `100–70–40–10%`.
- `modules/repeat_opponent_rp_service.py` khoảng dòng 7–45, 220–245: áp dụng hệ số thua theo từng lần thay cho mức hard-code cũ.
- `modules/admin_ranking_rebuild.py` khoảng dòng 225–400 và `modules/ranking_rebuild_service.py` khoảng dòng 65–68: tính lại BXH và sửa tỷ số Admin dùng đúng cả hai bộ hệ số.
- `modules/rp_formula.py` khoảng dòng 9, 67–73: nâng công thức lên `RP_V1.14.3` và cập nhật mô tả hệ số.
