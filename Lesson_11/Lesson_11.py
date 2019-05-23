from datetime import datetime


# Primitive Datentypen:

some_number = 3
float_number = 4.56
string_text = "hallo"
boolean = True

# Liste:

number_list = [9, 8, 6, 7, 1]

number_list.sort()

print(number_list[3:5])

automobiles_list = ["audi", "testla", "vw"]

print(automobiles_list[2])

automobiles_list.append("honda")

print(automobiles_list)

automobiles_list.remove("vw")

print(automobiles_list)


for item in automobiles_list:
    print(item)

for item in automobiles_list:
    item = "bla"
    print(item)

shopping_list = {"milk":2, "bread":5, "egg":10, "dictionary":{"c++":5, "java": 6}, "list":[1,2,3,4,5]}

print(shopping_list)
print(shopping_list["milk"])

Uhrzeit = datetime.now().isoformat(sep = " ", timespec='minutes')
print(Uhrzeit)
