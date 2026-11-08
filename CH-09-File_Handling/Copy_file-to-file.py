with open("CH-9-File_Handling/log.txt", "r") as f:
    content=f.read()

with open("CH-9-File_Handling/copying.txt", "w") as f:
    f.write(content)      # in write the data must be in string


# it will blank the file
with open("CH-9-File_Handling/copying.txt", "w") as f:
    f.write("")     