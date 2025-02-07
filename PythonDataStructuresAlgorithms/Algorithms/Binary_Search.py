# Divide and Conquer and search space is reduced to half in every iteration
# Use on sorted array
# Time complexity: O(log n), Space complexity: O(1)

# Binary Search in python
def binary_search(arr, target, low, high):
    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid + 1
    return -1


array = [3, 4, 5, 6, 7, 8, 9]
x = 4
result = binary_search(array, x, 0, len(array)-1)
if result == -1:
    print("Not found.")
else:
    print(f"Element is found at index: {result}")