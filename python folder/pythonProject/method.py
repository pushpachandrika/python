
class MethodOverloadingExample:
    def print_message(self, message=None, message2=None):
        if message2 is None:
            print(f"Message: {message}")
        else:
            print(f"Message 1: {message}")
            print(f"Message 2: {message2}")
example = MethodOverloadingExample()
example.print_message("Hello, World!")
example.print_message("Hello", "World!")






class MethodOverloadingExample:
    def print_info(self, *args):
        if len(args) == 1 and isinstance(args[0], str):
            print(f"String: {args[0]}")
        elif len(args) == 1 and isinstance(args[0], int):
            print(f"Integer: {args[0]}")
        elif len(args) == 2:
            print(f"String: {args[0]} and Integer: {args[1]}")
        else:
            print("Invalid input")
example = MethodOverloadingExample()
example.print_info("Hello, World!")
example.print_info(42)
example.print_info("Hello", 42)







class MethodOverloadingExample:
    def print_info(self, info):
        if isinstance(info, str):
            print(f"String: {info}")
        elif isinstance(info, int):
            print(f"Integer: {info}")
        else:
            print("Invalid input type.")
example = MethodOverloadingExample()
example.print_info("Hello, World!")
example.print_info(42)
example.print_info(3.14)