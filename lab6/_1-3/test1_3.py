print('----------------------------------1-----------------------------------------------')
def favorit_eat(*list):
    food = "Рагу из: "
    for ar in list:
        food = food + ar + " "
    print(food)

favorit_eat("картофель", "лук", "помидоры")
favorit_eat("яйцо", "лук")
favorit_eat("куропатки")



print('----------------------------------2-----------------------------------------------')


print('----------------------------------3-----------------------------------------------')

def cars(brand, model, color,**dict):
    dict['brand'] = brand
    dict["model"] = model
    dict["color"] = color
    return dict
new_car = cars('chevrolet', 'lanos', 'cherry', manufacturer=2006, weith=1360)

for k,v in new_car.items():
    print(k, ', ', v)

