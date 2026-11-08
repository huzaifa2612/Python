
class Employee:
    language = "Py"
    salary = 1200000    #Class Attributes

harry = Employee()
# it will give preference to Instance Attribute
harry.language = "C++"      # we can give object the new values if it is not declared in class  #Instance Attribute

print(harry.language, harry.salary)