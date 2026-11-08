name="huzaifa"

print(len(name)) #prints lengtih
print(name.endswith("fa"))  #Returns True is ends with written character
print(name.startswith("Hu"))
print(name.capitalize()) # Capitalize the First Letter of first word

s="world is bad bad"
print(s.find("bad"))  #find index of character
print(s.count("a"))  #Count number of words
print(s.replace("bad", "very"))   #replace

print(name.upper())  #make all the letters uppercase
print(name.lower()) 

print(s.title()) # Make first letter Capital of every word

print(name.strip()) # Remove extra spaces
print(name.lstrip()) # Remove extra spaces of left side
print(name.rstrip()) # Remove extra spaces of right side

print(s.split()) # Divide string into list base on spaces and ,(commas)

print(" ".join(s)) # convert words of list into strings

print(name.isalpha()) # check if string has only alphabets
print(name.isdigit()) # check if string has only digits

print(name.isalnum())  #Check if string has both alphabets and numbers

#Escape Sequence Characters
v="A Lazy Fox\nJump Over\t the \"GRapes\""
print(v)

print("C:\\Users\\Ali")  # To print backslash \

print("Helloo\bX") # b remove the previous character

print("Hello\rWorld") # r move cursor

print("Hello\fWorld") # Form feed