# Create a class Animal with a method sound(). Create a class Dog that inherits from Animal and calls the method.
class Animal:
    def sound(self):
        print("Animals make sounds")

class Dog(Animal):
    pass

d = Dog()
d.sound()

# using inheriting attributes
# Create a class Person with name and age. Create a class Student inheriting from Person.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

s = Student("Shahbaz", 20)
s.display()

# Question 3: Using super()
# Create a class Vehicle and a derived class Car

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def show(self):
        print(self.brand, self.model)

c = Car("Toyota", "Fortuner")
c1 = Car("Ford", "Endevor")
c.show() 
c1.show() 

# question 4: Employye and manager

class Employee:
    def __init__(self, name):
        self.name = name

class Manager(Employee):
    def work(self):
        print(self.name, "manages the team") 

m = Manager("Shahbaz")
m.work()
