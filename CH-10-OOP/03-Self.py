class Student:
    gpa=3.21
    language="Python"
    
    def getter(self):   # Must Object there
        print(f"Gpa is {self.gpa} and Language is {self.language}")

    @staticmethod 
    def greet():  # its mean we are not using any objects property and we dont neet to pass it object  
        print("Good Morning")    

huzaifa=Student()

huzaifa.greet()
huzaifa.getter()
# Python nichy waly consider krta ha is liye getter mai object dena lazmi
Student.getter(huzaifa)  # Print Same output Its a different way