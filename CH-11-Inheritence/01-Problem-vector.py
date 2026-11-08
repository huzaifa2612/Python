class TwoDVector:
    def __init__(self, i, j):  # Constructor
        self.i=i
        self.j=j

    def show(self):
        print(f"The value is {self.i}i + {self.j}j")

class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):    #Constructor
        super().__init__(i, j)   # Parent class ka constructor chly ga or i or j ismai initize ho jayein gy
        self.k=k    

    def show(self):
            print(f"The value is {self.i}i + {self.j}j + {self.k}k")    

a = TwoDVector(1, 2)
a.show()
b= ThreeDVector(1, 2, 3) 
b.show()       