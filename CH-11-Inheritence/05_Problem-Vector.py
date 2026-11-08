class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __add__(self, b):   # self is object 1 and b is object 2
        return Vector(self.i + b.i, self.j + b.j, self.k+b.k)

    def __str__(self):   # object ko readable text mein dikhane ke liye
        return f"{self.i}i + {self.j}j+ {self.k}k"


a = Vector(1, 2, 3)
b = Vector(3, 4, 1)

print("Addition:", a + b)