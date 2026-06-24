# multipleinheritance

class Employee:
    company = "ITC"
    name ="Shahbaz"
    def show(self):
        print(f"The name of the Employee is {self.name} and the company is {self.company}")

class Coder:
    language ="Python"
    def printLanguage(self):
        print(f"Out of all the language here is your language: {self.language}")

class Programmer(Employee, Coder):
    company = "ITC Infotech"
    def showlanguage(self):
        print (f"The name is {self.company} and he is good with {self.language} language")

a = Employee()
b = Programmer()


b.show()
b.showlanguage()
b.printLanguage()


# Problem 1: Basic Multiple Inheritance
# Create two classes Father and Mother. Both have a method. Create a Child class that inherits from both and access both methods.

class Father:
    def father_skill(self):
        print("Father: Diploma in Electrical")

class Mother:
    def mother_skill(self):
        print("Mother: House of queen")

class Child(Father, Mother):
    pass

c = Child()
c.father_skill()
c.mother_skill()

# Problem 2: Employee and Student
# Create classes Employee and Student. A class Intern should inherit from both and display employee and student details.
class Employee:
    def employee_info(self):
        print("Employee ID: E2040")

class Student:
    def student_info(self):
        print("Student Roll no: 1240439402")

class Intern(Employee, Student):
    pass

i = Intern()
i.employee_info()
i.student_info()

# Problem 3: Constructor in Multiple Inheritance
# Use constructors from two parent classes.
class A:
    def __init__(self):
        print("Constructor of A")

class B:
    def __init__(self):
        print("Constructor of B")
        
class C(A, B):
    def __init__(self):
        A.__init__(self)        
        B.__init__(self)      
        print("Constuctor of C")  

obj = C()


# Problem 4: Calculate Area and Perimeter
# Create Area and Perimeter classes. A child class should inherit both.
class Area:
    def area(self, l, b):
        return l * b
    

class Perimeter:
    def perimeter(self, l, b):
        return 2 * (l + b)
    
class Rectangle(Area, Perimeter):
    pass

r = Rectangle()
print("Area =", r.area(5, 4))
print("Perimeter =", r.perimeter(5, 4)) 


# roblem 5: Method Resolution Order (MRO)
# What happens when both parent classes have the same method name?
class A:
    def show(self):
        print("Class A")

class B:
    def show(self):
        print("Class B")

class C(A, B):
    pass

obj = C()
obj.show()
