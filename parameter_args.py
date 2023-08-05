def sum(num1,num2,num3=0):
    result = num1 + num2 + num3
    return result

numbers = input("Enter the numbers : ")
numbers_list = numbers.split()
numbers_list = [int(num) for num in numbers_list ]
total = sum(*numbers_list)
print("The sum of the all number is",total)

# this function same function but diffrent ways of argument
def sum_num(*args):
    print(args)
    total_num = 0
    for i in args:
        # print(i)
        total_num = total_num + i
    return total_num

user = input("Enter number : ")

user_input = user.split()
user_input = [int(num) for num in user_input]
total_result = sum_num(*user_input)
print("The sum of the all number is",total_result)