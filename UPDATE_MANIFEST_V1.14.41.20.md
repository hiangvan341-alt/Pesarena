# UPDATE MANIFEST V1.14.41.20

- Sửa logo Parsec bị hiển thị thiếu do bị ép vào khung vuông 18x18 px.
- Đổi khung logo thành 20x30 px đúng tỷ lệ biểu tượng dọc của Parsec.
- Giữ `object-fit: contain`, cho phép overflow hiển thị đầy đủ.
- Đổi logo sang tải ưu tiên (`loading=eager`) để tránh hiện chậm trong tiêu đề module.
- Không thay đổi logic phòng, API, database hoặc tài nguyên Supabase.

## File thay đổi
- `static/css/parsec_room.css`
- `templates/partials/parsec_room_panel.html`
- `app.py` (nếu có chuỗi phiên bản)
