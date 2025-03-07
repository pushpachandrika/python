# Seek to a specific index and read from there
file_name = "sample.txt"

with open(file_name, "r") as file:
    index = int(input("Enter the index to start reading from: "))
    file.seek(index)  # Move to the given index
    print("Content from index", index, ":\n", file.read())