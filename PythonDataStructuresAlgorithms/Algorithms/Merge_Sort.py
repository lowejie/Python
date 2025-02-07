# Divide problem into 2 sub problems until only one elment left
# Merge sorted arrays into original array

def merge_sort(arr):
    if len(arr) > 1:
        x = len(arr)//2
        l = arr[:x]
        r = arr[x:]
        # Sorting the halves of array
        merge_sort(l)
        merge_sort(r)
        y = z =d = 0
        while y < len(l) and z < len(r):
            if l[y] < r[z]:
                arr[d] = l[y]
                y += 1
            else:
                arr[d] = r[z]
                z += 1
            d += 1
        while y < len(l):
            arr[d] = l[y]
            y += 1
            d += 1
        while z < len(r):
            arr[d] = r[z]
            z += 1
            d += 1

def print_list(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
# Driver program
if __name__ == '__main__':
    arr = [11, 34, 2, 18, 33, 22, 88, 9]
    merge_sort(arr)
    print("The sorted array is as follows: ")
    print_list(arr)

