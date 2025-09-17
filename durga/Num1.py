import numpy as np
a=np.array([10,20,30])
b=np.array([1,2,3])
def product(a,b):
    result=0
    for i,j in zip(a,b):
        result=result+i*j
        print(result)
product(a,b)