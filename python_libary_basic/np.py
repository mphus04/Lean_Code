import numpy as np

matrix = np.array([[1 ,2, 3],[4, 5,6],[7,8,9]])
vectorize_mul_5 = matrix
mul_5 = lambda x :x * 5 
vectorize_mul_5 = np.vectorize(mul_5);
print(vectorize_mul_5(matrix));
# tính tb
print(np.mean(matrix))
# phương sai
print(np.std(matrix))
# độ lệch tiêu chuẩn
print(np.var(matrix))
