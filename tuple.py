# check that a tuple cannot be changed in python
a = (34, 56,2, "Sunny")
a[2] = "Shahbaz"
print(a[2]) # not can change

# write a program to count the numbers of zero in the following tuple
a = (7, 0, 8, 0, 0, 9)
no = a.count(0)
print(no)

# Create a tuple and print it.
a = (1, 2, 3, 4, "Shahbaz")
print(a)
print(type(a))

# Print the first and last element of a tuple.
b = (1, 2, 3, 4, "Shahbaz")
print(b[0], b[-1])

# Find the length of a tuple
b = (1, 2, 3, 4, "Shahbaz")
print(len(b))

# Count the occurrence of an element using count().
b = (1, 2, 3, 4, "Shahbaz", 2, 3, 2, 2)
b.count(2)
print(b.count(2))

# Find the index of an element using index().
c = (1, 2, 3, 4, "Shahbaz")
# c.index()
print(c.index(4))

# Concatenate two tuples
l1 = (1, 2, 3, 4)
l2 = (5, 6)
print(l1 + l2)

# Repeat a tuple 3 times.
tuple = (11, 14, 0)
print("Original tuple:", tuple)

N = 3
repeated_tuple = tuple * N
print(f"Repeated {N} times:", repeated_tuple)

# Check whether an element exists in a tuple
t = (1, 2, 3, 4, 5)

print(3 in t)

# Find the maximum and minimum value in a tuple.
s = (2, 38, 25, 5, 6, 8, 3)
print(max(s))
print(min(s))

# Find the sum of all elements in a tuple
z =(1, 3, 4, 5, 7)
print(sum (z))
