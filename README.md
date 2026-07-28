# Collap_V1.14.33_ZCOIN_PHASE1_COMPAT

Bản sửa tương thích database hiện có cho nền tảng Zcoin giai đoạn 1 của PES Arena / RankZone FC.

## Có gì mới

- Hiển thị số dư Zcoin trên thanh trên cùng.
- Trang Ví Zcoin và lịch sử giao dịch.
- Tab quản trị Zcoin.
- Admin có quyền được cộng/trừ Zcoin kèm lý do.
- Chống số dư âm, chống gửi lặp và ghi giao dịch nguyên tử.
- Dùng trực tiếp schema `zcoin_transactions` đã tồn tại.
- Các dữ liệu audit bổ sung được lưu trong `metadata`, không thêm cột mới.

## SQL tối thiểu

Có. Chạy file:

`docs/update_zcoin_phase1_compat_v1_14_33.sql`

File SQL này:

- Không tạo lại bảng.
- Không xóa dữ liệu.
- Không đổi cấu trúc bảng.
- Chỉ tạo index an toàn và RPC `adjust_zcoin_balance`.

## Chưa có trong giai đoạn này

- Điểm danh ngày.
- Gift Code.
- Cửa hàng và kho đồ.
- Hiệu ứng pháo hoa.

Không upload `.env`, `__pycache__`, `.pyc` hoặc `.pytest_cache` lên GitHub.
