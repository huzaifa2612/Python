#list
list=["apple", 1, False, "Ahmed"]    #Mutuable can be changed
print(type(list))  #Access by index       , len works in all

#tuple 
tuple=(1, 4, 5, 6, 7 ,4 ,4 ,3 ,3 ,3, "ABC")       # We cant change the tuple once it declared it remains tha same
print(type(tuple))             #Access by index         len works in all
   
#Dictionary 
Dic={
    "Huzaifa": 34,         #Access by index               len works in all
    "Wahab": 31,
    "Ahmed": 44,
    "Fahad": 0,
    0:"Maaz"}          #Dictionary  (Mutuable Can be Changed)  ==Unordered maps in C++
print(type(Dic))

#Set
Set=set()  # for empty                  len works in all
print(type(Set))            
# Main Function (set mai element repeat nhi hota)
 # ye data ko unorganize way ma store krta ha 
 #cant access by index


sett={1, 2, 3}           
print(type(sett))