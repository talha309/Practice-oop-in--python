class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    
    def start(self):
        print ("Vehicle is  start ...")

class Car(Vehicle):
    def __init__(self, brand, doors):
        super().__init__(brand)    
        self.doors = doors

    def start(self):
        return f"{self.brand} Car is starting.."

class Bike(Vehicle):
    def __init__(self, brand, type):
        super().__init__(brand)
        self.type = type
    def start(self):
        return f"{self.brand} Bike is Starting..."

c1 = Car("Toyota",4)
print (c1.start())
b1 = Bike("Honda", 70)
print (b1.start())

        
