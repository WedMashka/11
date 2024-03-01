def favorit_eat(*list):
    print('----------------------------------1-----------------------------------------------')

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

print('----------------------------------4-----------------------------------------------')