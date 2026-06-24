import numpy as np
arr=np.array([[1,2],[3,4]])
arr.flags.writeable=False
arr[0]=0
print(np.array(arr))