
def readContentFile(fileIn):
    strContent = fileIn.read()
    strContent = strContent.strip()
    return strContent
def readLinesFile(fileIn):
    f = fileIn.readlines()
    for line in f:
        print(line.strip())

def readAndSaveLinesFile(fileIn, listLine):
    f = fileIn.readlines()
    for line in f:
        listLine.append(line.strip())



listLines = []
with open('source/litreture.txt','r', encoding='utf-8') as File_In:
    # print('-------------------first variant out----------------------------')
    # print(readContentFile(File_In))
    # print('------------------------second variant out-------------------------')
    # readLinesFile(File_In)
    readAndSaveLinesFile(File_In,listLines)

print('--------------------------third variant-------------------------------')
for val in listLines:
    print(val)




