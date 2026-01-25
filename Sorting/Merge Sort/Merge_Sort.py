def Divide(arr, low, high):
    if low < high:
        mid = low + (high - low) // 2
        Divide(arr, low, mid)
        Divide(arr, mid + 1, high)
        merge(arr, low, mid, high)

def merge(arr, low, mid, high):
    s1 = mid - low + 1
    s2 = high - mid

    leftside = [0] * s1
    rightside = [0] * s2

    for i in range(s1):
        leftside[i] = arr[low + i]

    for j in range(s2):
        rightside[j] = arr[mid + 1 + j]

    i = j = 0
    k = low

    while i < s1 and j < s2:
        if leftside[i] < rightside[j]:
            arr[k] = leftside[i]
            i += 1
        else:
            arr[k] = rightside[j]
            j += 1
        k += 1

    while i < s1:
        arr[k] = leftside[i]
        i += 1
        k += 1

    while j < s2:
        arr[k] = rightside[j]
        j += 1
        k += 1


arr = [1, 7, 4, 90, 20, 50, 11, 20]
Divide(arr, 0, len(arr) - 1)
print(arr)
