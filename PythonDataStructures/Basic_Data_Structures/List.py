# List is an ordered collection of elements enclosed within []

list1 = [1, "a", True, 2, 'b', False]
print(list1)

#Accessing elements within list

print(list1[0])
print(list1[1])
print(list1[1:5])

# Changing values within list

list1[0] = 100
print(list1[0])

# Adding elements

list1.append("python")
print(list1)
list1.append([1, 2, 3, 4])
print(list1)

# Remove elements
list1.pop()
print(list1)
list1.pop()
print(list1)