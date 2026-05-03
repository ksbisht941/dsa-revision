import random

def bubbleSort(arr):
    """Sort the list in place using bubble sort and return the sorted list."""
    n = len(arr)
    idx = 0

    while idx < n - 1:
        jdx = 0
        while jdx < n - 1 - idx:
            if arr[jdx] > arr[jdx + 1]:
                arr[jdx], arr[jdx + 1] = arr[jdx + 1], arr[jdx]
            jdx += 1
        idx += 1

    return arr

arr = [random.randint(1, 100) for _ in range(10)]
print("Unsorted array:", arr)

result = bubbleSort(arr)
print("  Sorted array:", result)