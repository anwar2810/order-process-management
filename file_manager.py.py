import os
import shutil

# Create a new directory
def create_directory(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
        print(f"Directory '{directory_name}' created.")
    else:
        print(f"Directory '{directory_name}' already exists.")

# Create a new file
def create_file(file_path, content=""):
    with open(file_path, 'w') as file:
        file.write(content)
    print(f"File '{file_path}' created.")

# Delete a file
def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File '{file_path}' deleted.")
    else:
        print(f"File '{file_path}' does not exist.")

# Example usage
directory_name = "new_folder"
file_name = "new_file.txt"
file_path = os.path.join(directory_name, file_name)

create_directory(directory_name)
create_file(file_path, "This is a new file.")
delete_file(file_path)
# Delete the directory
def delete_directory(directory_name):
    if os.path.exists(directory_name):
        shutil.rmtree(directory_name)
        print(f"Directory '{directory_name}' deleted.")
    else:
        print(f"Directory '{directory_name}' does not exist.")

delete_directory(directory_name)