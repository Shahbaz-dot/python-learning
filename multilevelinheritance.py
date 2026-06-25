# MultilevelInheritance
class Employee:
    a = 1


class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3

o = Employee()
print(o.a) # prints the a attributes
# print(o.b) # shows an error as there is no b attributes in employe class

o = Programmer()
print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)



# class grandfather and class father
class Grandfather:
    def show_grandfather(self):
        print("My GrandFather: Marhum Aftab Alam")

class Father(Grandfather):
    def show_father(self):
        print("My Father: Mr Ehfaz Alam")

class Son(Father):
    def show_son(self):
        print("Son : Mr Shahbaz Alam")

obj = Son()
obj.show_grandfather()
obj.show_father()
obj.show_son()
