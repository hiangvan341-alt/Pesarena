# TEST REPORT · V1.14.41.42

## Đã chạy

- `python -m compileall -q .`: PASS.
- Biên dịch 46 Jinja templates bằng `Environment.get_template`: PASS, 0 lỗi.
- `pytest -q`: PASS, 52 test; FAIL 0.

## Phạm vi test Lucky Box mới

- APP_VERSION và đăng ký module.
- Python AST/compile.
- Admin Preview có `admin_required` và không ghi dữ liệu.
- RPC mở thật có advisory lock, idempotency, row lock và đúng 3 reward slots.
- Seed an toàn: Draft, giá 0, duplicate policy pending, no-reward tắt.
- Asset mapping đủ 18 dòng.
- `LUCKYBOX_ASSET_BASE_URL` tách riêng khỏi `SHOP_ASSET_BASE_URL`.

## Chưa chạy

- Chưa thực thi migration trên Supabase Production/Preview.
- Chưa chạy RPC với dữ liệu thật.
- Không cài được dependency từ Internet trong môi trường đóng gói; vì vậy chưa smoke-import toàn bộ Flask app. Việc này phải kiểm tra trên Vercel Preview sau khi chạy SQL.
