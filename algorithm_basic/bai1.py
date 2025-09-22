'''
tìm 1 số có phải số chính phương hay không
input = 16
output = True
'''
from math import * 
def CheckSquare(n):
    can = isqrt(n) # iqrt is can bac 2 cua n
    if can * can == n :
        return True
    else:
        return False
    
if __name__ =="__main__":
    n= int(input("Please enter number you want check  : "))
    if CheckSquare(n):
        print(f'{n} is  square number ')
    else:
        print(F'{n} is not square number ' )
    
    