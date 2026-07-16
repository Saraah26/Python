class Vehicle:
    def __init__(self,brand):
        self.brand = brand
    
    def honk(self):
        return"Beep Beep"
class ElectricCar(Vehicle):
    def __init__(self,brand,battery_size):
        super().__init__(brand)
        self.battery_size = battery_size

v_1 = Vehicle('GMC')
Electric_1= ElectricCar('Tesla',100)
print(Electric_1.honk())
print(Electric_1.battery_size)
print(Electric_1.brand)
print(v_1.brand)
