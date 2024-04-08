filePathOut = 'guestBook.txt'

def addNameGuest(fileOut, nameGuest):
    with open(fileOut, 'a', encoding='utf-8') as FO:
        FO.write(nameGuest + '\n')

def getGuestName(fileOut):
    nameGuest = input('Введите ваше имя:').strip()
    if len(nameGuest) > 1:
        nameGuest = 'Приветствую вас ' + nameGuest
        print(nameGuest)
        addNameGuest(fileOut, nameGuest)
    else:
        print('Вы не ввели имя')
        getGuestName(fileOut)



while True:
    getGuestName(filePathOut)
    isExit = input(' если хотите выйти введите 1, продолжить - ентер: ').strip()
    if isExit == '1':
        break