class MyClass:
    def __init__(self, arg1=None, arg2=None):
        if arg1 is None and arg2 is None:
            self.value1 = "Default Value"
            self.value2 = "Default Value"
            print(f"Default Constructor: value1 = {self.value1}, value2 = {self.value2}")
        elif arg2 is None:
            self.value1 = arg1
            self.value2 = "Default Value"
            print(f"One Argument Constructor: value1 = {self.value1}, value2 = {self.value2}")
        else:
            self.value1 = arg1
            self.value2 = arg2
            print(f"Two Argument Constructor: value1 = {self.value1}, value2 = {self.value2}")

class MainClass:
    def main(self):
        obj1 = MyClass()
        obj2 = MyClass("One Argument")
        obj3 = MyClass("First Argument", "Second Argument")
main_class = MainClass()
main_class.main()









class Parent:
    def __init__(self, arg1=None, arg2=None):
        if arg1 is None and arg2 is None:
            self.value1 = "Default Value"
            self.value2 = "Default Value"
            print(f"Parent Default Constructor: value1 = {self.value1}, value2 = {self.value2}")
        elif arg2 is None:
            self.value1 = arg1
            self.value2 = "Default Value"
            print(f"Parent One Argument Constructor: value1 = {self.value1}, value2 = {self.value2}")
        else:
            self.value1 = arg1
            self.value2 = arg2
            print(f"Parent Two Argument Constructor: value1 = {self.value1}, value2 = {self.value2}")
class Child(Parent):
    def _init_(self, arg1=None, arg2=None):
        super()._init_()
        super()._init_(arg1)
        super()._init_(arg1, arg2)
child_obj = Child("Argument1", "Argument2")







class Parent:
    def __init__(self, arg1=None, arg2=None):
        self.public_value = "Public Value"
        self._protected_value = "Protected Value"
        self.__private_value = "Private Value"
        if arg1 is None and arg2 is None:
            print(f"Parent Default Constructor: public_value = {self.public_value}, "
                  f"protected_value = {self.protected_value}, private_value = {self._private_value}")
        elif arg2 is None:
            self.public_value = arg1
            print(f"Parent One Argument Constructor: public_value = {self.public_value}, "
                  f"protected_value = {self.protected_value}, private_value = {self._private_value}")
        else:
            self.public_value = arg1
            self._protected_value = arg2
            print(f"Parent Two Argument Constructor: public_value = {self.public_value}, "
                  f"protected_value = {self._protected_value}, private_value = {self.__private_value}")

class Child(Parent):
    def _init_(self, arg1=None, arg2=None):
        super()._init_()
        super()._init_(arg1)
        super()._init_(arg1, arg2)
        print("\nAccessing in Child:")
        print(f"Public Value: {self.public_value}")
        print(f"Protected Value: {self._protected_value}")
        try:
            print(f"Private Value: {self.__private_value}")
        except AttributeError:
            print("Private Value is not accessible directly.")

child_obj = Child("Argument1", "Argument2")











class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"City: {self.city}")
person1 = Person("John Doe", 30, "New York")
print("Accessing attributes using methods:")
person1.display_info()
print("\nAccessing individual attributes directly:")
print(f"Name: {person1.name}")
print(f"Age: {person1.age}")
print(f"City: {person1.city}")