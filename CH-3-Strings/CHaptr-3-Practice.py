name=str(input("Enter Name: ")) #Strings are immutable  
print(f"Good Afternoon!, {name}")

Date="25-07-2026"
letter=f'''
     Dear <|{name}|>,
     You are Selected!
     <|{Date}|>
'''
print(letter)

h="Huzaifa is a  good boy"
print(h)
print(h.find("  "))
print(h.replace("  ", " "))

letter="Dear Huzaifa,\n\tThis Python Course is Nice. \nThanks!"
print(letter)