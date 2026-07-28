# Kiểm thử Collap_V1.14.33_ZCOIN_PHASE1_COMPAT

1. Chạy `docs/update_zcoin_phase1_compat_v1_14_33.sql` và nhận `Success. No rows returned`.
2. Upload source lên GitHub, không upload `.env` và `__pycache__`.
3. Chờ Vercel báo Ready + Production, sau đó Ctrl + F5.
4. Đăng nhập Owner, mở Admin → Zcoin.
5. Cộng thử 1.000 Zcoin cho một tài khoản test, nhập lý do rõ ràng.
6. Kiểm tra số dư ở topbar và trang Ví Zcoin của tài khoản test.
7. Trừ thử 300 Zcoin, kiểm tra số dư còn 700 và có đủ hai giao dịch.
8. Thử trừ 1.000 Zcoin khi chỉ còn 700; hệ thống phải từ chối.
9. Không thử trực tiếp trên tài khoản thật trước khi hoàn tất tài khoản test.
