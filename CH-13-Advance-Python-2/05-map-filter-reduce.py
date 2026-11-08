from functools import reduce
# Map Example 

l=[1, 2, 3, 4 ,5, 6, 8]

square=lambda x: x*x

sqlist=map(square, l)

print(list(sqlist))


# Filter Example

def even(n):
    if (n%2==0):
        return n
    False

onlyeven=filter(even, l)

print(list(onlyeven))       



# Reduce Function

def sum(a, b):
    return a+b

redd= reduce(sum, l)
print(redd)

        