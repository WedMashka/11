import json


def getNumber(): # запрашивает и возвращает число
    numberIn = input('enter your favorite number: ').strip()
    return numberIn

def writeToJsonFile(filePath, obj): # записываем объект в фаил
    with open(filePath, 'w') as OJ:
        json.dump(obj, OJ)

def readFromJson(filePath): # читаем фаил
    with open(filePath, 'r') as OJ:
        num = json.load(OJ)
        return num


FilePath = 'dataJsone.json' # путь к файлу

writeToJsonFile(FilePath, getNumber()) # запрашиваем и сохраняем число
print(' Я знаю твое любимое число! Это ' + readFromJson(FilePath)) # читаем и возвращаем результат