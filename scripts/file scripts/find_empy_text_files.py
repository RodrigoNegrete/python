import os

def add_text_to_empty_text_files(directory, text_to_add):
    # Walk through the directory and its subdirectories
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            
            # Check if the file size is 0 and it has a '.txt' extension (you can modify this check)
            if os.path.getsize(file_path) == 0 and os.path.splitext(file_path)[1].lower() == '.txt':
                # Open the file in write mode and add the text
                with open(file_path, 'w') as file:
                    file.write(text_to_add)

# Replace 'your_directory_path' with the path of the directory you want to search
directory_path = 'your_directory_path'

add_text_to_empty_text_files(directory_path)
print("Text added to empty text files.")
