class Student:
    gpa=3.21
    language="Python"

    def __init__(self, gpa, language):   # Dunder Method which i sautomatically call __len __()  and __str__()
        self.gpa=gpa
        self.language=language
        print("I am creating an object")
    
    def getter(self):   # Must Object there
        print(f"Gpa is {self.gpa} and Language is {self.language}")

   
huzaifa=Student(4.00, "Python Programming")

huzaifa.getter()
