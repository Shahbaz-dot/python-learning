# Write a program to find the greatest of four numbers entered by the user
a1 = int(input("Enter the number 1:"))
a2 = int(input("Enter the number 2:"))
a3 = int(input("Enter the number 3:"))
a4 = int(input("Enter the number 4:"))

if(a1>a2 and a1>a3 and a1>a4):
    print("Greatest number is a1:", a1)

elif(a2>a1 and a2>a3 and a2>a4):
    print("Greatest number is a2:", a2)

elif(a3>a1 and a3>a2 and a3>a4):
    print("Greatest number is a3:", a3)
    
# elif(a4>a1 and a4>a2 and a4>a3):
#     print("Greatest number is a4:", a4)
else:
    print("Greatest number is a4:", a4)

# Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user
marks1 = int(input("Enter your marks 1: "))
marks2 = int(input("Enter your marks 2: "))
marks3 = int(input("Enter your marks 3: "))

# Check for total percentage
total_percentage = (100*(marks1 + marks2 + marks3))/300
if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are passed:", total_percentage)

else:
    print("You failed, try again next year:", total_percentage)
  
#  Positive, Negative, or Zero: Take a number as input and print: "Positive" if number > 0: "Negative" if number < 0:"Zero" if number == 0
number = int(input("Enter a number: "))
if(number > 0):
    print("Postive")
elif(number < 0):
    print("Negative")
elif( number == 0):
    print("Zero")
print("thank you")

# A spam comment is defined as a text containing following keywords: "Make a lot of money", "buy now", "subscribe this", "click this". Write a program to detect these spams
p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("Enter your comment: ")
if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This comment is spam")

else:
    print("This comment is not a spam")

# Write a program to find whether a given username contains less than 10 characters or not
username = input("Enter username:")
if(len(username)<10):
    print("Your user contains less than 10 characters")

else:
    print("Your user contains more than or equal to 10 characters")

# Write a program which finds out whether a given name is present in a list or not
l = ["Shahbaz", "sunny", "zishan", "wasif", "kamran"]
name = input("Enter your name: ")

if(name in l):
    print("Your name is in the list")

else:
    print("Your name is not in the list")

# Even or Odd: Take an integer and check whether it is even or odd.
num = int(input("Enter a number: "))
if(num % 2 == 0):
    print("Number is Even")
else:
    print("Number is Odd")

# Write a program to find out whether a given post is talking about "Shahbaz" or not.
post = input("Enter the post: ")

if("Shahbaz".lower() in post.lower()):
    print("This post is talking about shahbaz")

else:
    print("This post is not talking about shahbaz")
  
# Largest of Two Numbers: Take two numbers and print the larger one.Taking two numbers as input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print(f"The largest number is: {num1}")
elif num2 > num1:
    print(f"The largest number is: {num2}")
else:
    print("Both numbers are equal")
