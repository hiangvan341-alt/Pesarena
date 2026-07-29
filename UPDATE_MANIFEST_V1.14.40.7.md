# Collap_V1.14.40.7 — Global Avatar Frames

## Mục tiêu
Hiển thị Khung Avatar đang trang bị ở toàn bộ vị trí có Avatar người dùng, không chỉ menu tài khoản góc trên.

## Phạm vi
- Players / Cộng đồng Player.
- BXH, Dashboard và danh sách người chơi trực tuyến.
- Phòng đấu: chủ phòng, khách, giao diện polling động.
- Danh sách phòng.
- Lời mời thi đấu và banner lời mời.
- Lịch sử trận đấu và lịch sử trong Hồ sơ.
- Chat sảnh, chat dưới cùng và chat phòng.
- Giữ nguyên khung ở Hồ sơ và menu tài khoản.

## Kỹ thuật
- Đọc khung Avatar theo lô với tối đa 2 truy vấn Supabase thay vì N+1.
- Cache bản đồ khung 15 giây; tự xóa cache khi trang bị/gỡ khung.
- Macro Avatar tự nhận `player.avatar_frame` hoặc tham số `frame`.
- Giữ kích thước Avatar gốc trong bảng; chỉ Avatar topbar dùng kích thước mở rộng.

## Không thay đổi
- Không sửa database.
- Không cần chạy SQL.
- Không thay đổi logic mua hàng, Kho đồ hoặc Zcoin.

## Kiểm tra
- Python compile: PASS.
- Jinja parse: 40/40 PASS.
- Shop Phase 3 static verification: PASS.
- Runtime import không chạy trong môi trường build vì môi trường không cài Flask; cần xác nhận bằng Vercel Preview.
