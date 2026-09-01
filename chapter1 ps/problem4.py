import os

# Specify the directory path
directory = "/"

# Get the list of files and directories
contents = os.listdir(directory)

# Print each item
print("Contents of the directory:")
for item in contents:
    print(item)