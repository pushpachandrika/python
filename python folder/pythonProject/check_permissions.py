import os

file_name = "sample.txt"

# Check read and write permissions
read_access = os.access(file_name, os.R_OK)
write_access = os.access(file_name, os.W_OK)

print(f"Read Access: {'Yes' if read_access else 'No'}")
print(f"Write Access: {'Yes' if write_access else 'No'}")