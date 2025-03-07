# 1st question Print “Bright IT Career” Ten Times Using For Loop
for i in range(10):
    print("Bright IT Career")

# 2nd question Java Program to Print 1 to 20 Numbers Using While Loop
i = 1
while i <= 20:
    print(i)
    i += 1

# 3rd question  Use Equal Operator (==) and Not Equal Operator (!=)
a = int(input())
b = int(input())
print(a == b)  # Equal
print(a != b)  # Not equal

# 4th question Print Odd and Even Numbers
for i in range(1, 21):
    if i % 2 == 0:
        print(f"{i} is Even")
    else:
        print(f"{i} is Odd")

# 5th question Largest Number Among Three Numbers
a = int(input())
b = int(input())
c = int(input())
largest = max(a, b, c)
print(f"The largest number is: {largest}")

# 6th question  Print Even Numbers Between 10 and 20 Using While Loop
i = 10
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1

# 7th question- Program to Print 1 to 10 Using Do-While Loop
i = 1
while True:
    print(i)
    i += 1
    if i > 10:
        break

# 8th  Find if a Number is Armstrong or Not
n = int(input())
sum = 0
temp = n
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if sum == n:
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")

# 9th Find if a Number is Prime or Not
n = int(input())
is_prime = True
for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break
if is_prime and n > 1:
    print(f"{n} is a Prime number")
else:
    print(f"{n} is not a Prime number")

# 10th-Check if a Number is Palindrome or Not
n = int(input())
rev = 0
temp = n
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10
if rev == n:
    print(f"{n} is a Palindrome number")
else:
    print(f"{n} is not a Palindrome number")

# 11th- Check Whether a Number is EVEN or ODD Using Switch
n = int(input())
result = {0: "Even", 1: "Odd"}
print(result[n % 2])

# 12th-Print Gender (Male/Female) Program According to Given M/F Using Switch
gender = input("Enter M/F: ").upper()

gender_dict = {
    "M": "Male",
    "F": "Female"
}
print(gender_dict.get(gender, "Invalid input"))