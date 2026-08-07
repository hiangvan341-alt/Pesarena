# Báo cáo quét hiệu năng Admin — V1.3.33

## Điểm nghẽn nghiêm trọng

1. **N+1 cleanup khi mở Admin**
   - Mỗi tài khoản xuất hiện trong phòng tạo thêm một truy vấn đọc phòng trực tiếp, sau đó có thể tiếp tục xóa/update.
   - Đây là nguyên nhân khiến chỉ một thao tác click tab có thể kéo dài hàng chục giây.

2. **Báo cáo dùng `list_matches()`**
   - Tải toàn bộ trận và toàn bộ cột.
   - Enrich tên/avatar cho từng trận.
   - Chạy auto-confirm từng bản ghi.
   - Không phù hợp với tác vụ chỉ cần đếm theo ngày.

3. **User × Mode database calls**
   - Với 100 user và 6 mode có thể phát sinh hàng trăm đến hơn 1.000 truy vấn phụ tùy cache/request context.

4. **Trang Tổng quan tải dữ liệu quá mức**
   - Tải full phòng và full trận chỉ để lấy số lượng trạng thái.

5. **Hủy phòng thiếu error boundary**
   - Update phòng/lời mời gọi `.execute()` trực tiếp.
   - Một lỗi mạng, timeout hoặc schema phụ trả thẳng HTTP 500.

## Kiến trúc sau sửa

- Mở tab chỉ đọc dữ liệu của tab đó.
- Báo cáo lọc ngày tại database.
- Không chạy cleanup trong GET `/admin`.
- Config và unlock được batch một lần.
- Hủy phòng có retry, catch lỗi và thông báo thân thiện.
- Vercel Logs có dòng `ADMIN_PERF` để đo thời gian thật sau deploy.

## Cách kiểm tra sau khi deploy

1. Mở lần lượt Tổng quan, Phòng, Trận đấu, Báo cáo.
2. Trong Vercel Logs tìm `ADMIN_PERF`.
3. Kiểm tra `duration_ms`; mục tiêu thông thường dưới 2–5 giây tùy cold start và Supabase.
4. Bấm từng khoảng Báo cáo; số `report_matches` phải thay đổi theo khoảng ngày.
5. Hủy một phòng; endpoint phải redirect về tab Phòng và hiện toast, không còn trang Internal Server Error.
