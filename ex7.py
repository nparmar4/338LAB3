# Importing necessary libraries/modules
import timeit  
import random
import json 
import sys 
import matplotlib.pyplot as plt  
sys.setrecursionlimit(200000) 


# Binary search function to find the index of a key in a sorted array
def binary_search(arr, key, start_midpoint=0):
    low = 0
    high = len(arr) - 1
    mid = start_midpoint 


    # Binary search 
    while low <= high:
        mid = (low + high) // 2 
        mid_val = arr[mid] 


        # Checking if key is present at mid, lower half, or upper half of array
        if mid_val < key:
            low = mid + 1  
        elif mid_val > key:
            high = mid - 1  
        else:
            return mid  


    return -1  


# Function to find best midpoints for each task
def find_best_midpoint(arr, task):
    best_midpoints = {}  
    num_samples = min(10, len(arr)) 
   
    # Looping through tasks
    for t in task:
        best_time = float('inf') 
        best_midpoint = 0  
       
        midpoints = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]
       
        # Looping through each midpoint and timing 
        for midpoint in midpoints:
            time_taken = timeit.timeit(lambda: binary_search(arr, t, midpoint), number=100)
            if time_taken < best_time:  
                best_time = time_taken  
                best_midpoint = midpoint 
        best_midpoints[t] = best_midpoint  
   
    return best_midpoints  # Returning dictionary containing best midpoints for each task


# Loading data from JSON files
with open(r"./ex7data.json", "r", errors="ignore") as inF:
    arr = json.load(inF)


with open(r"./ex7tasks.json", "r", errors="ignore") as inF:
    task = json.load(inF)


# Finding best midpoints 
best_midpoints = find_best_midpoint(arr, task)


# Printing best midpoints
print("The best midpoints for each task are:")
for t, midpoint in best_midpoints.items():
    print(f"Task {t}: The best midpoint is {midpoint}.")


# Extracting tasks and midpoints from dictionary
tasks = list(best_midpoints.keys())
midpoints = list(best_midpoints.values())


# Plotting tasks against midpoints 
plt.figure(figsize=(10, 6))  
plt.scatter(tasks, midpoints, color='red')
plt.title('Tasks vs. Midpoints chosen')  
plt.xlabel('Task')  
plt.ylabel('Midpoint chosen')  
plt.grid(True)  
plt.show() 


#Question 4: Since the dataset provided is large and well-organized, there could a slight performance impact
#from the first option of midpoint. Onw thing that can improve performance is choosing a midway that is close
#to the value being seeked in the task. Since this dataset is so large, the difference in time would be small,
#however, if applied to a smaller dataset, it would be evidently more efficient. 