filePathOut = 'guest.txt'

def addNameGuest(fileOut, nameGuest):
    with open(fileOut, 'a', encoding='utf-8') as FO:
        FO.write(nameGuest + '\n')

def getGuestName(fileOut):
    nameGuest = input('Введите ваше имя:').strip()
    if len(nameGuest) > 1:
        addNameGuest(fileOut, nameGuest)
    else:
        print('Вы не ввели имя')
        getGuestName(fileOut)

for i in range(4):
    getGuestName(filePathOut)