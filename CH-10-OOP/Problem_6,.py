class Demo:
    a = 4


o = Demo()

print(o.a)  # Instance attribute nahi hai, is liye class attribute print hoga

o.a = 0     # Object ke andar naya instance attribute create ho gaya

print(o.a)  # Instance attribute print hoga

print(Demo.a)  # Class attribute ab bhi 4 hai