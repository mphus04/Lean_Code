'''thuật toán sắp xếp'''

'''BUBBLE Sort: sắp xếp bong bóng'''
list = [1,3,5,4,9,7,6]
def BubbleSort(list):
    for i in range (len(list)-1):
        for j in range (1,len(list) - i): # trừ i để bỏ đi phần tử cuối cùng đã cho là lớn nhất nên ko cần xét nữa
            if list[j-1] > list[j]:
                list[j-1],list[j]=list[j],list[j-1] 
                print(list)
    return list 
# print(BubbleSort(list))
#output:[1, 3, 4, 5, 6, 7, 9]
# def InsertionSort(list):
#     i = 0
#     for j in range (1,len(list)):
#         while list[i] < list[j] :
#             i = i +1
#         m = list[j]
#         for k in range (j-i):
#             list[j-k] = list[j-k-1]
#         list[i] = m
#     return list
def InsertionSort(list):
    for j in range(1, len(list)):
        key = list[j]
        i = j - 1
        while i >= 0 and list[i] > key:
            list[i + 1] = list[i]
            i = i - 1
        list[i + 1] = key
    return list
print(InsertionSort(list))