class Student:
    def __init__(self, name, marks):
        if 0 <= marks <= 100:
            self.__marks=marks 
        else:
            raise ValueError("Marks must be between 0 and 100")      #Private Attribute
        self.name=name

    def get_marks(self):
        return self.__marks

    def set_marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self.__marks=new_marks
        else:
            print("Invalid Previous Marks Unchanged")





student = Student("Huzaifa", 99)
print(student.get_marks())

student.set_marks(58)
print(student.get_marks())

student.set_marks(150)
print(student.get_marks())

try:
    student = Student("Ali", 120)
except ValueError as e:
    print("Error:", e)




