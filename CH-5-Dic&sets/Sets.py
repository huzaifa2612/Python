#Set 
# to make empty set
e=set()
print(type(e))   

# Main Function (set mai element repeat nhi hota)
#cant access by index
# ye data ko unorganize way ma store krta ha 

s={1, 5, 32, 24, 5, 5, "avc"}
print(type(s))  
print(s)

#Methods
s.add(999)  # add value in set
s.remove(5)        # remove value
s.pop()    # remove the random value 
s.clear()    # Empty the set 

print(s)
print(len(s))