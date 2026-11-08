numbers = [12, 45, 7, 89, 23]

def find_largest(numbers):
    if len(numbers)==0:
        return
    
    largest=numbers[0]

    for n in numbers:
        if n>largest:
            largest=n

    return largest

print(find_largest(numbers))        
