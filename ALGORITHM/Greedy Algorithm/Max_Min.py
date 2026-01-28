def Gready_MAx_Min(arr):
    arr.sort()
    n=len(arr)
    mid=n//2
    Min =0
    Max =0
    j=n-1
    for i in range(mid):
        Max=Max+abs(arr[i]-arr[j])
        j=j-1
        
        Min =Min+abs(arr[2*i]-arr[2*i+1])
    print("MAX Differences :",Max)
    print("MIN Differences is :",Min)
    
arr=[12,5,25,10,2,15,8,30]
Gready_MAx_Min(arr)