'''thuật toán tìm kiếm'''
list = [1,3,4,6,8,9,10,12,13,14]
def TimKiem_TT(x,list):
    for i in range (len(list)):
        while i<=x and x!= list[i]:
            i = i + 1
        if i <= x :
            location = i+1
        else :
            location =  0
        return location
# print(TimKiem_TT(12,list))  
#OUTPUT = 9 

list1 = [1,2,3,4,5,6,7,8,9,10]
def TimKiem_NP1(x, list):
    i = 0  # Chỉ số bắt đầu từ 0
    j = len(list) - 1  # Chỉ số cuối cùng của mảng
    while i <= j:  # Sửa điều kiện lặp để bao gồm cả khi i == j
        m = (i + j) // 2  # Sử dụng phép chia nguyên để làm tròn xuống
        if x > list[m]:
            i = m + 1
        else:
            j = m - 1  # Giảm j xuống để tránh lặp vô hạn
    if i < len(list) and x == list[i]:  # Kiểm tra x có tồn tại trong mảng không
        location = i + 1
    else:
        location = 0  # Trả về -1 nếu không tìm thấy để tuân theo quy ước thông thường
    return location

print(TimKiem_NP1(10,list1))
#output 8
