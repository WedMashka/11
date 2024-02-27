colors = ["brown", "purple", "yellow", "green", "red","blue"]

for v in colors:
    if v =="green":
        print("Tree")

print("--------------------------------------------")


for v in colors:
    if v =="white":
        print("milk")
print("--------------------------------------------")



for v in colors:
    if v =="white":
        print("milk")
    elif v=="black":
        print("night")
    elif v=="yellow":
        print("sun")
    elif v=="purple":
        print("vaz")
    elif v=="blue":
        print("sky")
    elif v=="mint":
        print("sea")
    elif v=="белый":
        print("молоко")
    elif v=="черный":
        print("ночь")
    else:
        print("не совпал ни один цвет")
print("--------------------------------------------")

for v in colors:
    if v =="blue":
        print("sky")
print("--------------------------------------------")

for v in colors:
    if v =="white":
        print("milk")
    else:
        print("нет цвета")
print("--------------------------------------------")


for v in colors:
    if v =="blue":
        print("sky")
    else:
        print("нет цвета")

print(" период жизни человека--------------------------------------------")

age = 16

if age<2:
    print("младенец")
elif age>=2 and age<4:
    print("малыш")
elif age>=4 and age<13:
    print("ребенок")
elif age>=13 and age<20:
    print("подросток")
elif age>=60:
    print("пожилой человек")
elif age>=20 and age<65:
    print("взрослый")
elif age>=65:
    print("ура пенсия")
else:
    print("что-то пошло не так")


print(" список пользователей--------------------------------------------")



names = []

for inp in range(0,15):
    names.append(input())


if not names:
    print("we need to find some users")
else:
    for v in names:
        if v == "admin":
            print("Hellow ", v, ",would you like to see a status report? ")
        else:
            print("Hellow ", v, "thank you for logging in again")

print(" список уникальных имен--------------------------------------------")
names2 = ["Tom","Sam","Din","Bob","admin","Nina","Kirill","Frank","Sonya","Kim","Theodor","Mery"]

# словари



