words=["Donkey", "Bad", "Ganda"]

with open("CH-9-File_Handling/donk.txt", "r") as f:
    cntnt=f.read()

for word in words:    #jitny words han list mai utni baar loop chly fa
    cntnt=cntnt.replace(word, "#"*len(word))             #1st iteration mai first word replace ho ga  Then continues

with open("CH-9-File_Handling/donk.txt", "w") as f:
    f.write(cntnt)