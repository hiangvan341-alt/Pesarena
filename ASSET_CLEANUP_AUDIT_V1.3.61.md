# PES Arena V1.3.61 — Supabase Asset Cleanup

## Mục tiêu
Làm gọn runtime project, không giữ binary image đã có trên Supabase.

## Kết quả
- Trước cleanup: **16 ảnh local**, 685,812 bytes.
- Sau cleanup: **0 ảnh local** trong ZIP runtime.
- Xóa **21 file staging/local**, tổng 692,684 bytes.
- Xóa toàn bộ `UPLOAD_SUPABASE/`.
- Xóa `static/assets/room_v2/`.
- Giữ `SUPABASE_ASSET_MANIFEST.csv` vì chỉ là manifest text nhỏ.

## Bộ Room asset dùng trực tiếp Supabase
Base URL:
`https://wlnvdfghatgeygecwrqb.supabase.co/storage/v1/object/public/pes-assets/room-assets/v1.3.18`

8 file:
- room-texture-dark.webp
- center-stadium.webp
- pes-arena-room-logo.webp
- parsec-logo.webp
- vs-gold-emblem.webp
- stadium-red.webp
- share-link.webp
- stadium-blue.webp

Các file này đã có record upload trong `DANH_SACH_UPLOAD_CHI_TIET.csv` của bản trước và hai bộ local có SHA-256 trùng nhau.

## Cleanup code
- `room_asset_url()` remote-only.
- Parsec logo chuyển sang `room_asset()`.
- CSS Room fallback chuyển sang Supabase URL.
- Xóa fallback legacy `room-texture-blue.webp` không tồn tại, dùng `room-texture-dark.webp`.
- 6 mode logos tiếp tục dùng Supabase `room-assets/v1.3.40/modes`.

## Ảnh mới cần upload
**Không có.** V1.3.60 không còn ảnh binary nào ngoài 8 Room asset đã upload và bản sao staging của chính chúng.
