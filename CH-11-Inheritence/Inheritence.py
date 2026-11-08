class Employee:

    def show(self):
        print(f"The name is {self.name} and salary is {self.salary}")


class Programmer(Employee):  # derived class
    print("Huzaifa")




emp1 = Employee()

emp1.name = "Huzaifa"
emp1.salary = "aik lakh"

emp1.show()