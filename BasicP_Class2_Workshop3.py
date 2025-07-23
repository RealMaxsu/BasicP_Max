ask = input("Do you want to send a parcel? ")
if ask == "y":
    distance = int(input("Enter: "))
    if distance >= 5 and distance <= 50:
        print("The price is 10 Baht")
    elif distance >= 51 and distance <= 100:
        print("The price is 15 Baht")
    elif distance >= 101 and distance <= 300:
        print("The price is 25 Baht")
    elif distance >= 301 and distance <= 500:
        print("The price is 35 Baht")
    elif distance > 500:
        print("The price is 45 Baht")
    else:
        print("The distance is too short!")
elif ask == "n":
    print("")
else:
    print("")

#done