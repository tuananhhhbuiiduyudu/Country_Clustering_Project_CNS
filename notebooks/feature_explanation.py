# Giải thích các cột dữ liệu trong bộ dữ liệu Country_data.csb
# Thường dùng trong các bài toán học máy không giám sát 


# | **Tên cột**  | **Ý nghĩa**                                                                                                                   |
# | ------------ | ----------------------------------------------------------------------------------------------------------------------------- |
# | `country`    | **Tên quốc gia**                                                                                                              |
# | `child_mort` | **Tỷ lệ tử vong trẻ em** (dưới 5 tuổi trên 1000 trẻ sinh ra) — phản ánh điều kiện y tế và phát triển xã hội.                  |
# | `exports`    | **Tỷ lệ xuất khẩu** so với GDP (theo phần trăm) — ví dụ: 0.25 nghĩa là xuất khẩu chiếm 25% GDP.                               |
# | `health`     | **Chi tiêu cho y tế** trên GDP (theo phần trăm) — ví dụ: 0.05 nghĩa là 5% GDP dành cho y tế.                                  |
# | `imports`    | **Tỷ lệ nhập khẩu** so với GDP (theo phần trăm) — ví dụ: 0.30 nghĩa là nhập khẩu chiếm 30% GDP.                               |
# | `income`     | **Thu nhập bình quân đầu người** (GDP per capita, tính theo USD) — thể hiện mức sống.                                         |
# | `inflation`  | **Tỷ lệ lạm phát hàng năm** (theo phần trăm) — thể hiện sự ổn định kinh tế, giá cả tiêu dùng.                                 |
# | `life_expec` | **Tuổi thọ trung bình** — số năm trung bình một người sống ở quốc gia đó.                                                     |
# | `total_fer`  | **Tỷ lệ sinh sản** (fertility rate) — trung bình số con của một phụ nữ trong đời.                                             |
# | `gdpp`       | **GDP bình quân đầu người** (giá trị GDP per capita theo USD) — giống `income`, nhưng có thể khác về cách tính hoặc cập nhật. |

from src import config
print(config.SET_PATH_DATA)