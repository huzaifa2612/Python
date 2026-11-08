#Dictionary  (Mutuable Can be Changed)  ==Unordered maps in C++
d={}# Empty Dic
marks={
    "Huzaifa": 34,
    "Wahab": 31,
    "Ahmed": 44,
    "Fahad": 0,
    0:"Maaz"
}
print(marks, type(marks))
#print(marks["Ahmed1"])  #gives error if doesnt exitst
# Difference very Important Interview point of view
print(marks.get("Wahab2"))   # Return (None) if doesnt exist
 
print(marks.items()) #Print whole Dictionary in the form of Tupple

print(marks.keys()) #print all the keys
print(marks.values())  # Print tall the values of Keys

marks.update({"Huzaifa": 99, "Niazi": 39})  #Update Value    if Update value is not exists it add in the Dic like (Niai)
print(marks)

#pop
print(marks.pop("Fahad"))  # Output: 0
print(marks)

print(marks.popitem())  # It pops out the last key-value pair and we should not have to write key in it
print(marks)

print(len(marks))  #print length