def add(x,y):
 return x+y
def sub(x,y):
 return x-y
def mul(x,y):
 return x*y
def div(x,y):
 if y==0:
  return undefine
 else:
  return x/y
a=float(input("enter the 1st number"))
b=float(input("enter the 2nd number"))
print("Addition :", add(a,b))
print("subtraction:", sub(a,b))
print("multiplication:", mul(a, b))
print("division:", div(a,b))


n = int(input())
# Increment operation
n += 1
print("After increment:", n)
# Decrement operation
n -= 1
print("After decrement:", n)


a = int(input())
b = int(input())

if a == b:
    print("Equal")
else:
    print("Not Equal")


a = int(input())
b = int(input())

print(a < b)    # Less than
print(a <= b)   # Less than or equal to
print(a > b)    # Greater than
print(a >= b)

a = int(input())
b = int(input())

print("Smaller:", min(a, b))
print("Larger:", max(a, b))
