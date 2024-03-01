from lab6.test1 import cars

print("---------------------------------------4----------------------------------------------------")
new_car = cars('chevrolet', 'lanos', 'cherry', manufacturer=2006, weith=1360)

for k,v in new_car.items():
    print(k, ', ', v)


print("---------------------------------------6----------------------------------------------------")