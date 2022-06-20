import numpy as np
a= np.arange(1, 10)
print('initialised array')
print(a)
print('re-dimensioning array')
print(a.dtype)
print(np.reshape(a, (9,1), order='C'))
# change the dtype to 'float64'
arr = a.astype('float64')
print(arr)
print(arr.dtype)