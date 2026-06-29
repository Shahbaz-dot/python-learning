class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

c = Car("Toyota", "Fortuner")
print(c.brand, c.model)