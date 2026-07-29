# Collap V1.14.39.12

- Nền phát triển: Collap_V1.14.39.11, vốn quay lại từ V1.14.39.8.
- Đổi chống lặp đội thành lịch sử theo từng cặp đối thủ.
- Mỗi người bị loại các CLB chính mình đã dùng trong đúng 5 trận confirmed gần nhất với đối thủ hiện tại.
- Khi đổi sang đối thủ khác, lịch sử của cặp cũ không còn áp dụng.
- Rank thường và Random 3 chọn 1 dùng chung một lịch sử 5 trận.
- Vẫn bảo đảm hai bên trong cùng lượt random không nhận trùng CLB.
- Chuẩn hóa tên CLB bằng strip/casefold để tránh trùng do chữ hoa hoặc khoảng trắng.
- Không cần chạy SQL.

# Collap V1.14.39.11

- Nền: Collap V1.14.39.10.
- Rank thường: mỗi người không được nhận lại CLB đã sử dụng trong đúng 5 trận Rank thường đã xác nhận gần nhất.
- Bỏ cơ chế nới lịch sử cấm xuống 1 hoặc 0 trận; bảo đảm 5 CLB gần nhất luôn bị loại.
- Random 3 chọn 1: giữ nguyên cơ chế đội đã chọn không xuất hiện ở lượt sau.
- Không thay đổi SQL hoặc cấu trúc Supabase.

# Collap V1.14.39.7

- Thay đổi Giới hạn thi đấu Rank mỗi ngày: không còn chặn tạo phòng, mời đấu, vào phòng, Sẵn sàng hoặc Đá tiếp.
- Trận thứ 11 trở đi trong ngày thường và trận thứ 16 trở đi vào cuối tuần vẫn được chơi và lưu lịch sử.
- Trận vượt giới hạn nhận 0 RP cho cả hai, không tác động chuỗi thắng/thua và không phát danh hiệu.
- Ghi rõ lý do không tính RP trong `matches.note` và `rp_details.daily_rank_limits`.
# Collap V1.14.39.10

- Quay lại hoàn toàn nền mã nguồn `Collap_V1.14.39.8`; không sử dụng các thay đổi giao diện/polling của V1.14.39.9.
- Rank thường: mỗi người không được nhận lại CLB đã dùng trong đúng 3 trận Rank thường đã xác nhận gần nhất.
- Random 3 chọn 1: CLB người chơi thực sự đã chọn trong các trận đã xác nhận sẽ không xuất hiện trong các lượt Random 3 chọn 1 tiếp theo của chính người đó.
- Các CLB chỉ xuất hiện trong 3 lựa chọn nhưng không được chọn vẫn có thể xuất hiện lại.
- Trong cùng một lượt Random 3 chọn 1, 6 lựa chọn của hai bên vẫn không trùng nhau.
- Không cần chạy SQL.
