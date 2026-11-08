def generateTables(n):
    tables=""
    for i in range(1, 11):
        tables+=f"{i} x {n} = {i*n}\n"

    with open(f"Tables/table_of_{n}.txt", "w") as f:
        f.write(tables)








for i in range(2, 11):
    generateTables(i)