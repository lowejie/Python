# Sort in ascending or descending order
# Maintain sorted and unsorted part
# Compare elements between sorted and unsorted to insert in apropriate location
# Time complexity: O(n^2), Space complexity: O(1)
# Stable and Inplace algorithm

def insertion_sort(arr):
    for step in range(1, len(arr)):
        key = arr[step]
        j = step - 1
        while j >= 0 and key > arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key


data = [5, 2, 1, 7, 8]
insertion_sort(data)
print("Sorted Array in Descending Order")
print(data)