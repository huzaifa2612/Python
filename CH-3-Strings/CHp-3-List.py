friend=["apple", 1, False, "Ahmed"]
print(friend[0])     #Unlike Strings list are mutable
friend[0]="Programming"
print(friend)
print(friend[1:3])
friend.append("Mango")  # Add at the end
print(friend)

l1=[1, 4, 6, 3, 52, 23, 41, 7, 7, 7]
l1.insert(3, 4444444) #to insert at the specific index
print(l1.pop(1))  # print and pop the index

l1.remove(6) # remove the value not index
print(l1.count(7)) #Count the 7
print(l1)
l1.sort()  # Sort
l1.reverse()  # then reverse
print(l1)

print(type(l1))
l1.clear() #Delete all the values and list will be empty