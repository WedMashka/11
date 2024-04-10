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



def smarShowFavoriteNumber(filePath): # проверяет есть ли фаил, если нет то запросит число и сохранит в фаил потом выведет результат
    res = False
    try:
        readFromJson(filePath) # читаем фаил
    except FileNotFoundError:
        writeToJsonFile(FilePath, getNumber())  # запрашиваем и сохраняем число
        res = readFromJson(filePath)
    else:
        res = readFromJson(filePath)
    finally:
        print(' Я знаю твое любимое число! Это ' + res)  # читаем и возвращаем результат


FilePath = 'dataJsone.json' # путь к файлу

smarShowFavoriteNumber(FilePath)