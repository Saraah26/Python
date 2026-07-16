from abc import ABC,abstractmethod 
class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        """Every vehicle defines hw it starts"""
        pass

class Car(Vehicle):
    def start_engine(self):
        return "Turning the key ...!"

class Motorcycle(Vehicle):
    def start_engine(self):
        return "hit the ignition button!"

car_1 = Car()
bike_1 = Motorcycle()

print(car_1.start_engine())
print(bike_1.start_engine())