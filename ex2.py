import timeit
import matplotlib.pyplot as plt
import numpy as np
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def generate_cases(size):
    # Best case: sorted in ascending order
    best_case = np.arange(size)
    
    # Average case: randomly shuffled
    average_case = np.random.permutation(size)
    
    # Worst case: sorted in descending order
    worst_case = np.arange(size)[::-1]
    
    return best_case, average_case, worst_case
    
#get numbers betweeen 1-100
number_set = set(range(1, 101))

# Generate 20 random different numbers from the set
sizes = random.sample(number_set, 20)

bubble_sort_times = {'best': [], 'average': [], 'worst': []}
quick_sort_times = {'best': [], 'average': [], 'worst': []}

for size in sizes:
    best_case, average_case, worst_case = generate_cases(size)
    
    # Bubble sort times
    bubble_sort_best_time = timeit.timeit(lambda: bubble_sort(best_case.copy()), number=1)
    bubble_sort_average_time = timeit.timeit(lambda: bubble_sort(average_case.copy()), number=1)
    bubble_sort_worst_time = timeit.timeit(lambda: bubble_sort(worst_case.copy()), number=1)
    
    bubble_sort_times['best'].append(bubble_sort_best_time)
    bubble_sort_times['average'].append(bubble_sort_average_time)
    bubble_sort_times['worst'].append(bubble_sort_worst_time)
    
    # Quick sort times
    quick_sort_best_time = timeit.timeit(lambda: quick_sort(best_case.copy()), number=1)
    quick_sort_average_time = timeit.timeit(lambda: quick_sort(average_case.copy()), number=1)
    quick_sort_worst_time = timeit.timeit(lambda: quick_sort(worst_case.copy()), number=1)
    
    quick_sort_times['best'].append(quick_sort_best_time)
    quick_sort_times['average'].append(quick_sort_average_time)
    quick_sort_times['worst'].append(quick_sort_worst_time)

# Plotting
plt.figure(figsize=(18, 6))

# Function to plot line of best fit
def plot_best_fit(x, y, label):
    plt.plot(x, y, 'o', label=label)
    m, b = np.polyfit(x, y, 1)
    plt.plot(x, m*np.array(x) + b, label='Line of Best Fit')

# Best case
plt.subplot(1, 3, 1)
plot_best_fit(sizes, bubble_sort_times['best'], 'Bubble Sort')
plot_best_fit(sizes, quick_sort_times['best'], 'Quick Sort')
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.title('Best Case')
plt.legend()
plt.grid(True)

# Average case
plt.subplot(1, 3, 2)
plot_best_fit(sizes, bubble_sort_times['average'], 'Bubble Sort')
plot_best_fit(sizes, quick_sort_times['average'], 'Quick Sort')
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.title('Average Case')
plt.legend()
plt.grid(True)

# Worst case
plt.subplot(1, 3, 3)
plot_best_fit(sizes, bubble_sort_times['worst'], 'Bubble Sort')
plot_best_fit(sizes, quick_sort_times['worst'], 'Quick Sort')
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.title('Worst Case')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

