def divisible(n):
    if(n%5==0):
        return n
    False
a=[1, 5, 10, 242, 3, 323, 2, 3, 23, 50, 40]
f=list(filter(divisible, a))
print(f)