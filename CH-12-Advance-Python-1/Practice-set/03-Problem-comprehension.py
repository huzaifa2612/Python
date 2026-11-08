n=int(input("Enter Number to write Table: "))

table=[n*i for i in range (1, 11)]

with open("tables.txt", "a") as f:
    f.write(f"Table of {n}: {str(table)} \n")