# UPDATE MANIFEST V1.14.41.12

## Lỗi đã sửa
Logo Parsec bị hiển thị rất lớn dù file ảnh đã tải lên Supabase.

## Nguyên nhân
Không phải do kích thước file ảnh. CSS `parsec_room.css` cũng đang được tải qua `asset_url()`. Khi `STATIC_ASSET_BASE_URL` trỏ tới Supabase, website có thể nhận file CSS cũ chưa có giới hạn 22 px. Do đó ảnh dùng kích thước gốc 358×558 px hoặc bị quy tắc khác kéo giãn.

## Cách sửa
1. Tải `parsec_room.css` từ static của chính bản deploy.
2. Khóa logo ở 18×18 px trong CSS module.
3. Thêm thuộc tính width/height và inline `!important` trong HTML.
4. Thêm quy tắc dự phòng ở cuối `style.css`.
