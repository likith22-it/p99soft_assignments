
from abc import ABC,abstractmethod

class Vehcile(ABC):
    @abstractmethod
    def create(self):
        pass

class car(Vehcile):
    def create(self):
        print("car created")

class bike(Vehcile):
    def create(self):
        print("bike created")

class FactoryMethod:
    @staticmethod
    def vehcile(type):
        if type=="car":
            return car()
        elif type=="bike":
            return bike()
        
if __name__=="__main__":
    factory=FactoryMethod.vehcile("car")
    factory.create()