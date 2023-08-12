from math import *

numbers = [11, 22, 33, 44, 55, 66, 77, 88, 99]
even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print("The even number of the list",even_numbers)
print("The odd number of the list",odd_numbers)

result = ceil(7.805)
print(result)

num  = lambda a: a*a
print(num(2**2)) 