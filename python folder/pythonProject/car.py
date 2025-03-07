# car.py
class Car:
    def _init_(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"This car is a {self.brand} {self.model}.")

