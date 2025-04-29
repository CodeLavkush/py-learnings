class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"{self.brand} {self.model}"

class Battery:
    def batteryInfo(self):
        return "This is battery"

class Engine:
    def engineInfo(self):
        return "This is engine"

class ElectricCar(Car, Battery, Engine):
    pass

my_new_tesla = ElectricCar("Tesla", "Model S")

print(my_new_tesla.batteryInfo())
print(my_new_tesla.engineInfo())
print(my_new_tesla.full_name())
