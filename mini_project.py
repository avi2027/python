belance = input("Enter your belance : ")
belance = int(belance)

def shoping(product,price):
    product_price = f"The product price is {price}"
    print(product_price)
    global belance 
    belance = belance - price
    belance = f"You return money {belance}"
    return [product,price,belance]

return_money = shoping("Macbook", 1200)
print(return_money)
