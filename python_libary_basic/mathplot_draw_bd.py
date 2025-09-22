''' Thư viện mathplotlib '''
import matplotlib.pyplot  as plt
import numpy as np
'''example 1 '''
# print(plt.style.available) # kiểu dữ liệu để thay đổi
# plt.style.use('seaborn-v0_8-darkgrid') # sử dụng kiểu dữ liệu
# plt.show()
# '''biểu đồ xiên'''
# x = [ 2 , 4 , 5, 6 ,7] 
# y = [ 4 ,  7, 8, 9, 0]
# plt.plot(x, y) # vex biểu đồ xiên
# plt.plot(x, color="red" , linestyle = 'dashed')
# plt.show() # show biểu đồ 


# # # Plot API  vs Object - Oriented (OO) API

'''vẽ biểu đồ dángj sin cos bằng thư viện numpy'''
# z = np.linspace(0, 10, 1000)
# plt.plot(z , np.sin(z), color="pink", linestyle = "dashed",label="SinX")
# plt.plot(z , np.cos(z), color="black" ,label="CosX")
# plt.xlabel("bien X") # đăt tên trục x
# plt.ylabel("sinX")
# plt.title("do thi sinx and cosx ") # đặt tên cho biểu đồ
# # plt.axis([0, 4 ,-0.7 , 0.6]) gioi han nhu lim
# plt.axis("equal") 
# plt.legend() # chú thích cho biểu đồ 
# plt.show()
# plt.xlim([0.4]) giới hạn x
# plt.ylim([-0.7, 0.6]) giới hạn y 


'''Object - Oriented (OO) API'''
# 1. chuẩn bị data
# x=[1,2,3,4]
# y=[5,6,8,9]
#2 . Set up plot
# fig, ax= plt.subplots(figsize=(5, 5)) ## Figure size = Width & Height of the plot
## fig là hình tổng
## ax là hình nhỏ
# ax.plot(x, y)
# ax.set(title="do thi cua x va y",
#        xlabel="truc x ", ylabel="truc y")
#plt.show()

'''ve bieu do mu 3 '''
x = np.linspace( 0 , 10 , 2000) ##khoang cach 
x[:5]
# fig, ax = plt.subplots()
# ax.plot(x, x**3) 
# plt.show()


'''Most common types of Mathplotlib plots'''

"""Scatter : biểu đồ phân tán"""
# plt.scatter(x, np.exp(x)) ## y = e^(x)
# plt.show()

"""OO API"""
# rng= np.random.RandomState(0)
# x = rng.randn(100)
# y = rng.randn(100)
# colors = 100*rng.rand(100) ## số lượng màu sắc 
# sizes = 500*rng.rand(100) ## kích thước mỗi điểm 
# fig , ax = plt.subplots()
# img1=ax.scatter(x,y, s=sizes, c=colors ,cmap='viridis', alpha=0.7)
# ## biểu đồ phân tán-kích thước random- màu random - phối màu -độ mờ 
# fig.colorbar(img1) ## cột màu sắc 
# plt.show()

"""BIỂU ĐỒ CỘT(BAR CHART)"""
# *vertical chart
# *horizon

### prepare data from a python dictionary
soft_drink_prices = {"Coke": 10 , "pessi":12, "siting": 8}
# fig , ax = plt.subplots()
# ax.bar(soft_drink_prices.keys(), soft_drink_prices.values())
# ## ax.barh(list(soft_drink_prices.keys()),list(soft_drink_prices.values())) ### đảo ngược biểu đồ
# ax.set(title="tap hoa")
# plt.show()

"""HISTOGRAM :biểu đồ tần suất dạng côt"""
# ## prepare data
student_height = np.random.normal(170, 10 , 250) ## chiều cao tb là 170-độ lệch chuẩn là 10-tổng là 250
# print(student_height[:10]) ## in ra 10 phần tử đầu tiên 
# plt.hist(student_height, bins=30) ## biểu đồ tần suất - chia nhỏ khoảng ra   
# plt.show()

"""SUBPLOTS"""
## OPTION 1
fig, ((ax1,ax2), (ax3,ax4)) = plt.subplots(nrows=2,ncols=2,figsize=(10, 5))
ax1.plot(x, x/2) ## vẽ biểu đồ cho axes 1 
ax1.plot(x, x*2)
####ax[0,0].plot(x, x/2) # cách chon 2 như truy xuất trong mảng

ax2.scatter(np.random.random(10),np.random.random(10)) ## vẽ biểu đồ cho axes 2 
##ax[0,1].plot(x, x/2) # cách chon 2 như truy xuất trong mảng

ax3.bar(soft_drink_prices.keys(),soft_drink_prices.values()) ## vẽ biểu đồ cho axes 3 
##ax[1,0].plot(x, x/2) # cách chon 2 như truy xuất trong mảng

ax4.hist(student_height, bins=30) ## # vẽ biểu đồ cho axes 4
##ax[1,1].plot(x, x/2) # cách chon 2 như truy xuất trong mảng

plt.show()
