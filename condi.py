num = input("Enter a number: ")
num = int(num)

if num % 2 == 0 and num < 50:
    print("Even number!")
elif num % 2 !=0 and num<50:
    print("Odd number!")
else:
    print("Invalid number!")