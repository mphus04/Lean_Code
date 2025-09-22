import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None) # cho hiển thị full hàng
pd.set_option('display.max_rows', None) # cho hiển thị full cột
cities = pd.read_csv('./data/california_cities.csv')

# Extract Latd = Vĩ độ,  Longd = Kinh độ
lat, lon = cities['latd'],cities['longd'] # truy xuất dữ liệu
population, area = cities['population_total'],cities['area_total_km2'] # truy xuất dữ liệu
plt.style.use('seaborn-v0_8') 
plt.figure(figsize=(8,6)) 
# print(lat[:10])

'''Plot using Pylot API'''
plt.scatter(lon,lat,c=np.log10(population),cmap='viridis',s=area,linewidths=0, alpha= 0.75) 
# biểu đồ tần suất phân bố (x - y - c:là màu sắc mỗi 10 ^(x) - cmap:là định dạng màu- s là độ lớn của điểm đó ở đây cho bằng độ lớn của area  # )
# log10(population): là 10 ^ (x , y) phải sài vì giá trị quá lớn
plt.axis('equal')
plt.xlabel('longlatitude')
plt.ylabel('lattitude')
plt.colorbar(label='log$(10)$(population)') 
plt.clim(3,7) # giới hạn cột màu chú thích
area_range = [ 50, 100, 300, 500, 1000,1200] # tạo một mảng cho diện tích là các phần tử trong mảng để chú thích cho điểm trong biểu đồ
for area in area_range:
    plt.scatter([], [], s=area ,c='k',alpha=0.5 , label=str(area) + 'km$^2$')
# cho thêm một đồ thị mới nhưg mà bỏ trống giá trị x và y
# với mỗi giá trị trong mảng area_range=giá trị của điểm trong biểu đồ
# đổi kiểu dữ liệu trong biến area thành str để làm thành chú thích dạng số + km vuông
plt.legend(labelspacing=1,title="City Area") # dòng này để hiện chú thích ra
plt.title('California Cities : Population and Area Distribution')
plt.show()