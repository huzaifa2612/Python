word="Donkey"

with open("CH-9-File_Handling/donk.txt", "r") as f:
    cntnt=f.read()

nwcntnt=cntnt.replace(word, "#####")

with open("CH-9-File_Handling/donk.txt", "w") as f:
    f.write(nwcntnt)