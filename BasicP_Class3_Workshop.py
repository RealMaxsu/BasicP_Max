bossVava = 20

dragSlay = 5
lightSaber = 15
badRacket = 30

for x in range(2):
    if x == 0:
        print("You're currently fighting P'Vava")
        action = int(input("Select your action:\n1 to fight\n2 to leave\nEnter your action:"))
        if action == 1:
            timeAtk = int(input("How many times you want to attack?\nEnter your action: "))
            for y in range(timeAtk):
                if y <= timeAtk:
                    weapon = int(input("What weapon do you want to use?\nWeapons that you can choose:\n1 for Dragon Slayer\n2 for Light Saber\n3 for Badminton Racket\nEnter weapon of your choice: "))
                    if weapon == 1:
                        bossVava -= dragSlay
                        if bossVava == 0:
                            print(f"Congratulation! You slayed P'Vava")
                            break
                        else:
                            bossVava += 20
                            print(f"P'Vava still survive!\nP'Vava got 20 more HP.\nNow P'Vava has {bossVava} HP.")
                            continue
                    elif weapon == 2:
                        bossVava -= lightSaber
                        if bossVava == 0:
                            print(f"Congratulation! You slayed P'Vava")
                            break
                        else:
                            bossVava += 20
                            print(f"P'Vava still survive!\nP'Vava got 20 more HP.\nNow P'Vava has {bossVava} HP.")
                            continue
                    elif weapon == 3:
                        bossVava -= badRacket
                        if bossVava == 0:
                            print(f"Congratulation! You slayed P'Vava")
                            break
                        else:
                            bossVava += 20
                            print(f"P'Vava still survive!\nP'Vava got 20 more HP.\nNow P'Vava has {bossVava} HP.")
                            continue
                    else:
                        print("Please select other number: ")
                        y -= 1
                        continue
                else:
                    print(f"P'Vava still survive with {bossVava} HP.\nYou are out of attack!")
                    break
        elif action == 2:
            print("You fled!")
            break
    elif x == 1:
        break

#done