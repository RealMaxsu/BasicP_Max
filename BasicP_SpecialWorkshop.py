member = input("Enter your member: ")
price = float(input("Enter your price: "))
date = int(input("What is day is today? "))
if member == "Gold":
    if price > 1000:
        price = price * (0.85)
    else:
        price = price * (0.9)
elif member == "Silver":
    if price > 1000:
        price = price * (0.9)
    else:
        price = price * (0.95)
else:
    price = price
if date % 2 == 0:
    price = price
else:
    if price >= 800:
        price = price * (0.95)
    else:
        price = price
if price >= 800:
    price = price
else:
    price += 50
print(f"Your total price is: {price}")

#done