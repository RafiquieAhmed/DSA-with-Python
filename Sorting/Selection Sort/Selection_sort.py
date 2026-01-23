def Selection_Sorting(arr):
    size=len(arr)
    
    for i in range(size):
        min=i
        for j in range(i,size):
            if(arr[min]>arr[j]):
                min=j
        arr[i],arr[min]=arr[min],arr[i]

arr=[10,20,4,7,9,40,80,70]
Selection_Sorting(arr)
print(arr)
    