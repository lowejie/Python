# Selection sort based on comparison
# Select minimum value index and swap with first index (0) in each iteration
# Repeat in each iteration
# Time complexity = O(n^2), Space complexity = O(1)
# Traditional sort might not be stable, Inplace

def selection_sort(arr, size):
    for step in range(size):
        min = step
        for i in range(step + 1, size):
            # Find minimum number
            if arr[i] > arr[min]:
                min = i
        # Put minimum number in correct position
        (arr[step], arr[min]) = (arr[min], arr[step])


data = [-20, 45, 12, 22, 19]
size = len(data)
selection_sort(data, size)
print(f"Sorted Array using selection sort in descending order: {data}")
