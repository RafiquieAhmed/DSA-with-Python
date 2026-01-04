from array import *
''' array size take from user '''
arr =array('i',[])
n=int(input("Enter a number"))

for  i in range(0,n):
    arr.append(int(input("enter next input ")))
    
for x in arr:
    print(x,end=" ")
    
