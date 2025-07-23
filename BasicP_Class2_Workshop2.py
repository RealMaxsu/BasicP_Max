distance = int(input("Enter: "))
if distance >= 5:
    if distance >= 5 and distance <= 500:
        if distance >= 5 and distance <= 300:
            if distance >= 5 and distance <= 100:
                if distance >=5 and distance <= 50:
                    print("The price is 10 baht.")
                else:
                    print("The price is 15 baht.")
            else:
                print("The price is 25 baht.")
        else:
            print("The price is 35 baht.")
    else:
        print("The price is 45 baht.")
else:
    print("The distance is too short.")

#done