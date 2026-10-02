import numpy as np
matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Original matrix:\n",matrix)
print("Sub-matrix:\n",matrix[0:2,0:2])
arr=np.array([5,12,8,20,3,17,25])
print("\nElements greater than 10 :",arr[arr>10])
print("\nDimensions:",matrix.ndim)
print("Shape:",matrix.shape)
print("Data type:",matrix.dtype)
