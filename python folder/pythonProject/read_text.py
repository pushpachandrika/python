#Open and read the text file
with open("sample.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content