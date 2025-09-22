'''
tính số ước của một số 
input = 6
output = 4
'''
from math import  *
def Estimate(n):
    numb_elm  = 0
    for i in range (1 , isqrt(n)+ 1):
        if n%i==0 :
            numb_elm +=1 # lấy nghiệm là i (6%1 lấy 1 ,6%2 lấy 2 )
            if i!= n//i: # dấu chia lấy phần nguyên
                numb_elm +=1 # lấy nghiệm là n//i tức là (6//1 = 6 và 6//2 = 3)
    return numb_elm
def main():
    Estimate(n)
if __name__ == "__main__":
    n = int(input("Please enter number you want calculate estimate : "))
    print(f'number estimate of {n} is {sum(n)}')
    