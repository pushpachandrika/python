# Random access reading using seek()
file_name = "sample.txt"

with open(file_name, "r") as file:
    file.seek(10)  # Move to the 10th byte in the file
    content = file.read(20)  # Read the next 20 characters
    print("Random Access Content:\n", content)