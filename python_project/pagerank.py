import numpy as np 
M = np.array([[0,0,1.0/2,1.0/2],
[1.0/3,0,0,0],
[1.0/3,0,0,1.0/2],
[1.0/3,1.0,1.0/2,0]])

M_khac = np.array([[0,0,1.0/2, 1.0/4],
[1.0/3,0,0,1/4],
[1.0/3,0,0,1/4],
[1.0/3,1.0,1.0/2,1/4]])

# Mũ 2 
print(np.linalg.matrix_power(M,2))

'''Xử lý dangling node trong thuật toán Pagerank'''
x = np.array([[1],[1],[1],[1]])
# lập lại 10 lần thì cho đi đến 10 
for i in range (10):
    x = np.dot(M_khac,x)
    # print(i+1,x)
    # print("--------------------------------------")
# D quan trọng nhất


'''Xử lý nhánh web reducible'''
A = np.array([[0.0, 0.0, 1/2.0, 0.0, 0.0, 0.0, 0.0, 0.0],
[1.0/3, 0.0, 1/2.0, 0.0, 0.0, 0.0, 0.0, 0.0],
[1/3.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
[1.0/3,1/2.0,1/2.0, 0.0, 0.0, 0.0, 0.0, 0.0],
[0.0 ,1/2.0, 0.0, 0.0, 0.0,1/2.0, 0.0,0.0],
[0.0, 0.0, 0.0,0.0, 0.0, 0.0, 1.0,1/2.0],
[0.0, 0.0, 0.0,1/2.0, 1.0, 0.0, 0.0, 1/2.0],
[0.0, 0.0, 0.0,0.0, 0.0,1/2.0, 0.0, 0.0]])

N = 8
X = np.array([1.0/N, 1.0/N, 1.0/N, 1.0/N, 1.0/N, 1.0/N, 1.0/N, 1.0/N])
for i in range(7):
    X = np.dot(A,X)
    # print(i+ 1 ,X)
    # print("___________________________________________________________________________")
# Ma tran phan ky 
B = np.matrix([[0,1],
              [1,0]])
# print(B.dot(B))
# print(B.dot(B.dot(B)))
# print(np.linalg.matrix_power(B,2))
# print(np.linalg.matrix_power(B,10))
# print(np.linalg.matrix_power(B,100))

