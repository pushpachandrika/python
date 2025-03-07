import random


def generate_expression():
    num1 = random.randint(1, 10)
    num2 = random.randint(0, 10)  # for 0 casee
    operator = random.choice(['+', '-', '*', '/'])
    expression = f"{num1} {operator} {num2}"
    return expression


def main():
    for _ in range(5):
        expression = generate_expression()
        result = eval(expression)  # This will raise an error if there  is a division by zero
        print(f"Expression: {expression} = {result}")


if __name__ == "__main__":
    main()

import random


def generate_expression():
    num1 = random.randint(1, 10)
    num2 = random.randint(0, 10)  # num2 can be 0, which may cause division by zero
    operator = random.choice(['+', '-', '*', '/'])
    expression = f"{num1} {operator} {num2}"
    return expression


def main():
    for _ in range(5):
        expression = generate_expression()
        try:
            result = eval(expression)  # to calculate string
            print(f"Expression: {expression} = {result}")
        except ZeroDivisionError:  # Catch block for division by zero
            print(f"Expression: {expression} = Error: Division by zero")


if __name__ == "__main__":
    main()


def method_that_raises_exception():
    # This method raises a ZeroDivisionError
    result = 1 / 0  # Division by zero will raise an exception
    return result


def main():
    print("Calling the method that raises an exception...")
    method_that_raises_exception()  # This will raise an exception


if __name__ == "__main__":
    main()

import random


def generate_expression():
    num1 = random.randint(1, 10)  # Random number between 1 and 10
    num2 = random.randint(0, 10)  # Random number between 0 and 10 (to allow division by zero)
    operator = random.choice(['+', '-', '*', '/', '('])
    expression = f"{num1} {operator} {num2}"
    return expression


def evaluate_expression(expression):
    return eval(expression)  # Evaluate the expression


def main():
    for _ in range(5):
        expression = generate_expression()
        try:
            result = evaluate_expression(expression)
            print(f"Expression: {expression} = {result}")
        except ZeroDivisionError:
            print(f"Expression: {expression} = Error: Division by zero")
        except SyntaxError:
            print(f"Expression: {expression} = Error: Invalid syntax")
        except Exception as e:
            print(f"Expression: {expression} = An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()


def method_that_raises_exception():
    # This method raises a ValueError with a custom message
    raise ValueError("This is a custom error message: Something went wrong!")


def main():
    print("Calling the method that raises an exception...")
    method_that_raises_exception()  # This will raise an exception


if __name__ == "__main__":
    main()

import random


# Define a custom exception
class MyCustomError(Exception):
    """Custom exception class for specific error handling."""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def generate_random_number():
    """Function that generates a random number between -10 and 10."""
    return random.randint(-10, 10)  # Random number between -10 and 10


def check_value(value):
    """Function that raises MyCustomError if the value is negative."""
    if value < 0:
        raise MyCustomError("Negative values are not allowed!")


def main():
    try:
        # Generate a random number
        random_number = generate_random_number()
        print(f"Generated random number: {random_number}")

        # Check the value
        check_value(random_number)  # Check the value
        print(f"The number {random_number} is valid.")

    except MyCustomError as e:
        print(f"Caught an exception: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()

import random


# Define a custom exception
class MyCustomError(Exception):
    """Custom exception class for specific error handling."""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def generate_random_number():
    """Function that generates a random number between -10 and 10."""
    return random.randint(-10, 10)  # Random number between -10 and 10


def check_value(value):
    """Function that raises MyCustomError if the value is negative."""
    if value < 0:
        raise MyCustomError("Negative values are not allowed!")


def main():
    try:
        # Generate a random number
        random_number = generate_random_number()
        print(f"Generated random number: {random_number}")

        # Check the value
        check_value(random_number)  # Check the value
        print(f"The number {random_number} is valid.")

    except MyCustomError as e:
        print(f"Caught an exception: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Execution of the main function is complete.")


if __name__ == "__main__":
    main()

import random


def generate_expression():
    """Generate a random arithmetic expression."""
    num1 = random.randint(1, 10)  # Random number between 1 and 10
    num2 = random.randint(0, 10)  # Random number between 0 and 10 (to allow division by zero)
    operator = random.choice(['+', '-', '*', '/'])
    expression = f"{num1} {operator} {num2}"
    return expression


def evaluate_expression(expression):
    """Evaluate the arithmetic expression and handle exceptions."""
    try:
        result = eval(expression)  # Evaluate the expression
        return result
    except ZeroDivisionError:
        raise ZeroDivisionError("Error: Division by zero is not allowed.")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")


def main():
    for _ in range(5):
        expression = generate_expression()
        print(f"Generated expression: {expression}")
        try:
            result = evaluate_expression(expression)
            print(f"Result: {expression} = {result}")
        except ZeroDivisionError as e:
            print(e)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()

------------------- 9
th - -------------------------


def read_file(file_name):
    """Function to read a file and handle FileNotFoundError."""
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    # Specify a file name that does not exist
    file_name = "non_existent_file.txt"
    print(f"Attempting to read the file: {file_name}")
    read_file(file_name)


if __name__ == "__main__":
    main()


def read_file(file_name):
    """Function to read a file and handle IOError."""
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(content)
    except IOError as e:
        print(f"IOError: {e}")


def main():
    # Specify a file name that does not exist
    file_name = "non_existent_file.txt"
    print(f"Attempting to read the file: {file_name}")
    read_file(file_name)


if __name__ == "__main__":
    main()


class MyClass:
    def __init__(self):
        self.existing_field = "I exist!"


def access_field(obj, field_name):
    """Function to access a field of an object and handle AttributeError."""
    try:
        # Attempt to access the specified field
        value = getattr(obj, field_name)
        print(f"Value of '{field_name}': {value}")
    except AttributeError:
        print(f"Error: The field '{field_name}' does not exist in the object.")


def main():
    my_object = MyClass()

    # Attempt to access an existing field
    access_field(my_object, "existing_field")

    # Attempt to access a non-existing field
    access_field(my_object, "non_existing_field")


if __name__ == "__main__":
    main()
