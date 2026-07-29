# Tối ưu hiệu năng V1.14.39.9

## Ưu tiên trải nghiệm đã thực hiện
1. Polling trạng thái chỉ tải fragment phòng, không tải lại `base.html`, sidebar, topbar, CSS và JavaScript.
2. API state tiếp tục trả 204 khi phòng không thay đổi; fragment chỉ tải khi state key đổi.
3. Giữ nguyên node `#roomLiveShell`, chỉ thay nội dung bên trong để giảm layout/repaint và tránh khởi tạo lại toàn bộ trang.
4. Polling phòng: waiting_ready 6 giây; khách playing 6 giây; chủ playing 12 giây; khách chờ xác nhận 4 giây; chủ chờ xác nhận 8 giây.
5. Chat phòng đổi 12 giây thành 18 giây; sau khi gửi tin vẫn làm mới ngay.
6. Thông báo toàn hệ thống đổi 15 giây thành 60 giây và dừng khi tab ẩn.
7. Lời mời: trang phòng 15 giây; BXH/Players 20 giây; trang khác 30 giây.
8. CSS/JS Zcoin chỉ nạp tại Ví, Điểm danh, Kho đồ, Shop và Admin Economy.
9. Xóa request 404 `rank_frames/*.png`.
10. Chuẩn hóa một URL cache cho mỗi ảnh Supabase.

## Không thay đổi
- Công thức RP, giới hạn trận ngày, phòng đấu và lịch sử.
- Không đổi SQL/Supabase schema.
- Không cần upload lại gói ảnh Supabase hiện tại.
