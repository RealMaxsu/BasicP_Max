fruitBasket = ["apple","banana","coconut"]


# print(fruitBasket[0])
# fruitBasket[0] = "avocado"
# print(fruitBasket[0])

# fruitBasket.append("dog")
# print(f"Add dog to the basket: {fruitBasket}")

# fruitBasket.pop(3)
# print(f"Remove dog from the basket: {fruitBasket}")

# for i in fruitBasket:
#     print(f"{i} is delicious!")

# selectFruit = input("Which fruit do you want to find: ")
# def findFruit(selectFruit):
#     for i in fruitBasket:
#         if i == selectFruit:
#             print(f"Found {i}")
#         else:
#             print("Not found")

# findFruit(selectFruit)

#Change print to return
# selectFruit = input("Which fruit do you want to find: ")
# def findFruit(selectFruit):
#     for i in fruitBasket:
#         if i == selectFruit:
#             return f"Found {i}"
#         else:
#             return "Not found"

# print(findFruit(selectFruit))
#not done

#-------------------------------------------------------------------------------------------------------------------
std = {"student_name":"Kanawut Duangdeeden", "student_age": 18, "student_ID": 68130500006, "student_gender": "Male"}


# print(std["ID"])
# for i in std:
#     askName = input("What is your users? ")
#     if askName == std["student_name"]:
#         print(std)
#     else:
#         print("Permission denied!")

# if std["student_age"] >= 18:
#     print("You can access information.")
#     askAcc = input("Do you want to access information?(y/n) ")
#     if askAcc == "y":
#         print(std)
#     elif askAcc == "n":
#         print("Return back to menu")
# else:
#     print("Permission denied!")

# students = [
#     {"student_name":"Max", "student_age": 18, "student_gender": "Male"},
#     {"student_name":"Atom", "student_age": 19, "student_gender": "Female"},
#     {"student_name":"Vava", "student_age": 19, "student_gender": "Male"},
#     {"student_name":"Riw", "student_age": 19, "student_gender": "Male"}
# ]

# for i in students:
#     print(i["student_name"])

# students = [{"name": "Thanasorn Dusadeeroj", "age": 19, "ID": 67130500014},
#             {"name": "satit", "age": 15, "ID": 6713050047}]
# for i in students:
#     if i["age"] >= 18:
#         print(f'{i["name"]} is old enough!')
#     else:
#         print(f'{i["name"]} is too young!')