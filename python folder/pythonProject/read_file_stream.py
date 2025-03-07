 Read file line by line (stream reading)
file_name = "sample.txt"

with open(file_name, "r") as file:
    for line in file:
        print(line, end="")  # Print each line