from function import sum_total

user_input=input("Enter:").split();
# user_input = input("Enter two numbers : ")
# user_input_sum = user_input.split()
user_input = [int(num) for num in user_input]
total = sum_total(*user_input)
text = f"The total sum is {total}"
print(text)
