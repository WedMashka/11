
def getGreatUser(filePath): # Читает имя из фаила и возвращает его
    with open(filePath, 'r', encoding='utf-8') as FO:
        userName = FO.read()
        return userName

def writeNameToFile(filePath, userName):
    with open(filePath, 'w', encoding='utf-8') as FO:
        FO.write(userName)

def getName():
    userName = input('Enter user name: ').strip()
    return userName
def chekName(userName):
    print(userName + '?')
    ansver = input('yes/no: ').lower()
    if ansver == 'yes':
        return True
    else:
        return False

def mainGreatUser(filePath):
    try: # проверяем есть ли файл, если нет запрашиваем имя и записываем в фаил, если есть то проверяем верное ли там имя.
        getGreatUser(filePath)
    except FileNotFoundError:
        writeNameToFile(filePath, getName())
    else:
        userName = getGreatUser(filePath)
        if not chekName(userName):
            writeNameToFile(filePath, getName())
    finally:
        print('Hellow dear ' + getGreatUser(filePath))

FilePath = 'source/userName.txt' # путь к файлу
mainGreatUser(FilePath)

