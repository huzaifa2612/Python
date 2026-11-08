class Employee:

    @property     #Getter ki terah kam krta ha 
    def name(self):
        return f"{self.fname} {self.lname}"


    @name.setter   # Setter ki terah kam krta ha
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]


e = Employee()
e.a = 45

e.name = "Harry Khan"
print(e.fname, e.lname)   # we are calling both name manually
print(e.name)  # python will auto print both first and last name using getter function

