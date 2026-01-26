def QuickSort(arr,left,right):
    if(left<right):
        pivot=partition(arr,left,right)
        
        QuickSort(arr,left,pivot-1)
        QuickSort(arr,pivot+1,right)
        
def partition(arr,left,right):
    pivot_p=arr[left]
    i=left+1
    j=right
    
    while( True):
        while(i<= j  and arr[i]<pivot_p):
            
            i=i+1
            
        while(i<=j and arr[j]>pivot_p):
            j=j-1
            
        if (i<j):
            arr[i],arr[j]=arr[j],arr[i]
        else:
            break
        
    arr[left],arr[j]=arr[j],arr[left]
    return j

arr=[1,50,39,2,1,74,489,939,501,9,282,]
QuickSort(arr,0,len(arr)-1)
print(arr)