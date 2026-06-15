# Can you change the values inside a list which is contained in set S?
s = {8, 7, 12, "Harry", [1,2]}
s[4][0] = 9

# Can we have a set with 18 (int) and '18' (str) as a value in it?
s = set()
s.add(18)
s.add("18")
print(s)

# What will be the length of following set s:
s = set()
s. add(20)
s. add (20.0)
s. add('20') # length of s after these operations
print(len(s))
# coz 20 == 20.0

# write a program to input 8 number from user and display all the unique numbers(once)
s = set()
n = input("Enter number : ")
s.add(int(n))
n = input("Enter number : ")
s.add(int(n))
n = input("Enter number : ")
s.add(int(n))
n = input("Enter number : ")
s.add(int(n))
n = input("Enter number : ")
s.add(int(n))
n = input("Enter number : ")
s.add(int(n))
n = input("Enter number : ")
s.add(int(n))
n = input("Enter number : ")
s.add(int(n))

print(s)
# s = {} what is the type of s
s ={}
print(type(s))

# Create a set with 5 numbers.
s ={1, 3, 45, 76, 23}
print(s)

# Add an element using add().
e ={1, 3, 45, 76, 23}
e.add(18)
print(e)

# Remove an element using remove()
f ={1, 3, 45, 76, 23}
f.remove(3)
print(f)

# Find the union of two sets.
a = {1, 2, 3, 4}
b ={2, 5, 6}
print(a.union(b))

# Find the intersection of two sets
a = {1, 2, 3, 4}
b ={2, 5, 6}
print(a.intersection(b))

# Find the difference between two sets.
a = {1, 2, 3, 4}
b ={2, 5, 6}
print(a.difference(b))

# Check if an element exists in a set.
s ={1, 3, 45, 76, 23}
print(1 in s)


# Find the length of a set.
x ={1, 3, 45, 76, 23, 7, 18}
print(len(x))

# Convert a list into a set
c =[1,2, 3, 45, 10, "Shahbaz"]
print(set(c))

# Clear all elements from a set.
w ={1, 3, 45, 76, 23, 7, 18}
w.clear()
print(w)
