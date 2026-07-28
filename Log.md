# Collap_V1.14.39.3

- `modules/daily_rank_limit_service.py` (khoảng dòng 1–260): thêm mốc reset lượt Rank riêng cho từng người chơi; chỉ đặt lại số trận được phép chơi, không xóa lịch sử và không reset trần +150 RP.
- `modules/admin_system_routes.py` (khoảng dòng 195–270): thêm route Admin reset lượt Rank hôm nay, kiểm tra công tắc đang bật và ghi nhật ký thao tác.
- `templates/admin.html` (khoảng dòng 550–600): thêm khối chọn người chơi và nút reset trong phần Giới hạn thi đấu Rank mỗi ngày.
- Khác V1.14.39.2: Admin có thể cấp lại đủ 10/15 lượt Rank trong ngày cho từng tài khoản mà không sửa hoặc xóa dữ liệu trận đấu.
