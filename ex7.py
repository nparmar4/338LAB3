# Importing necessary libraries/modules
import timeit  # Module to measure execution time of code snippets
import random  # Module to generate random numbers
import json  # Module to work with JSON data
import sys  # Module providing access to some variables used or maintained by the Python interpreter
import matplotlib.pyplot as plt  # Module to create plots and graphs
sys.setrecursionlimit(200000)  # Setting recursion limit to avoid recursion depth errors


# Binary search function to find the index of a key in a sorted array
def binary_search(arr, key, start_midpoint=0):
    # Initializing low and high pointers for binary search
    low = 0
    high = len(arr) - 1
    mid = start_midpoint  # Initializing mid variable with the provided start_midpoint


    # Binary search loop
    while low <= high:
        mid = (low + high) // 2  # Calculating mid index
        mid_val = arr[mid]  # Getting the value at mid index


        # Checking if key is present at mid, in the lower half, or in the upper half of the array
        if mid_val < key:
            low = mid + 1  # If key is greater, update low pointer
        elif mid_val > key:
            high = mid - 1  # If key is smaller, update high pointer
        else:
            return mid  # If key is found, return its index


    return -1  # If key is not found, return -1


# Function to find the best midpoints for each task
def find_best_midpoint(arr, task):
    best_midpoints = {}  # Dictionary to store best midpoints for each task
    num_samples = min(10, len(arr))  # Determining the number of samples for each task, minimum of 10 or the array length
   
    # Looping through each task
    for t in task:
        best_time = float('inf')  # Initializing best time with infinity
        best_midpoint = 0  # Initializing best midpoint with 0
       
        # Predefined midpoints to test for the binary search
        midpoints = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000]
       
        # Looping through each midpoint
        for midpoint in midpoints:
            # Timing the binary search function with the current midpoint
            time_taken = timeit.timeit(lambda: binary_search(arr, t, midpoint), number=100)
            if time_taken < best_time:  # If current time is better than the best time
                best_time = time_taken  # Update best time
                best_midpoint = midpoint  # Update best midpoint
       
        best_midpoints[t] = best_midpoint  # Storing the best midpoint for the current task in the dictionary
   
    return best_midpoints  # Returning the dictionary containing best midpoints for each task


# Loading data from JSON files
with open(r"./ex7data.json", "r", errors="ignore") as inF:
    arr = json.load(inF)  # Loading array data from JSON file


with open(r"./ex7tasks.json", "r", errors="ignore") as inF:
    task = json.load(inF)  # Loading task data from JSON file


# Finding the best midpoints for each task
best_midpoints = find_best_midpoint(arr, task)


# Printing the best midpoints for each task
print("The best midpoints for each task are:")
for t, midpoint in best_midpoints.items():
    print(f"Task {t}: The best midpoint is {midpoint}.")


# Extracting tasks and midpoints from the dictionary
tasks = list(best_midpoints.keys())
midpoints = list(best_midpoints.values())


# Plotting tasks against midpoints chosen
plt.figure(figsize=(10, 6))  # Setting the figure size
plt.scatter(tasks, midpoints, color='red')  # Creating scatter plot
plt.title('Tasks vs. Midpoints chosen')  # Setting the title of the plot
plt.xlabel('Task')  # Setting the label for x-axis
plt.ylabel('Midpoint chosen')  # Setting the label for y-axis
plt.grid(True)  # Turning on grid
plt.show()  # Displaying the plot


# Answer to question 4 as code comments: There is a slight performance impact from the first option of midpoint, which is
#probably because the dataset in "ex7data.json" is large and well-organized. Amid a million ascending numbers, choosing a
#midway nearer the goal task seems to slightly improve performance. The overall execution time difference is still quite small,
#though. The impact of the initial midway pick would probably be more apparent in situations with smaller lists. Although the
#impact on speed is negligible, it is clear that the initial midpoint selection affects the binary search algorithm's efficiency, however slightly.