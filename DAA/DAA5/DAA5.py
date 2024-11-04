import random
import time

# Deterministic QuickSort (Pivot: Last Element)
def deterministic_partition(arr, low, high):
    pivot = arr[high]  # Choose the last element as pivot
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def deterministic_quick_sort(arr, low, high):
    if low < high:
        pi = deterministic_partition(arr, low, high)
        deterministic_quick_sort(arr, low, pi - 1)
        deterministic_quick_sort(arr, pi + 1, high)

# Randomized QuickSort (Pivot: Random Element)
def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)  # Choose a random pivot
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return deterministic_partition(arr, low, high)

def randomized_quick_sort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quick_sort(arr, low, pi - 1)
        randomized_quick_sort(arr, pi + 1, high)

# Function to compare the two methods
def compare_quick_sorts(n):
    # Generate a large list of random integers
    arr = [random.randint(1, 10000) for _ in range(n)]
    
    # Copy the array for both sorting algorithms
    arr_deterministic = arr[:]
    arr_randomized = arr[:]

    # Measure time for deterministic quicksort
    start_time = time.time()
    deterministic_quick_sort(arr_deterministic, 0, n - 1)
    deterministic_time = time.time() - start_time

    # Measure time for randomized quicksort
    start_time = time.time()
    randomized_quick_sort(arr_randomized, 0, n - 1)
    randomized_time = time.time() - start_time

    # Print results
    print(f"Array size: {n}")
    print(f"Deterministic QuickSort time: {deterministic_time:.5f} seconds")
    print(f"Randomized QuickSort time: {randomized_time:.5f} seconds")

# Driver code
if __name__ == "__main__":
    n = int(input("Enter the size of the array (e.g., 100000 for large analysis): "))
    compare_quick_sorts(n)
