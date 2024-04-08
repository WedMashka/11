filePathOut = 'reasons.txt'

def addReason(fileOut, reason):
    with open(fileOut, 'a', encoding='utf-8') as FO:
        FO.write(reason + '\n')

def getReason(fileOut):
    reason = input('Почему вам нравится программировать: ').strip()
    if len(reason) > 1:
        addReason(fileOut, reason)
    else:
        print('Вы не ввели причину')
        getReason(fileOut)



while True:
    getReason(filePathOut)
    isExit = input(' если хотите выйти введите 1, продолжить - ентер: ').strip()
    if isExit == '1':
        break