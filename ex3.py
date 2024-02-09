def bubbleSort(a):
    numComparisons = 0
    numSwaps = 0
    k = len(a)
    for i in range(k):
        for n in range(0, k-i-1):
            numComparisons += 1
            if a[n] > a[n+1]:
                a[n], a[n+1] = a[n+1], a[n]
                numSwaps += 1
    return numComparisons, numSwaps

def bubbleSort(a):
    numComparisons = 0
    numSwaps = 0
    k = len(a)
    for i in range(k):
        for n in range(0, k-i-1):
            numComparisons += 1
            if a[n] > a[n+1]:
                a[n], a[n+1] = a[n+1], a[n]
                numSwaps += 1
    return numComparisons, numSwaps

# Example input:
intArray = [63, 39, 78, 26, 12, 40, 90]
comparisons, swaps = bubbleSort(intArray)
print("Array after sorting:", intArray)
print("Number of comparisons:", comparisons)
print("Number of swaps:", swaps)

#this code was generated with AI but was significantly modified to be accurate