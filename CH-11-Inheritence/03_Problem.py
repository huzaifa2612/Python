class Employee:
    salary=234
    increment=20

    @property    # property ka kaam hota hai method ko attribute ki tarah use karna.  
    def salaryincreament(self):    # due to property this function is working as getter 
        return self.salary + self.salary * (self.increment/100)

    @salaryincreament.setter
    def salaryincreament(self, salary):
        self.increment=((salary/self.salary)-1)*100
        


a=Employee()

print(a.salaryincreament)

a.salaryincreament=280

print(a.increment)