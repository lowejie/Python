# Array is a linear data structure that stores homogenous elements in contiguous locations
# Datatype varname [size] = {ele1, ele2, ele3};

# 1-D Array

num = int(input("How many elements within array?: "))
arr = []
print(f"Enter {num} elements:")
for i in range(num):
    element = input()
    arr.append(element)
print("The array elements are:\n")
for i in range(num):
    print(arr[i])
print(arr)

# 2 D array

r_num = int(input("Number of rows: "))
c_num = int(input("Number of columns: "))
twod_arr = [[0 for col in range(c_num)]for row in range(r_num)]

for row in range(r_num):
    for col in range(c_num):
        twod_arr[row][col] = row*col
print(twod_arr)
