import numpy as np
a=np.array([10,20,30])
b=np.array([1,2,3])
c=np.array([4,5,6])
#def product(a,b,c):
result=0

for i,j,k in zip(a,b,c):

    result=result+i*j*k
    print(result)
#product(a,b,c)