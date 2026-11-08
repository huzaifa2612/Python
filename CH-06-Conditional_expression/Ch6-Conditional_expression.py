a=12
b=10
c=9
if(a>b and a>c):
    print("a is greater")

marks1=33
marks2=40
marks3=50

total_percentage=(100*(marks1+marks2+marks3))/300   #percentage

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("Pass", total_percentage)

else:
    print("You Failed!", total_percentage)





#Check Spam
p1="Make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this"

message=str(input("Enter your comment: "))

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This comment is spam")

else:
    print("This comment is not a spam")





#Unsername contain less than 10 characters

username=str(input("Enter your username: "))
if(len(username)<10):
    print("Your username contain less than 10 characters")
else:
    print("All is well!")    



#Check if name present in list


l = ["Harry", "Huzaifa", "Shubham", "Divya"]

name = input("Enter your name: ")

if name in l:
    print("Your name is in the list")
else:
    print("Your name is not in the list")



#Check if post is talking about huzaifa    

post = input("Enter the post: ")

if "Huzaifa".lower() in post.lower():
    print("This post is talking about huzaifa")
else:
    print("This post is not talking about huzaifa")    