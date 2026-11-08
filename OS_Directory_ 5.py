import os
# Specify the directory you want to list
directory_path = r"C:\Program Files"
# List all files and directories in the specified path
contents = os.listdir("directory_path")
# Print each file and directory name
for item in contents:
    print(item) 

# os Python Standard Library ka module hai jo operating system,
# files, folders aur paths ke saath interact karne mein help karta hai.
# os.listdir(path) specified folder ke andar mojood files aur directories
# ke names ki list return karta hai.