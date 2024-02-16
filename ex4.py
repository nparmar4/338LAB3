import matplotlib.pyplot as plt
import numpy as np

def quicksort(arr):
    if len(arr) <= 1:
        return arr, 0  # Base case: if the array has 0 or 1 elements, it's already sorted and no comparisons are made.
    
    pivot = arr[len(arr) // 2]  # Choose the middle element as the pivot
    left = [x for x in arr if x < pivot]  # Elements less than the pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
    right = [x for x in arr if x > pivot]  # Elements greater than the pivot
    
    sorted_left, left_comparisons = quicksort(left)  # Recursively sort the left partition
    sorted_right, right_comparisons = quicksort(right)  # Recursively sort the right partition
    
    return sorted_left + middle + sorted_right, len(arr) - 1 + left_comparisons + right_comparisons

# Test the implementation with inputs of increasing size
input_sizes = [10, 100, 1000, 10000, 100000, 1000000]
comparisons_list = []

for size in input_sizes:
    input_array = list(range(size, 0, -1))  # Generate an array of size 'size' in descending order
    sorted_array, comparisons = quicksort(input_array)
    comparisons_list.append(comparisons)
    print(f"Input size: {size}, Comparisons: {comparisons}")

# Plotting the results
plt.figure(figsize=(10, 6))
plt.plot(input_sizes, comparisons_list, marker='o', linestyle='-')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Input Size (log scale)')
plt.ylabel('Comparisons (log scale)')
plt.title('Quicksort Comparisons vs Input Size')
plt.grid(True)
plt.show()

#this code was generated using AI but was also slightly mofified to provide accurate results