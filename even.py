numbers = [10, 15, 20, 23, 30, 35, 40]

def count_even(numbers):
    count =0
    for n in numbers:
        if (n%2==0):
            count=count+1
    return count


print(count_even(numbers))