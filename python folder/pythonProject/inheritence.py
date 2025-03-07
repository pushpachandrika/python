class A():
    def display(self):
        print("Display Inside class A")

    def show(self):
        print("Show Inside class A")


# Subclass B inheriting from A
class B(A):
    def print(self):
        print("Print Inside class B")

    def show(self):
        print("Show Inside class B")


# Driver code
s = A()
s.display()
s.show()

k = B()
k.print()
k.show()