class Employee:
    language = "Py"
    salary = 1200000    #Class Attributes

harry = Employee()
harry.name = "Harry"   # we can give object the new values if it is not declared in class  #Instance Attribute

print(harry.name, harry.language, harry.salary)