marks={
    "Huzaifa": 34,
    "Wahab": 31,
    "Ahmed": 44,
    "Fahad": 0,
    0:"Maaz"
}
#print(marks["Ahmed1"])  #gives error if doesnt exitst
# Difference very Important Interview point of view
print(marks.get("Wahab2"))   # Return (None) if doesnt exist


set={19, "19", 19.0}   #v,Important interview quesiton
print(set)
print(len(set))

marks={
    "Huzaifa": 34,   #agar 2 same han wo baad wala consider ho ga
    "Huzaifa": 31,
    "Ahmed": 31,   #values can be same
    "Fahad": 0,
    0:"Maaz"
}
print(marks)

#for loop with else

l = [1, 7, 8]

for item in l:
    print(item)
else:
    print("done")  # This is printed when the loop exhausts!