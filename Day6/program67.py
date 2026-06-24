import numpy as np
arr1=np.array([[1,3,5,7],
              [1,2,3,4]])
arr2=np.array([[2,4],
               [6,8],
              [4,3],
              [2,1]])
row=len(arr1)
col_a=len(arr1[0])
col=len(arr2[0])
res=[[0 for _ in range(col)]for _ in range(row)]
for i in range(row):
    for j in range(col):
        for k in range(col_a):
            res[i][j]+=arr1[i][k]*arr2[k][j]
print(np.array(res))