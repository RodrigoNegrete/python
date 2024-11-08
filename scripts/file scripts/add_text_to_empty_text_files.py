import os

def find_empty_text_files(directory):
    empty_text_files = []
    
    # Walk through the directory and its subdirectories
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            
            # Check if the file size is 0 and it has a '.txt' extension (you can modify this check)
            if os.path.getsize(file_path) == 0 and os.path.splitext(file_path)[1].lower() == '.txt':
                empty_text_files.append(file_path)

    return empty_text_files

def add_text_to_files_with_confirmation(files_list, text_to_add):
    for file_path in files_list:
        print(f"Empty text file found: {file_path}")

    confirmation = input("Do you want to add text to these files? (yes/no): ").lower()

    if confirmation == 'yes':
        for file_path in files_list:
            with open(file_path, 'w') as file:
                file.write(text_to_add)
        print("Text added to empty text files.")
    else:
        print("No text added. Exiting.")

# Replace 'your_directory_path' with the path of the directory you want to search
directory_path = 'your_directory_path'

# Replace 'your_text_to_add' with the text you want to add to the empty files
text_to_add = 'your_text_to_add'

empty_text_files_list = find_empty_text_files(directory_path)

if not empty_text_files_list:
    print("No empty text files found.")
else:
    add_text_to_files_with_confirmation(empty_text_files_list, text_to_add)
