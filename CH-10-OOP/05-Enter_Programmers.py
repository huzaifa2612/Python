class Programmer:
    company="Miscrosoft"

    def __init__(self, name, salary, pin):
        self.name=name
        self.salary=salary
        self.pin=pin

    def getter(s):
        print(f"Name: {s.name}\nSalary: {s.salary}\nPin: {s.pin}\n")    

programmers=[]

while True:
    print("<------Enter Programmers Data------>")
    name=input("Enter Your Name: ").strip()

    while True:
        try:
            salary=int(input("Enter Your Salary: "))
            break;
        except ValueError:
            print("Invalid Input!. Enter You Salary in Numbers")

    while True:
        try:
            pin=int(input("Enter Your PIN: "))
            break;
        except ValueError:
            print("Invalid Input!. Enter PIN in Numbers:")

    new_programmer=Programmer(name, salary, pin)
    programmers.append(new_programmer)

    choice=input("Do you want to add another Programmer? (yes/no)").lower().strip()
    if(choice!="yes"):
        break;

print("\nALL Programmers.")
for pro in programmers:
    pro.getter()        