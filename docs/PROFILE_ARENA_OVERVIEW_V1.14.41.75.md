# Profile Arena Overview · V1.14.41.75

## Mục tiêu

Đưa phần nhận diện đầu trang về bố cục hồ sơ game-client rõ ràng hơn, lấy cảm hứng từ cách tổ chức thông tin của các game MOBA nhưng vẫn sử dụng ngôn ngữ hình ảnh riêng của PES Arena.

## Thay đổi

- Avatar và tên người chơi được đặt trực tiếp trên vùng banner thay vì nằm trong một thanh thông tin tách rời.
- Cụm nhận diện bên trái gồm avatar, tên, huy hiệu, trạng thái, username, RP và rank.
- Dải trưng bày phía dưới gồm danh hiệu nổi bật, ba nút showcase dạng huy hiệu tròn và crest rank ở bên phải.
- Các nút quản lý, cửa hàng, mời đấu và chia sẻ được thu gọn thành cụm điều khiển nổi.
- Banner tiếp tục dùng `object-fit: contain`, không cắt mặt hoặc chi tiết quan trọng.
- Toàn bộ CSS mới vẫn nằm dưới `.profile-v2-page`, không tác động Shop, Lucky Box, Phòng đấu, BXH hoặc Admin.

## Dữ liệu

Không thêm bảng SQL, không thay đổi API, route hoặc logic tính điểm. Giao diện chỉ sử dụng dữ liệu profile hiện có.
