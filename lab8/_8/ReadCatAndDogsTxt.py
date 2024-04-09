
catsFilePath = 'source/cats.txt'
dogsFilePath = 'source/dogs.txt'

def readFile(filePath):
    try:
        with open(filePath, 'r', encoding='utf-8') as FileCats:
            catsName = FileCats.read().strip()
    except FileNotFoundError:
        print(' Фаил не найден в указанном каталоге ')
    else:
        print(catsName)
    finally:
        print(' Done !')

readFile(catsFilePath)
readFile(dogsFilePath)