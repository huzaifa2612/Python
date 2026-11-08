# def f_to_c(f):
#     return 5 * (f - 32) / 9

# f = int(input("Enter temperature in F: "))
# c=f_to_c(f)
# print(f"{round(c, 2)} Degree C")   #rounf of to 2 decimal


# def pattern(n):
#     if(n==0):
#         return
#     print("*" *n)
#     pattern(n-1)


# n=int(input("Enter Number to print Pattern: "))
# pattern(n)

def rem(l, word):
    n=[]
    for item in l:
        if not(item==word):           
            
            n.append(item.strip(word))    #strip the word and add rest of the word to list n
    return n                
   
      






l=["Huzaifa", "Games", "Programming", "Rohan", "an"]
print(rem(l, "an"))