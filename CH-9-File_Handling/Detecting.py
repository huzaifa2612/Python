# Detecting Python

# with open("CH-9-File_Handling/log.txt", "r") as f:
#     content=f.read()

# if("Python" in content):
#     print("Python is present")
# else:
#     print("Python is no present")    


# Detecting the line in which python is present

with open("CH-9-File_Handling/log.txt", "r") as f:
    lines=f.readlines()      #it stores the who text in lines but keep it sepreate line by line with /n

lineno=1
for line in lines:      # put 1st line to line
    if("Python" in line):  #checking in first line in 1st iteration
        print(f"Python is present in line {lineno}")   #print line number
        break
    lineno+=1    #counter
else:
    print("Python is not present")