import os
import shutil

def edit_text_files(file_path, new_content):
    with open(file_path, "a") as file:
        file.write(new_content)
x = 0
while x != 2000:
    edit_text_files("C:/Users/okuopu637/desktop/file manipulation/names.txt", " Oliver ")
    x += 1

def replace_text_in_file(file_path, old_text, new_text):
    with open(file_path, "r") as file:
        content = file.read()

    content = content.replace(old_text, new_text)
   
    with open(file_path, "w") as file:
        file.write(content)

replace_text_in_file("C:/Users/okuopu637/desktop/file manipulation/script.txt", "and", "Die Hard")

def read_file(file_path):
    with open(file_path, "r") as file:
        content= file.read()
        return content

a = read_file("C:/Users/okuopu637/desktop/file manipulation/sample.txt")
list = a.split()
print(len(list))