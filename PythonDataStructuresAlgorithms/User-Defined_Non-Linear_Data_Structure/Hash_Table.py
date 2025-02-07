# Hashing takes key as input and provides hash value as output.
# One-way function
# Hash table stores pairs of keys and values

# Function with parameters

def hashing_key(key, m):
    # modulus operation to find hash value
    return key % m


# The size of the hash table
m = 8
print(f"The hash value for 4 is {hashing_key(4, m)}")
print(f"The hash value for 3 is {hashing_key(3, m)}")
print(f"The hash value for 10 is {hashing_key(10, m)}")
print(f"The hash value for 12 is {hashing_key(12, m)}")
print(f"The hash value for 8 is {hashing_key(8, m)}")
