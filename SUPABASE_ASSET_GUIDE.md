# Hướng dẫn tài nguyên tĩnh Supabase — V1.14.39.8

## Nên đưa lên Supabase Storage

Upload toàn bộ nội dung của gói `Supabase_Assets_V1.14.39.8.zip` vào một thư mục public, ví dụ:

```text
Bucket: pes-assets
Thư mục: v1/
```

Sau khi upload, cấu hình Vercel Environment Variable:

```text
STATIC_ASSET_BASE_URL=https://<project>.supabase.co/storage/v1/object/public/pes-assets/v1
```

Không thêm dấu `/` ở cuối. Nếu chưa cấu hình biến này, website tự dùng bản WebP nằm trong `/static`, nên không bị mất ảnh.

## Giữ trong Vercel/GitHub

- `static/style.css`
- `static/css/*.css`
- `static/js/*.js`
- `static/*.svg`

Các file này nhỏ, thay đổi theo phiên bản code và đang có cache dài bằng `APP_VERSION`, nên giữ cùng deployment sẽ an toàn hơn.

## Định dạng đã dùng

- Ảnh nền, logo, biểu tượng Rank, thẻ Rank và ảnh VS: WebP.
- QR Zalo: PNG để ưu tiên khả năng quét.
- SVG cúp: giữ SVG vì rất nhẹ và sắc nét.

## Cache đề xuất cho bucket

```text
Cache-Control: public, max-age=31536000, immutable
```

Khi thay ảnh, nên upload vào thư mục phiên bản mới như `v2/`, sau đó đổi `STATIC_ASSET_BASE_URL`, thay vì ghi đè file cũ.
