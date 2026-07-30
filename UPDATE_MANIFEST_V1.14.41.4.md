# PES Arena V1.14.41.4 — Daily Rank Fair Count Hotfix

## Mục tiêu

Hoàn thiện quy tắc khi một người đã hết lượt Rank nhưng đối thủ vẫn còn lượt.

## Quy tắc sau nâng cấp

- Trận thứ 10 ngày thường hoặc trận thứ 15 cuối tuần vẫn được tính bình thường.
- Từ trận tiếp theo của một trong hai người, trận không cộng/trừ RP cho cả hai.
- Trận ngoài giới hạn không tác động chuỗi thắng/thua hoặc danh hiệu.
- Người còn lượt không bị mất lượt khi gặp người đã hết lượt.
- Trận vẫn lưu lịch sử và có ghi chú rõ nguyên nhân.
- Trận hòa vẫn tính một lượt nếu trận đó còn nằm trong giới hạn.

## File thay đổi

- `app.py`
- `modules/daily_rank_limit_service.py`
- `modules/match_result_service.py`
- `modules/admin_ranking_rebuild.py`
- `test_daily_rank_limit.py`
- `Log.md`

## Database

Không cần chạy SQL mới. Dữ liệu đánh dấu được lưu trong trường JSON `matches.rp_details` hiện có.

## Kiểm thử

```text
13 passed
```
