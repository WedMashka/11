from lab6._5.fileWithFunction import cars
from lab6._5.fileWithFunction import *
from lab6._5.fileWithFunction import cars as cr
print("---------------------------------------5----------------------------------------------------")


new_car = cars('VAZ', '2106', 'black', manufacturer=1992, weith=980)

for k,v in new_car.items():
    print(k, ', ', v)



new_car2 = cr('VAZ', '2106', 'black', manufacturer=1992, weith=980)

for k,v in new_car2.items():
    print(k, ', ', v)



