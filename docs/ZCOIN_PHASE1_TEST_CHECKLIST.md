# Kiểm thử Collap_V1.14.35_ZCOIN_PHASE1_CLEAN

## SQL

- Database đã chạy SQL tương thích của V1.14.33: **không cần chạy lại SQL**.
- Database mới chưa có RPC `adjust_zcoin_balance`: chạy `docs/update_zcoin_phase1_compat_v1_14_35.sql` một lần.
- SQL không tạo lại bảng, không xóa dữ liệu và không reset số dư.

## Kiểm thử sau deploy

1. Đăng nhập tài khoản player, kiểm tra logo và số dư Zcoin trên topbar.
2. Mở menu tài khoản → **Ví & lịch sử Zcoin**.
3. Trang Ví chỉ hiển thị logo, số dư và lịch sử giao dịch; không còn khung “Giai đoạn 1”.
4. Đăng nhập Owner, mở Admin → Zcoin.
5. Cộng thử 1.000 Zcoin cho tài khoản test với lý do rõ ràng.
6. Kiểm tra số dư topbar và lịch sử ví của tài khoản test.
7. Trừ thử 300 Zcoin; số dư và lịch sử phải cập nhật đúng.
8. Thử trừ vượt số dư; hệ thống phải từ chối.
9. Không kiểm thử bằng tài khoản thật trước khi tài khoản test hoạt động ổn định.
