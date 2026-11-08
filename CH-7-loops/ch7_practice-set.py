# l = ["Harry", "Soham", "Sachin", "Rahul"]

# for name in l:
#     if name.startswith("S"):
#         print(f"Hello {name}")  


# n=int(input("Enter number: "))
# for i in range(2, n):
#     if(n%i==0):
#         print("Number is not Prime")
#         break
# else:
#  print("Number is Prime")       

# n=int(input("Enter the Number: "))
# for i in range(1, n+1):
#    print(" "* (n-i), end="")
#    print("*"* (2*i-1), end="")  #dont allow to add new line
#    print("")

# z=int(input("Enter the Number: "))
# for i in range(1, z+1):
#    #print(" "* (n-i), end="")
#    print("*"* (i), end="")  #dont allow to add new line
#    print("")   

z=int(input("Enter the Number: "))
for i in range(1, z+1):
   if(i==1 or i==z):
      print("*" *z, end="")
   else:
      print("*", end="")
      print(" "* (z-2), end="")
      print("*", end="")
   print("")   