def bubbleSort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0, n-1-i):
            if (arr[j]> arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
arr=[ 3, 1,3 ,8 ,9,90,89,40]
bubbleSort(arr)
print(arr)