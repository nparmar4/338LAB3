import random
import time

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def measure_performance(search_algorithm, array_size, num_trials=100):
    total_time = 0
    for _ in range(num_trials):
        arr = list(range(array_size))  # Create a sorted array
        target = random.randint(0, array_size - 1)  # Choose a random target
        random.shuffle(arr)  # Shuffle the array
        start_time = time.perf_counter()
        index = search_algorithm(arr, target)
        end_time = time.perf_counter()
        total_time += end_time - start_time
    return total_time / num_trials

# Measure performance for different array sizes
array_sizes = [1000, 2000, 5000, 10000]
linear_search_times = []
binary_search_times = []

for size in array_sizes:
    linear_search_time = measure_performance(linear_search, size)
    binary_search_time = measure_performance(binary_search, size)
    linear_search_times.append(linear_search_time)
    binary_search_times.append(binary_search_time)

# Print the results
for i, size in enumerate(array_sizes):
    print(f'Array Size: {size}')
    print(f'  Linear Search: {linear_search_times[i]:.6f} seconds')
    print(f'  Binary Search: {binary_search_times[i]:.6f} seconds')
    print()

# Plot the results
import matplotlib.pyplot as plt

plt.plot(array_sizes, linear_search_times, label='Linear Search')
plt.plot(array_sizes, binary_search_times, label='Binary Search')
plt.xlabel('Array Size')
plt.ylabel('Average Time (seconds)')
plt.title('Performance of Linear vs Binary Search')
plt.legend()
plt.savefig('performance_plot.png')
plt.show()

#this code was generated using chatGPT but was slightly modified to show accurate results