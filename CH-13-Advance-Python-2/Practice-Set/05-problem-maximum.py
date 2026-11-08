from functools import reduce
a=[1, 5, 10, 242, 3, 323, 2, 3, 23, 50, 40]

def greater(a, b):
    if(a>b):
        return a
    else:
        return b

print(reduce(greater, a))
    