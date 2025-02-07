# Checks each and every element
# Brute force algorithm
# Time complexity and Space complexity: O(1) 

def linear_search(arr, size, target):
    for i in range(0, size):
        if arr[i] == target:
            return i
    return -1


array = [2, 4, 0, 1, 9]
x = 0
n = len(array)
result = linear_search(array, n, x)
if result == -1:
    print("Element not found.")
else:
    print(f"Element found at index: {result}")

