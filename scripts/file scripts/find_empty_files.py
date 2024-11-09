import os

def find_empty_files(directory):
    empty_files = []
    
    # Walk through the directory and its subdirectories
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            
            # Check if the file size is 0
            if os.path.getsize(file_path) == 0:
                empty_files.append(file_path)

    return empty_files

# Replace 'your_directory_path' with the path of the directory you want to search
directory_path = 'your_directory_path'
empty_files_list = find_empty_files(directory_path)

if not empty_files_list:
    print("No empty files found.")
else:
    print("Empty files found:")
    for file_path in empty_files_list:
        print(file_path)
