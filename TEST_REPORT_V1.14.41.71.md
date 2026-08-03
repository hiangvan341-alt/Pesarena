# TEST REPORT — V1.14.41.71

- Python compile: thành công.
- Pytest: 107 passed / 0 failed.
- Banner foreground vẫn dùng `object-fit: contain`, không crop artwork.
- Xóa nền tối trực tiếp của ảnh banner để nền blur phía sau có thể lấp hai bên.
- Tăng độ phủ, saturation và blur của backdrop để các banner 4:1 hòa vào khung compact tự nhiên hơn.
- Banner mặc định khi chưa trang bị vẫn giữ nguyên.
- Không có migration hoặc thay đổi database.
