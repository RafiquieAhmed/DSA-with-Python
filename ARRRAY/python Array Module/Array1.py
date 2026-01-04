'''
import array as arr

val=arr.array('i',[1,2,3,4,5,6])

for i in range(0,6):
    print(val[i],end=" ")
print('\n')
for x in val:
    print(x,end=",")
    
    '''

'''2 method  of array create '''
from array import *

val_a=array('h',[10,20,30,40,50])

for x in val_a:
    print(x*2,end=" ")
    print('\n')
val_f =array('d',[1,2,3,4,5,6.5,7,8,9.2])
for x in range(0,len(val_f)):
    print(val_f[x],end=' ')
     #u for char 

print("\n")
print("your value of type code is ",val_f.typecode)

''' reverse  of a array '''

val_f.reverse()
for x in range(0,len(val_f)):
    print(val_f[x],end=' ')

# insert value

val= array('i',[2,4,6,7,8,0])

val.insert(1,90)
val.append(10000)
val[1]=0
for x in range(0,len(val)):
    print(val[x],end =" ")
print('\n')
    
''' copy the the array from orginal copy'''

copy_arr=array(val.typecode, (x for x in val))
copy_arr.pop()
copy_arr.remove(0)
for x in range(0,len(copy_arr)):
    print(copy_arr[x],end=" ")
    
abc= copy_arr[2:-2]

print('\n')
for x in range(0,len(abc)):
    print(abc[x],end=" ")
    
    # reverse of string 
abc =copy_arr[::-1]
print('\n')
for x in range(0,len(abc)):
    print(abc[x],end=" ")
# a=val[start index : end index]



     