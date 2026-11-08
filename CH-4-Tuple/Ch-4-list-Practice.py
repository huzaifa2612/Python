#Input 5 Fruits
# a=[]
# for i in range(0, 5):
#     b=str(input("Enter Value of 5 Fruits: "))
#     a.insert(i, b)

# print(a)


#Input Students marks and sorted them
marks=[]

for i in range(0, 5):
    d=int(input(f"Enter Marks of Student {i+1}: "))
    marks.insert(i, d)

marks.sort()
print(marks)


#Count number of zeros
a=(7, 0, 8, 0, 0, 9)
print(a.count(0))



#Check a tuple cannot be changed
b=(1, 4, 5, 6, 7 ,4 ,4 ,3 ,3 ,3)
# b[2]="Larry "  #Gives error

print(sum(b))  # Print sum of a List or Tuple