tickets_amount = int(input("How many tickets?: "))
price=0

for age in range(tickets_amount):
    age = int(input("Your age: "))

def get_price(age):
    if age < 18:
        return 0
    elif 18 <= age <= 25:
        return 990
    else:
        return 1390

for price in range(tickets_amount):
    price = tickets_amount * get_price(age)
    if tickets_amount > 3:
        price = tickets_amount * get_price(age) * 0.9

print("Amount to be paid:", price)