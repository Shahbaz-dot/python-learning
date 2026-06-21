# 1. Create a Class "Programmer" for storing information of few programmers working at Microsoft.
class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Shahbaaz", 1800000, 841231)
print(p.name, p.salary, p.pin, p.company)

z = Programmer("zishan", 2000000, 226028)
print(z.name, z.salary, z.pin, z.company

# Write a class "calculator" capable of finding square, cube and square root of a number.
class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square is {self.n*self.n}")

    def cube(self):
        print(f"The cube of {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The squareroot is {self.n**1/2}")

a = Calculator(4)
a.square()
a.cube()
a.squareroot()

# 3. Create a class with a class attribute a; create an object from it and set 'a' directly using object.ai= o. Does this change the class attribute?

class Demo:
    a = 4

o = Demo()
print(o.a) # prints the class attributes because instance attributes is not persent

o.a = 0 # class instance(object) is set
print(o.a)  #prints the class attributes because instance attributes is persent
print(Demo.a)

# Add a static method in problem 2, to greet the user with hello.
class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square is {self.n*self.n}")

    def cube(self):
        print(f"The cube of {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The squareroot is {self.n**1/2}")

    @staticmethod
    def hello():
        print("hello there!")

a = Calculator(4)
a.square()
a.cube()
a.squareroot()
a.hello()

# Write a class Train which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.
from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no: {self.trainNo}  is running on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")


t = Train(15034)
t.book("Lucknow", "Siwan")
t.getStatus()
t.getFare("Lucknow", "Siwan")

# Can you change the self-parameter inside a class to something else (say
# "harry"). Try changing self to "slf" or "harry" and see the effects.
from random import randint

class Train:
    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(alam, fro, to):
        print(f"Ticket is booked in train no: {alam.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no: {self.trainNo}  is running on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")


t = Train(15034)
t.book("Lucknow", "Siwan")
t.getStatus()
t.getFare("Lucknow", "Siwan")
