namePath1 = 'source/articleKPI.txt'
namePath2 = 'source/articlePerfomaceonWorkPlace.txt'
namePath3 = 'source/otherText.txt'
targetW= 'the'

def counterWord(filePath, targetWord):
    count = ' Done !'
    try:
        with open(filePath, 'r', encoding='utf-8') as FileObj:
            fileItem = FileObj.read().strip()
    except FileNotFoundError:
        print(' Фаил не найден, пожалуйста проверьте правильность введенного пути')
    else:
        count = fileItem.lower().count(targetWord)

        count = f' слово {targetWord}  встречается в тексте {filePath}  {count} раз'
    finally:
        print(count)

counterWord(namePath1, targetW)
counterWord(namePath2, targetW)
counterWord(namePath3, targetW)
