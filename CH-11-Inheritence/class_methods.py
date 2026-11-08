class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")  # to print the attribute of class


e = Employee()
e.a = 45

e.show()