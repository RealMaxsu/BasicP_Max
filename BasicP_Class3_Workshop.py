bossVava = 100

dragSlay = 30
lightSaber = 15
badRacket = 99

for x in range(2):
    if x == 0:
        print("You're currently fighting P'Vava")
        action = int(input("Select your action:\n1 to fight\n2 to leave\nEnter your action:"))
        if action == 1:
            timeAtk = int(input("How many times you want to attack?\nEnter your action: "))
            for y in range(timeAtk):
                if y <= timeAtk:
                    weapon = input("What weapon do you want to use?\nEnter weapon of your choice: ")
                    if weapon == dragSlay:
                        bossVava -= 30
                        if bossVava > 0:
                            print(f"You have {y} more attack!")
                            continue
                        else:
                            print(f"Congratulation! You slayed P'Vava")
                    elif weapon == lightSaber:
                        bossVava -= 15
                        if bossVava > 0:
                            print(f"You have {y} more attack!")
                            continue
                        else:
                            print(f"Congratulation! You slayed P'Vava")
                    elif weapon == badRacket:
                        bossVava -= 99
                        if bossVava > 0:
                            print(f"You have {y} more attack!")
                            continue
                        else:
                            print(f"Congratulation! You slayed P'Vava")
                    else:
                        print("This weapon isn't available.")
                        y += 1
                        print(f"You have {y} more attack!")
                        continue
                else:
                    print(f"P'Vava still survive with {bossVava} HP.\nYou are out of attack!")
                    break
        elif action == 2:
            break
    elif x == 1:
        break

#Can simplify
#1.1 Make weapons in {}, use "if weapon in weapons:" and "bossVava -= weapons[weapon]""
#Make bosses in {}, use bosses{boss(or other variable)}
#Maybe delete {y}
#not done