
filePath = 'source/litreture.txt'
def cahgeLinesFile(fileIn): #принимает имя файла возвращает список измененных строк
    listChangedLines= []
    with open(fileIn, 'r', encoding='utf-8') as fileObject:
        f = fileObject.readlines()
        for line in f:
            line = line.strip()
            line = line.replace('Марины Ланда, Сергея Васильева', 'Сергея и Марины')
            listChangedLines.append(line)
    return listChangedLines

for lines in cahgeLinesFile(filePath):
    print(lines)









