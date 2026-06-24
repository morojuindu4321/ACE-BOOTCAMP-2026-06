import numpy as np
print(np.__version__)
arr1=np.array([[[1,2,3,4],[5,6,7,8],[5,6,7,8]],
               [[1,2,3,4],[5,6,7,8],[5,6,7,8]],
               [[1,2,3,4],[5,6,7,8],[5,6,7,8]]])
print(arr1)
print(arr1.ndim)
print(arr1.shape)
print(arr1[2,0,1])
print(arr1[2,1,3])
print(arr1[1][1][1])