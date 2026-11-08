s={2, 12, 34, 12, 34, 67}
a={2, 67, 87, 89 ,0, 87, 100}

print(s.union(a))
print(s.intersection(a))
print(s-a)

y = {1, 2}
z = {1, 2, 3, 4}     #Y is subset of z 

print(y.issubset(z))