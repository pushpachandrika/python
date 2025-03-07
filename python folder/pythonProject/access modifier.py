
class Parent:
    __id = 100
    __name = "John"

    def __private_method(self):  # Private method
        print("This is a private method")
        print(f"ID: {self.__id}, Name: {self.__name}")

    def main_method(self):
        print("Inside main method:")
        print(f"Accessing private fields - ID: {self.__id}, Name: {self.__name}")
        self.__private_method()  # Calling private method


class Child(Parent):
    def access_private(self):
        try:
            print(self.__id)  # Attempt to access private field
        except AttributeError as e:
            print(f"Cannot access private field: {e}")
        try:
            self.__private_method()  # Attempt to access private method
        except AttributeError as e:
            print(f"Cannot access private method: {e}")


# Testing
print("Testing Private Fields and Methods:")
parent = Parent()
parent.main_method()
child = Child()
child.access_private()
print("\n" + "-" * 50 + "\n")


# 2. Class with Protected Fields and Methods
class Base:
    _age = 25  # Protected field
    _salary = 50000  # Protected field

    def _protected_method(self):  # Protected method
        print(f"Protected method: Age: {self._age}, Salary: {self._salary}")


# Same package class
class SamePackage:
    def access_protected(self, base_obj):
        print("Accessing from same package:")
        print(f"Age: {base_obj._age}, Salary: {base_obj._salary}")
        base_obj._protected_method()


# Different package simulation (in Python, we'll just use a different class)
class DifferentPackageChild(Base):
    def access_from_child(self):
        print("Accessing from child class (different package):")
        print(f"Age: {self._age}, Salary: {self._salary}")
        self._protected_method()


class DifferentPackage:
    def access_protected(self, base_obj):
        print("Accessing from different package:")
        print(f"Age: {base_obj._age}, Salary: {base_obj._salary}")
        base_obj._protected_method()


# Testing Protected
print("Testing Protected Fields and Methods:")
base = Base()
same_pkg = SamePackage()
same_pkg.access_protected(base)

diff_child = DifferentPackageChild()
diff_child.access_from_child()

diff_pkg = DifferentPackage()
diff_pkg.access_protected(base)
print("\n" + "-" * 50 + "\n")


# 3. Class with Public Fields and Methods
class PublicClass:
    id = 1  # Public field
    name = "Public"  # Public field

    def public_method(self):  # Public method
        print(f"Public method: ID: {self.id}, Name: {self.name}")


# Accessing from same package
class SamePackageAccess:
    def access_public(self, pub_obj):
        print("Accessing public from same package:")
        print(f"ID: {pub_obj.id}, Name: {pub_obj.name}")
        pub_obj.public_method()


# Accessing from different package
class DifferentPackageAccess:
    def access_public(self, pub_obj):
        print("Accessing public from different package:")
        print(f"ID: {pub_obj.id}, Name: {pub_obj.name}")
        pub_obj.public_method()


# Testing Public
print("Testing Public Fields and Methods:")
pub = PublicClass()
same_access = SamePackageAccess()
same_access.access_public(pub)

diff_access = DifferentPackageAccess()
diff_access.access_public(pub)