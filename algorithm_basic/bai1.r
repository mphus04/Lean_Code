# Cài đặt gói "incidence2" nếu chưa cài
if (!require(incidence2)) {
  install.packages("incidence2")
}

# Tải gói "incidence2"
library(incidence2)

# Tạo khung dữ liệu với cột "date_onset" chứa các ngày
df <- data.frame(date_onset = as.Date(c("2023-11-01", "2023-11-02", "2023-11-03", "2023-11-04", "2023-11-05", "2023-11-06", "2023-11-07", "2023-11-08", "2023-11-09", "2023-11-10", "2023-11-11", "2023-11-12", "2023-11-13", "2023-11-14", "2023-11-15")))

# Tạo đối tượng xảy ra, tổng hợp các trường hợp theo ngày
epi_day <- incidence(
  x = df,
  date_index = "date_onset",
  interval = "day"
)

# In ra tóm tắt về đối tượng incidence object
print(summary(epi_day))

# Vẽ biểu đồ incidence object
plot(epi_day, main = "Biểu đồ incidence object", xlab = "Ngày", ylab = "Số ca nhiễm")