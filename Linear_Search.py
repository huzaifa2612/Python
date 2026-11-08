numbers = [-12, -5, -20, -3]
largest =float('-inf')
s_lar=float('-inf')

def find_second_largest(number):
    for n in number:
        if n>largest:
            s_lar=largest
            largest=n
        elif n > s_lar and n!=largest:
            s_lar=n


    print(largest)
    print(s_lar)


find_second_largest(numbers)