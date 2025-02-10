import os
# 
# Get the contents of the directory
directory_path = '.'  # You can specify another directory path here
contents = os.listdir(directory_path)

# Print the contents
for item in contents:
    print(item)
