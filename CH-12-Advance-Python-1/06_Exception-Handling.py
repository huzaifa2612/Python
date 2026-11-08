try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except Exception as e:   # caught error ko e variable mein rakh deta hai.
    print(e)  

print("Thank You")



try:
    pass

except ZeroDivisionError:
    # Code
    pass

except TypeError:
    # Code
    pass

except:
    # Code      # All other exceptions are handled here.
    pass