# Quick sort follows divide and conquer paradigm
# Pivot randomly or first/last selected
# Time complexity: O(n^2), Space complexity: basic = O(n), modified = O(log n)
# Unstable and Inplace algorithm

# Partition position finding function
def partition(arr, l, h):

    # right most element = pivot
    pivot = arr[h]

    # pointer for greater element
    i = l - 1

    # Traverse all the elements in the array and compare with pivot
    for j in range(l, h):
        if arr[j] <= pivot:
            # if smaller element is present than pivot then swap
            i = i + 1

            # swapping i with j
            (arr[i], arr[j]) = (arr[j], arr[i])

    # swap pivot with i if its greater than pivot
    (arr[i + 1], arr[h]) = (arr[h], arr[i + 1])

    # get back to the intial position where partition was done
    return i + 1

# quick sort function
def quick_sort(arr, l, h):
    if l < h:

        # smaller element than pivot --> left
        # greater element than pivot --> right
        pi = partition(arr, l, h)

        # left of pivot recursion call
        quick_sort(arr, l, pi - 1)

        # right of pivot recursion call
        quick_sort(arr, pi + 1, h)


data = [9, 8, 7, 2, 10, 20, 1]
print("Unsorted Array")
print(data)
size = len(data)
quick_sort(data, 0, size -1)
print("Sorted Array in ascending order:")
print(data)