try:
    with open("1.txt", "r") as f:
        print(f.read())

except Exception as e:
    print(e)


try:
    with open("2.txt", "r") as f:
        print(f.read())

except Exception as e:
    print(e)



try:
    with open(r"C:\Users\dell\Desktop\Coding\Python_10_hr\CH-12-Advance-Python-1\Practice-set\3.txt", "r") as f:
        print(f.read())

except Exception as e:
    print(e)    