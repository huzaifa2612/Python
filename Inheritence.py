class Person:
    def __init__(self, name):
        self.name=name

    def introduce(self):
        print(f"Name: {self.name}")


class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no=roll_no

    def display(self):
        self.introduce()
        print(f"{self.roll_no}")



s1=Student("Huzaifa", 101)

s1.display()