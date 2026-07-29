# Quy tắc Random V1.14.39.12

## Lịch sử theo cặp đối thủ

Với mỗi cặp người chơi A–B, hệ thống đọc đúng 5 trận `confirmed` gần nhất giữa A và B.
Lịch sử này dùng chung cho Rank thường và Random 3 chọn 1.

- Đội A đã dùng trong 5 trận A–B bị loại khỏi lượt random tiếp theo của A khi gặp B.
- Đội B đã dùng trong 5 trận A–B bị loại khỏi lượt random tiếp theo của B khi gặp A.
- Khi A chuyển sang gặp C, lịch sử A–B không được áp dụng; hệ thống dùng lịch sử riêng A–C.
- Trong Random 3 chọn 1, sáu lựa chọn của hai bên trong cùng lượt vẫn khác nhau.
- Không cần SQL hoặc bảng mới.
