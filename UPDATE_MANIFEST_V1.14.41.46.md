# V1.14.41.46 · Lucky Box Rate Visibility Hotfix

## Thay đổi
1. Tăng `APP_VERSION` lên `V1.14.41.46`.
2. Gỡ hoàn toàn khối tỷ lệ khỏi giao diện người chơi.
3. Gỡ dòng “Tỷ lệ trong nhóm” khỏi từng thẻ phần thưởng.
4. Admin xem UI người chơi cũng không thấy tỷ lệ, đúng như trải nghiệm member.
5. Tỷ lệ vẫn được quản lý tại Admin Lucky Box và mô phỏng Draft riêng.

## Triển khai
- Không cần SQL.
- Dán patch, commit, push và kiểm tra Vercel Preview.
- Chưa merge `main` trước khi hoàn tất kiểm thử.
