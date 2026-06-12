# Write a python program to display a user entered name followed by Good Afternoon using input () function 
name = input("Enter your name:")
# print("Good Afternoon:", name)
print(f"Good Afternoon, {name}")

# Write a program to fill in a letter template given below with name and date
letter = '''Dear <|Name|>,
You are selected as a Python Developer in Amazon!
<|Date|>'''
print(letter.replace("<|Name|>", "Shahbaz bin ehfaz").replace("<|Date|>", "12 June 2026"))

# write a program to format the following letter using escape sequance charactersconst person = {
letter = "Dear Shahbaz, \n\this macbook is nice. \nThanks!"
print(letter)

# replace the double space form problem 3 with single spaces
name = "Shhahbaz alam iss   good boy"
print(name.replace("   ", " "))
print(name) # strings are immuatabele that you can not change them by runing functions on them

# Create a string and print it.
a = "shahbaz"
print(a)
print(type(a))

# Print the length of a string
a = "shahbaz"
print(len(a))

# Convert a string to uppercase.
a = "shahbaz"
print(a.upper())

# Convert a string to lowercase.
a = "Shahbaz"
print(a.lower())

# Count how many times a character appears in a string.
a = "shhahbaaz"
print(a.count("h"))

# Check whether a word exists in a string.
a = "Shahbaaz is good guy"
print("good" in a)

# Reverse a string.
a ="zabhahs"
print(a[::-1])

# Replace one word with another in a string.
b =  "Shahbaz is a good boy x"
print(b.replace("x", "best"))

# Take a name as input and print "Hello, Name".
a = input("Enter a name: ")
print("helllo", a)

# Check whether a string is a palindrome.
a = input("Enter a string: ")

if a == a[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
