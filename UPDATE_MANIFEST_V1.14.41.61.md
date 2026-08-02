# PES Arena V1.14.41.61

Ngày cập nhật: 02/08/2026 (Asia/Bangkok)

## Nội dung
- Đặt `total_matches = wins + draws + losses` làm nguồn chuẩn duy nhất khi hiển thị BXH, Players, Dashboard và Hồ sơ.
- Tỷ lệ thắng không còn lấy mẫu số từ cột `total_matches` có thể bị lệch trong SQL.
- Khi xác nhận, hoàn tác hoặc xử thua do bỏ phòng, hệ thống ghi lại `total_matches` đúng bằng tổng W/H/B mới.
- Công thức 10 trận đầu trong RP Engine sử dụng tổng W/H/B.
- Import CSV không còn chấp nhận `total_matches` độc lập với W/H/B.
- Tính lại BXH giữ `total_matches` đồng bộ với W/H/B.

## File thay đổi
- `app.py`
- `modules/match_result_service.py`
- `modules/rp_engine.py`
- `modules/profile/service.py`
- `modules/admin_account_routes.py`
- `modules/admin_ranking_rebuild.py`
- 4 test kiểm tra phiên bản được cập nhật
- `test_total_matches_source_of_truth.py`
