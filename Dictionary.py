# s = {} what is the type of s
s ={}
print(type(s))

# Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!
words = {
    "madad": "Help",
    "kursi": "chair",
    "Billi": "Cat",

}

word = input("Enter thw word you want meaning of: ")
print(words[word])

# Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are
d = {}
name = input("Enter friends name: ")
lang = input("Enter Lnaguage name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Lnaguage name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Lnaguage name: ")
d.update({name: lang})

name = input("Enter friends name: ")
lang = input("Enter Lnaguage name: ")
d.update({name: lang})

print(d)
