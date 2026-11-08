dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}      #Agar same key dono mein ho, jaise "b", to second dictionary ki value use hoti hai,

merged = dict1 | dict2

print(merged)  # Output: {'a': 1, 'b': 3, 'c': 4}