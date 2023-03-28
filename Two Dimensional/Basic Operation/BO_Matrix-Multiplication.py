import numpy as np
first=np.array([[0,1,1],[1,0,1]])
second=np.array([[1,1],[1,1],[-1,1]])

# In Numpy Matrix Multilication is very easy you can do it in just few line of code.

matrix_mul=np.dot(first,second)
print(matrix_mul)

#Ouput will be
# [[0 2]
#  [0 2]]
