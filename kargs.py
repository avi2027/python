def student_name(first,second):
    name = f"{first} {second}"
    return name

name = student_name("Avi","Mondal")
print(name)

# student details function
def student_details(name,age,department,ID):
    details = f"Name -> {name} \nAge -> {age} \nDepartment -> {department} \nID -> {ID}"
    return details

details = student_details("Avi Mondal",24,"CSE",1558)
print(details)

# on function but multiple return 

def a_lot(num1,num2):
    add = num1 + num2
    sub = num1 - num2
    mul = num1 * num2

    return [add,sub,mul]
ans = a_lot(25,5)
print("The all answer are ->",ans)

