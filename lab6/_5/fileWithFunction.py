

def cars(brand, model, color,**dict):
    dict['brand'] = brand
    dict["model"] = model
    dict["color"] = color
    return dict
new_car = cars('chevrolet', 'lanos', 'cherry', manufacturer=2006, weith=1360)


