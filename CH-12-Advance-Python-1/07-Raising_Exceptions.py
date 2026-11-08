a = int(input("Enter a number: "))
b = int(input("Enter second number: "))

if b == 0:
    raise ZeroDivisionError(
        "Hey our program is not meant to divide numbers by zero"   # we raise error and crash program so that the developer
    )                                                              # he mad a huge mistake so that he can fix it
else:
    print(f"The division a/b is {a/b}")