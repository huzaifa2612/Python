name="Huzaifa"
#Slicing
sl=name[0:5] #Last Index not Included
sb=name[-7: -2]  # -1 starts form the last index
# Advance Slicing Techniques
si=name[0:]  #from 0 index to last index
sh=name[:7] # form start to 6 index (last is not included)
print(sl)
print(sb)
print(sh)
print(si)
print(name[2])

# Slicing with Skip value
z="012345678"
print(z[1:9:2]) #select from index 1 to 8 then print every 2nd number