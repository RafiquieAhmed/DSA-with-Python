'''
import numpy
numpy.arrray()

//2nd method
import numpy as np
np.array()
'''

#Best version no need of metion type code 
from numpy import *


val =array([1,2,3,4,8.0],float)
for x in val:
    print(x,end=' ')
    
''' 
1 we need numpy  because  array only support homogenious [1,2,3] array but numpy also support hetrogenious array([1,2,3.0,'a])
2
'''

# linspace (start ,end,no.of partiations)
print('\n')
arr1=linspace(10,20,7)
for x in arr1:
    print(x,end=" ")


# arange  is also used for A.p progression
print('\n arrage conept \n')
# arrange(start,end ,common differnecs)
arr2 = arange(1,20,3)
for x in arr2:
    print(x,end=" ")
    
print ('\n')
# logspace
arr3 = logspace(1,20,3)
for x in arr3:
    print(x,end=" ")
print('\n')
#Zeroes no.of zeroes you want to create
arr4 = zeros(20)
for x in arr4:
    print(x,end=" ")
arr5 = ones(20)
print('\n')
for x in arr5:
    print(x,end=" ")

# to create an array like [6 6  6 6 6 ]
print('\n')
arr5 = full(6,5)
for x in arr5:
    print(x,end=" ")
