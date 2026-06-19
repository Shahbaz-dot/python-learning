# Write a program using functions to find greatest of three numbers
a = 1
b = 3
c = 5

def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c

a = 1
b = 23
c = 5

print(greatest(a, b, c))

# Write a python function to print first n lines of the following pattern:
# ***
# **  - for n = 3
# *
def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)

pattern(3)

# Write a python program using function to convert Celsius to farenheit
def f_to_c(f):
    return 5*(f-32)/9
    
f = int(input("Enter temperature in F: "))
c = f_to_c(f)
print(f"{round(c, 2)} °C" )

# Write a python function which converts inches to cms
def inch_to_cms(inch):
    return inch * 2.54

n = int(input("Enter value in inches: "))

print(f"The corresponding value n cms is {inch_to_cms(n)}")

# How do you prevent a python print) function to print a new line at the end
print("a")
print("b")

# agar chte ho new line na aaye to end="" krdo
print("c", end="")
print("d", end="")

# Write a recursive function to calculate the sum of first n natural numbers
'''
sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 3 + 4

sum(n) = 1 + 2 + 3 + 4..... n

sum(n) = sum(n-1) + n
'''
def sum(n):
    if(n==1):
        return  1
    return sum(n-1) + n

print(sum(4))
