import sys 
sys.setrecursionlimit(20000)

def merge_sort(arr, low, high):
    if low < high:
        mid = (low+high)//2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid+1, high)
        merge(arr, low, mid, high)

def merge(arr, low, mid, high):
    n1 = mid - low + 1
    n2 = high - mid

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arr[low + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    i = 0  
    j = 0 
    k = low  

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Reference Chat GPT for following code
    # Copy the remaining elements of L[], if any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

arr = [8, 42, 25, 3, 3, 2, 27, 3]
merge_sort(arr, 0, 7)
print(arr)  