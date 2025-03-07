string = "Hello"
print(string)
string1 = "World"
print(string1)
string2 = """Welcome to the world of Python"""
print(string2)
print()



# Define two strings
string1 = "Hello, "
string2 = "world!"
# Concatenate the strings
result = string1 + string2
# Print the result
print(result)



# Define a string
my_string = "Python programming"
# Find the length of the string
length = len(my_string)
# Print the length
print("The length of the string is:", length)



# Define a string
my_string = "Hello, world!"
# Extract a substring using slicing
substring = my_string[7:12]  # Extract characters from index 7 to 11
# Print the extracted substring
print(substring)



import re
# Define the string
my_string = "Hello, world!"
# Define the regular expression pattern
pattern = r"^Hello"
# Use re.match() to check if the string matches the pattern
match = re.match(pattern, my_string)
# Check if a match was found
if match:
    print("The string matches the pattern.")
else:
    print("The string does not match the pattern.")



# List of strings
words = ["apple", "banana", "cherry"]
# Sort the list lexicographically
sorted_words = sorted(words)
print(sorted_words)





# Define some strings
string1 = "Hello, world!"
string2 = "hello, world!"
string3 = "world"
string4 = "hello"
string5 = "apple"
string6 = "banana"
# 1. Demonstrate startswith()
print("Demonstrating startswith():")
print(f"Does '{string1}' start with 'Hello'? {string1.startswith('Hello')}")
print(f"Does '{string2}' start with 'hello'? {string2.startswith('hello')}")
print(f"Does '{string1}' start with 'world'? {string1.startswith('world')}")
print()

# 2. Demonstrate endswith()
print("Demonstrating endswith():")
print(f"Does '{string1}' end with 'world!'? {string1.endswith('world!')}")
print(f"Does '{string2}' end with 'world'? {string2.endswith('world')}")
print(f"Does '{string1}' end with 'Hello'? {string1.endswith('Hello')}")
print()

# 3. Demonstrate comparison (similar to compareTo() in Java)
print("Demonstrating string comparison (similar to compareTo()):")
# Comparing string1 and string3
if string1 < string3:
    print(f"'{string1}' is lexicographically less than '{string3}'")
elif string1 == string3:
    print(f"'{string1}' is equal to '{string3}'")
else:
    print(f"'{string1}' is lexicographically greater than '{string3}'")



my_string = "***Hello, world!***"
# Trim '*' characters
trimmed_string = my_string.strip('*')
# Print the result
print(f"Original string: '{my_string}'")
print(f"Trimmed string: '{trimmed_string}'")




# Define a string
my_string = "Hi, world! Hi again!"
# Replace 'Hi' with 'Hello'
new_string = my_string.replace("Hi", "Hello")
# Print the result
print(new_string)


# Define a string with spaces
my_string = "Hello world this is Pushpa"
# Split the string into a list of words
split_list = my_string.split()
# Print the result
print(split_list)



# Define an integer
num = 1510
# Convert the integer to a string
num_str = str(num)
# Print the result
print(f"Integer: {num}")
print(f"String: {num_str}")



# Define a string in uppercase
my_string = "KANURI PUSHPA CHANDRIKA"
# Convert the string to lowercase
lowercase_string = my_string.lower()
# Print the result
print(lowercase_string)


