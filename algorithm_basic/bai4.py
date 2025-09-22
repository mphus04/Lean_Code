'''
Kiểm tra có phải là  số nguyên tố không
'''
from math import *
# def IsPrime(n):
#     if n < 2 :
#         print(" N must > 2 ")
#     else :
#         for i in range(2, isqrt(n)+1):
#             if n%i==0 and (i!=1,i!=0):
#                 return False 
#         return True
# if __name__ == "__main__":
#     n = int(input("Please enter number you want define :"))
#     if IsPrime(n):
#         print(f'{n} is Prime')
#     else:
#         print(f'{n} is not Prime')
        
'''
Tìm số nguyên tố trong khoảng N
'''
def isPrime(N):
    for i in [x+1 for x in range (N)]:
        if N % i == 0 and (i!=1 and i!=N):
            return False
    return True

S_prime = [isPrime(x) for x in range (1,40)]
# in ra type bool 

S = [x for x in range(40)
         if (isPrime(x)==True and x>0)]
# in ra interger
print((S_prime))