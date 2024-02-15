import time
import random
import matplotlib.pyplot as plt
import numpy as np

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        left, right = 0, i
        while left < right:
            mid = (left + right) // 2
            if key < arr[mid]:
                right = mid
            else:
                left = mid + 1
        arr.insert(left, key)
        del arr[i+1]

def run_experiment(n):
    traditional_times = []
    binary_times = []
    for i in range(1, n+1):
        arr = [random.randint(0, 1000) for _ in range(i)]
        
        start_time = time.time()
        insertion_sort(arr.copy())
        traditional_times.append(time.time() - start_time)
        
        start_time = time.time()
        binary_insertion_sort(arr.copy())
        binary_times.append(time.time() - start_time)
    
    return traditional_times, binary_times

def plot_results(traditional_times, binary_times):
    x = np.arange(1, len(traditional_times) + 1)
    plt.plot(x, traditional_times, label='Traditional Insertion Sort')
    plt.plot(x, binary_times, label='Binary Insertion Sort')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (s)')
    plt.legend()
    plt.show()

n = 100
traditional_times, binary_times = run_experiment(n)
plot_results(traditional_times, binary_times)


#The results of this experiment show that the traditional insertion sort is faster
#for smaller input sizes. Binary insertion sort on the other hand becomes faster
#as the input sizes increases. The reason for this is because traditional
#insertion sort has a worst-case time complexity of O(n^2), and binary insertion
#sort has a worst-case time complexity of O(n log n). As the input size increases,
#the difference in time complexity becomes more apparent which results in the 
#binary insertion sort method becoming the faster of the two for large inputs.

#this code was generated using AI but was modified to ensure accurate output