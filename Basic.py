import numpy as np
a=np.arange(9).reshape(3,3)
print("Matrix A is")
print(a)
lst=[5,5,6,7,3,5,7,2,8]
b=np.array(lst).reshape(3,3)
print("Matrix B is")
print(b)
c=a+b
print(c)
d=a-b
print(d)

e=a*b  
print(e)

f=a*1/b 
print(f)

