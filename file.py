import os
import shutil

def find_files_and_folders(path):
    for root, dir, files in os.walk(path):
        print(f"Current directory: {root}")
        print("Directories:")
        for directory in dir:
            print(os.path.join(root,directory))
        print("Files:")
        for file in files:
            print(os.path.join(root,file))
        print("----------------------------------------------------------------")

# shutil.make_archive("mynewzip","zip","C:/Users/okuopu637/Desktop/file manipulation")
shutil.unpack_archive("mynewzip.zip","C:/Users/okuopu637/Desktop")

print(os.walk("C:/Users/okuopu637/desktop/file manipulation"))
find_files_and_folders("C:/Users/okuopu637/desktop/file manipulation9566")

def edit_text_files(file_path, new_content):
    with open(file_path, "w") as file:
        file.write(new_content)

edit_text_files("C:/Users/okuopu637/Desktop/file manipulation/sample.txt", "Oliver Kuopus")

def search_and_erase(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"{file_path} has been erased.")
    else:
        print(f"{file_path} does not exist.")

search_and_erase("C:/Users/okuopu637/Desktop/fots/Magnolia.ttf")

def read_file(file_path):
    with open(file_path, "r") as file:
        content= file.read()
        return content

def write_to_file(file_path, text_to_write):
    with open(file_path, "w") as file:
        file.write(text_to_write)

def replace_text_in_file(file_path, old_text, _new_text):
    with open(file_path, "r") as file:
        content=file.read()

    content = content.replace(old_text, new_text)
    
    with open(file_path, "w") as file:
        file.write(content)
