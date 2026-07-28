# Collap V1.14.39.6

- Bổ sung thống kê số trận theo chế độ Rank Random và Random 3 chọn 1 trong Báo cáo trận đấu Admin.
- Hiển thị số trận, tỷ lệ phần trăm và chế độ phổ biến hơn theo từng khoảng thời gian.
- Bổ sung hai cột chế độ vào bảng thống kê theo ngày.
- Không thay đổi database và không cần chạy SQL.

# Collap_V1.14.39.3

- `modules/daily_rank_limit_service.py` (khoảng dòng 1–260): thêm mốc reset lượt Rank riêng cho từng người chơi; chỉ đặt lại số trận được phép chơi, không xóa lịch sử và không reset trần +150 RP.
- `modules/admin_system_routes.py` (khoảng dòng 195–270): thêm route Admin reset lượt Rank hôm nay, kiểm tra công tắc đang bật và ghi nhật ký thao tác.
- `templates/admin.html` (khoảng dòng 550–600): thêm khối chọn người chơi và nút reset trong phần Giới hạn thi đấu Rank mỗi ngày.
- Khác V1.14.39.2: Admin có thể cấp lại đủ 10/15 lượt Rank trong ngày cho từng tài khoản mà không sửa hoặc xóa dữ liệu trận đấu.

## Collap_V1.14.39.5
- Rà soát cấu trúc module, route, template và CSS.
- Xóa module Zcoin legacy gây route trùng nếu import nhầm.
- Xóa `__pycache__` và `.pyc` khỏi bản phát hành.
- Thêm `AUDIT_V1.14.39.5.md` ghi kết quả kiểm tra và khuyến nghị tách tiếp.
- Giữ nguyên CSS phòng đấu/BXH vì các selector lặp chủ yếu nằm ở breakpoint và lớp vá phiên bản.
