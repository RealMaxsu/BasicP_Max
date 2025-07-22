ask = input("Do you want to send a parcel? ")
price = 0
while ask == "y":
    if ask == "y":
        distance = int(input("Enter: "))
        if distance >= 5 and distance <= 50:
            print(f"The price is 10 Baht")
            price += 10
        elif distance >= 51 and distance <= 100:
            print(f"The price is 15 Baht")
            price += 15
        elif distance >= 101 and distance <= 300:
            print(f"The price is 25 Baht")
            price += 25
        elif distance >= 301 and distance <= 500:
            print(f"The price is 35 Baht")
            price += 35
        elif distance > 500:
            print(f"The price is 45 Baht")
            price += 45
        else:
            print(f"The distance is too short!")
        ask = input("Do you want to send more parcel? ")
    elif ask == "n":
        print(f"The total price is: {price}")

    #not done