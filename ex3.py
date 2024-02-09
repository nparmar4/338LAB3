import matplotlib.pyplot as plt

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
#intArray = [63, 39, 78, 26, 12, 40, 90]
#comparisons, swaps = bubbleSort(intArray)
#print("Array after sorting:", intArray)
#print("Number of comparisons:", comparisons)
#print("Number of swaps:", swaps)


def generate_inputs(start, stop, step):
    inputs = []
    for size in range(start, stop, step):
        inputs.append(list(range(size, 0, -1)))  # Reverse ordered input
    return inputs

# Run bubble sort on inputs of increasing size
input_sizes = list(range(100, 1100, 100))
comparisons_list = []
swaps_list = []

for size in input_sizes:
    intArray = list(range(size, 0, -1))  # Reverse ordered input
    comparisons, swaps = bubbleSort(intArray)
    comparisons_list.append(comparisons)
    swaps_list.append(swaps)

# Plotting
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(input_sizes, comparisons_list, marker='o', linestyle='-')
plt.title('Number of Comparisons vs Input Size')
plt.xlabel('Input Size')
plt.ylabel('Number of Comparisons')

plt.subplot(1, 2, 2)
plt.plot(input_sizes, swaps_list, marker='o', linestyle='-')
plt.title('Number of Swaps vs Input Size')
plt.xlabel('Input Size')
plt.ylabel('Number of Swaps')

plt.tight_layout()
plt.show()


#this code was generated with AI but was significantly modified to be accurate