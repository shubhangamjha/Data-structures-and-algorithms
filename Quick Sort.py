import time
import random

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quickSort(left) + middle + quickSort(right)

n_values = [10, 100, 1000, 10000]
for n in n_values:
    arr = [random.randint(0, 100) for _ in range(n)]
    start_time = time.time()
    quickSort(arr)
    end_time = time.time()
    print(f"Time Complexity for quick sort with n={n}: {end_time - start_time} seconds")

print("Time Complexity of Quick Sort for worst case scenario is: O(n^2)")

print("QuickSort is much faster in practice and its average-case time complexity is O(n log n)")