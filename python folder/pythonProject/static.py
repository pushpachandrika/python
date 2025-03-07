class MyClass:
    static_variable = "This is a static variable"
    def __init__(self, name):
        self.name = name

    @classmethod
    def access_static_variable(cls):
        return cls.static_variable
print(MyClass.static_variable)
print(MyClass.access_static_variable())
obj = MyClass("John")
print(obj.static_variable)



class MyClass:
    static_variable = 100

    def __init__(self, value):
        self.instance_variable = value

    def show_values(self):
        print(f"Instance Variable: {self.instance_variable}")
        print(f"Static Variable (accessed through instance): {self.static_variable}")



obj1 = MyClass(10)
obj1.show_values()
obj2 = MyClass(20)
obj2.show_values()
obj1.static_variable = 200


class MyClass:
    static_variable = 100

    def __init__(self, value):
        self.instance_variable = value

    def change_static_variable(self, new_value):
        MyClass.static_variable = new_value

    def change_instance_variable(self, new_value):
        self.static_variable = new_value

    def show_values(self):
        print(f"Instance Variable: {self.instance_variable}")
        print(f"Static Variable (accessed through instance): {self.static_variable}")




obj1 = MyClass(10)
obj1.show_values()
obj1.change_static_variable(500)
obj1.show_values()
obj2 = MyClass(20)
obj2.show_values()
obj2.change_instance_variable(300)
obj1.show_values()
obj2.show_values()



class MyClass:
    static_variable = 100

    def __init__(self, value):
        # Instance variable
        self.instance_variable = value

    @classmethod
    def change_static_variable(cls, new_value):
        cls.static_variable = new_value

    def show_values(self):
        print(f"Instance Variable: {self.instance_variable}")
        print(f"Static Variable (via class): {MyClass.static_variable}")


obj1 = MyClass(10)
obj1.show_values()
obj1.change_static_variable(500)
obj1.show_values()
obj2 = MyClass(20)
obj2.show_values()