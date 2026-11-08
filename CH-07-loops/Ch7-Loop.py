for i in range(1,6, 2):      #step size
    print(i)

i=1
while(i<6):
    print(i)
    i=i+1

list=["Huzaifa", "stocks", "Crypto", "Forex"]
for l in list:
 print(l)        


 l = [1, 7, 8]

for item in l:
    print(item)
else:
    print("done")  # This is printed when the loop exhausts!


#BReak and Contine

for i in range(100):
    if i == 34:
        break  # Exit the loop right now
    print(i)


for i in range(100):
    if i == 34:
        continue  # Skip this iteration
    print(i)    