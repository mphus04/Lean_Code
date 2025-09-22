'''
Tổng của ước số 
input : 6
output : 12 
'''
from math import *
def Desimate(n):
    Desimate_set = []
    for i in range (1 ,isqrt(n)+1):
        if n%i == 0:
            Desimate_set.append(i)
            if i!= n//i:
                Desimate_set.append(n//i)
    return Desimate_set
def Sum_Des(Destimate_set):
    Sum = sum(Desimate_set)
    print(Sum)   
if __name__ == "__main__":
    n = int(input("please enter number you want sum of destimate : "))
    Desimate_set = Desimate(n)
    print(Desimate_set)
    Sum_Des(Desimate_set)
    
