# Function Definition
def avg():
    a=50
    b=100
    print((a+b)/2)


# Function Call
avg()    

def goodday(name, end="Thanks"):
    print("Goof Day, " + name)
    print(end)
    return "Bye"

a= goodday("Huzaifa", "Thank You")
goodday("Huuzzaiifa")
print(a)



def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)

n=int(input("Enter Number to Find Factorial: "))
print(f"The factorial of this number is: {factorial(n)}")