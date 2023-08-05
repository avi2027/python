#          0   1   2   3   4   5   6   7   8
numbers = [11, 22, 55, 66, 44, 55, 99, 88, 77]
print(numbers[3],numbers[-3])

# for i in range (len(numbers)):
#     print(numbers[i])

# print(print_list)
# list (start : end)
print(numbers[1:7])
print(numbers[1:7:1])
# list(start : end : step)
print(numbers[1:7:2])

#print the array
print("print the array/list",numbers[:]) # shortcut to print a list
# revers the array
print("print the reverse array/list",numbers[::-1]) #shortcut to reverse a list

# count the occurrence of 55 in the list
print("Occurrence of 55 in the list:", numbers.count(55))
# print(numbers.count(55))