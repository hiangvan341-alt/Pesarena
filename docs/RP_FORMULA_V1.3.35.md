# PES Arena V1.3.35 — Công thức RP đã chốt

## Random / Random 3 chọn 1
- Giữ nguyên cơ chế thắng/thua hiện tại và cùng cấp độ RP.
- Hòa, chênh RP < 500: mỗi người random độc lập +1 đến +6 RP.
- Hòa, chênh RP >= 500: người RP thấp random +1 đến +6; người RP cao +0.
- Không có bonus chênh trình.

## Series
Mỗi người chỉ random một lần khi Series có kết quả cuối: `rp_final = rp_base + random(-2,+3)`.

| Mode | Kết quả | Base |
|---|---|---:|
| Lượt đi/về | Thắng cả 2 | +30 |
| | Thắng 1 + hòa 1 | +22 |
| | 1 thắng + 1 thua, thắng tổng | +15 |
| | 1 thắng + 1 thua, thua tổng | -10 |
| | Thua 1 + hòa 1 | -22 |
| | Thua cả 2 | -28 |
| BO3 | 2-0 | +32 / -28 |
| | 2-1 | +25 / -23 |
| Chiến thuật BO3 | 2-0 | +32 / -31 |
| | 2-1 | +25 / -23 |
| Cấm chọn BO3 | 2-0 | +32 / -31 |
| | 2-1 | +25 / -23 |

## Bỏ cuộc
- Người bỏ cuộc: -20 RP cố định.
- Người còn lại: không cộng RP do bỏ cuộc (vẫn có thể được tính trận thắng theo cơ chế lịch sử hiện tại).

## Audit Supabase
Các trường base/variance/final chỉ phục vụ audit/backend. Template người chơi không tham chiếu các trường này.
