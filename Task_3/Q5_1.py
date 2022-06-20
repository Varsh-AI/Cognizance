import numpy as np
a = np.random.randint(6 ,size = (2,3))
print("a =\n",a)
b = np.random.randint(6 ,size = (3,5))
print("b =\n",b)
c = np.dot(a,b)
print("c =\n",c)