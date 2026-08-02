# V1.14.41.56

- Tách hoàn toàn trạng thái phòng và kết quả trận.
- Admin hủy phòng chỉ giải phóng người chơi; không sửa trạng thái trận, tỷ số, tranh chấp hoặc RP.
- Trận `waiting_confirm` tiếp tục chờ dù phòng đã bị hủy.
- Sau 12 giờ không xác nhận và không tranh chấp, hệ thống tự xác nhận kết quả và cộng/trừ RP.
- Bỏ phạt RP đối với người quên xác nhận kết quả.
- Chặn Admin đổi trực tiếp `disputed` sang `confirmed`; bắt buộc dùng `Xác nhận TC`.
