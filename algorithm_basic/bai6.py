'''TÌm số lượng tối đa phần tử cho ra trong 1 chuỗi biết trước tagret '''
list = [1,4,12,13,5,6,7,8,2,10,11]
target= int(input("hãy nhập target mà bạn muốn :"))
def MaxcountElement(list,target):
    sort_list = sorted(list)
    print(sort_list)
    for i in range(len(sort_list)-1):
        sum_list = sum(sort_list[0:i])
        while sum_list >= target :
            return f'với target = {target} thì số lượng tối đa phần tử cần dùng là {i - 1}'

print(MaxcountElement(list,target))
