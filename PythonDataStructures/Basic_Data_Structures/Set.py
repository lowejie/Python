# Set is an unordered and unindexed colleciton of elements enclosed with {}

set1 = {1, "a", 3.14}
print(set1)

# Does not allow duplicates
set1 = {1, "a", 3.14, 1, 1, "a", "a"}
print(set1)

# Add values to set
set1.add("hello world")
print(set1)
set1.update(["python", 38, 3+9j])
print(set1)