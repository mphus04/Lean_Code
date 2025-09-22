''' Largest Sum Subarray'''
def Sum_Subarray(list_sum):
    max_list = 0
    max_far = 0
    for x in list_sum:
        max_list = max(0,max_list + x)
        max_far = max(max_list,max_far)
    return max_far
list_sum = [4,-2,-5,1,2,3,6,-5,1]
print(Sum_Subarray(list_sum))