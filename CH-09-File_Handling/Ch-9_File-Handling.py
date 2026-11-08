#f=open("file.txt")
# data1=f.readline()
# print(data1, type(data1))

# data2=f.readline()
# print(data2, type(data2))     # aik line readlkrny k liye readline
                                  #sari read krny k liye readlines

# data3=f.readline()
# print(data3, type(data3))

# data4=f.readline()
# print(data4, type(data4))
# f.close()

#Using Loop

# f=open("file.txt")
# data=f.readline()
# while(data!=""):
#     print(data)
#     data=f.readline()


# Write 

# strr="I am learning python"
# fl=open("file.txt", "w")  # write
# fl.write(strr)
# fl.close()


# Append

# strr="I am Trader"
# fl=open("file.txt", "a")  # apped last pai add krna
# fl.write(strr)
# fl.close()


# With Statement to avoid .close()

with open("file.txt") as f:
    print(f.read())
# File Handling Modes


# r - open for reading

# w - open for writing

# a - open for appending

# + - open for updating

# 'rb' will open for read in binary mode.

# 'rt' will open for read in text mode.