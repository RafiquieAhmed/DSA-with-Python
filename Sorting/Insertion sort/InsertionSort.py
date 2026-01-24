def insertion(arr):
    size=len(arr)
    for i in range(1,size):
        key =arr[i]
        j =i-1
        while(j>=0 and key <arr[j]):
            arr[j+1]=arr[j]
            j=j-1
            
        arr[j+1]=key
arr=[64,32,25,45,40,51,2]
insertion(arr)
print(arr)