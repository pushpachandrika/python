# Write a program to print your name.

print ("pushpa")
print("Multi-line commenting")

a = -5
print("Type of a: ", type(a))
b = False
print("Type of b: ", type(b))
c = 5.0
print("Type of c: ", type(c))
String = 'Hello'
print("Type of String: ", type(String))

a = 5
# Uses global because there is no local 'a'
def f():
    print('Inside f() : ', a)
def g():
    a = 2
    print('Inside g() : ', a)
def h():
    global a
    a = 4
    print('Inside h() : ', a)
# Global scope
print('global : ', a)
f()
print('global : ', a)
g()
print('global : ', a)
h()
print('global : ', a)