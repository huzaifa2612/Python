class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, b):   # self is object 1 and b is object 2
        return Complex(
            self.r + b.r,
            self.i + b.i
        )

    def __mul__(self, b):   # multiply two complex objects
        real_part = (self.r * b.r) - (self.i * b.i)
        imaginary_part = (self.r * b.i) + (self.i * b.r)

        return Complex(real_part, imaginary_part)

    def __str__(self):   # object ko readable text mein dikhane ke liye
        return f"{self.r} + {self.i}i"


a = Complex(1, 2)
b = Complex(3, 4)

print("Addition:", a + b)
print("Multiplication:", a * b)