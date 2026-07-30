# PES Arena V1.14.41.22 — Random 3 chọn 1 Pool Fallback Fix

## Lỗi đã sửa

Random 3 chọn 1 có thể báo `Không có CLB phù hợp cho rank ...` khi:

- Rank của người chơi chỉ được cấu hình một hoặc vài Tier.
- Tier đó không còn đủ 6 CLB khác nhau cho hai bên.
- Danh sách 5 CLB gần nhất với cùng đối thủ làm cạn pool còn lại.

## Cách sửa

- Giữ nguyên nguyên tắc 6 lựa chọn trong cùng lượt không trùng nhau.
- Ưu tiên đúng tỷ lệ Tier theo Rank như trước.
- Khi Tier được cấu hình đã cạn, tự tìm Tier gần nhất còn CLB phù hợp.
- Nếu lịch sử 5 trận làm cạn toàn bộ pool, chỉ nới danh sách lịch sử; không nới danh sách đội đã xuất hiện trong lượt hiện tại.
- Chỉ báo lỗi khi bảng Supabase thực sự không còn đủ CLB hoạt động để tạo lựa chọn.

## File thay đổi

- `app.py`
- `Log.md`
- `UPDATE_MANIFEST_V1.14.41.22.md`

## Kiểm tra

- Python compile: thành công.
- Pytest: 31/31 bài test thành công.
