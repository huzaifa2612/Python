f=open("CH-9-File_Handling/poem.txt")
c=f.read()
print(c)
if("Twinkle" in c):  # in complete string ke andar substring search karta hai.
    print("Twinkle is Present")
else:
    print("Not Present")

f.close()