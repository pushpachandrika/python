# person.py
class Person:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


# car.py
class Car:
    def _init_(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"This car is a {self.brand} {self.model}.")


# _init_.py (empty or contains import statements)
from .person import Person
from .car import Car

# main.py (Main program to use the package)
from mypackage import Person, Car

# Creating objects and calling methods
person1 = Person("Alice", 25)
person1.introduce()

car1 = Car("Toyota", "Corolla")
car1.display_info()