import numpy as np
arr = np.array([1,2,3,4])
print(arr[0:4:2])
print(arr[1:4:2])
print(arr[::-1])
print(arr[0:4:1])
arr1 = np.array([[1,2,3,4],
                [1,12,13,14]])
print(arr1[1:2,1])
print(arr1[0:2,1])
print(arr1[:,2:4])