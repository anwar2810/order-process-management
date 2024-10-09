# file_manager.py

import os

def list_files(directory):
    """List all files in the given directory."""
    try:
        with os.scandir(directory) as entries:
            for entry in entries:
                if entry.is_file():
                    print(entry.name)
    except FileNotFoundError:
        print(f"The directory {directory} does not exist.")

if __name__ == "__main__":
    directory = input("Enter the directory path: ")
    list_files(directory)