# UPDATE MANIFEST V1.14.41.31

## Mục tiêu
Khắc phục trạng thái lời mời Tìm Nhanh bị treo và bảo đảm lời mời thực sự được gắn với phòng trước khi báo thành công.

## File thay đổi
- `app.py`
- `static/js/quick_match.js`
- `static/css/quick_match.css`
- `Log.md`

## Luồng mới
1. Tạo lời mời pending.
2. Gắn `invite_id` vào đúng phòng trống của người gửi.
3. Chỉ trả `ok: true` khi bước 2 có dữ liệu trả về.
4. Poll trạng thái đối chiếu trực tiếp: lời mời, phòng người gửi, presence đối thủ, trận/phòng/lời mời khác của đối thủ.
5. Đối thủ offline/bận thì chuyển người tiếp theo; phòng đã có khách thì dừng toàn bộ chuỗi.

## Kiểm tra
- `python -m py_compile app.py modules/quick_match/service.py`
- `node --check static/js/quick_match.js`
- `pytest -q` → 35 passed
