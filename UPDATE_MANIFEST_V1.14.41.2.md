# UPDATE MANIFEST — Collap V1.14.41.2

## Mục đích
Hotfix bảo mật cấu hình Flask, khôi phục kiểm thử tự động RP và dọn file cache trước khi triển khai.

## File đã thay đổi

| File | Nội dung |
|---|---|
| `app.py` | Bắt buộc `FLASK_SECRET_KEY` trên Production/Preview; cập nhật version |
| `test_rp_engine.py` | Cập nhật RP V1.14.3 và chuyển thành 7 pytest tests |
| `.env.example` | Làm rõ biến môi trường bắt buộc |
| `Log.md` | Ghi lịch sử phiên bản |

## File đã dọn
- Toàn bộ thư mục `__pycache__`.
- Toàn bộ file `*.pyc`.

## SQL
Không có SQL mới cho V1.14.41.2.

Bản này vẫn phụ thuộc SQL của V1.14.41.1:

`docs/update_global_name_style_ticket_only_v1_14_41_1.sql`

## Kiểm tra trước khi deploy
1. Vercel phải có `FLASK_SECRET_KEY`.
2. Chạy `python test_rp_engine.py`.
3. Chạy `pytest -q test_rp_engine.py`.
4. Xác nhận SQL V1.14.41.1 đã chạy đúng Supabase Production.
