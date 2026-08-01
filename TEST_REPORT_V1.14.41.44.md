# TEST REPORT · V1.14.41.44

## Kết quả
- Pytest: 69 passed, 0 failed.
- Python AST/compile: đạt.
- JavaScript `node --check`: đạt.
- Jinja: 48 template tải hợp lệ.

## Phạm vi xác minh
- Route Lucky Box người chơi, lịch sử và chi tiết.
- Admin Preview UI không gọi RPC mở hộp thật.
- Mở thật vẫn dùng `open_lucky_box` và request UUID chống trùng.
- Giá, tỷ lệ 0–3 vật phẩm, reward pool và lịch sử hiển thị trên UI.
- Tích hợp Cửa hàng và menu tài khoản.
- Không có migration SQL mới.

## Chưa xác minh trong container
- Không import/chạy Flask runtime vì môi trường kiểm thử không cài package Flask.
- Cần xác minh trực tiếp trên Vercel Preview trước khi merge hoặc promote.
