# num1 = input('Enter the first number: ').strip()
# num2 = input('Enter the second number: ').strip()

def getNumber(val):
    num = input(f'Enter the {val} number: ').strip()
    return num

def chekAndReturnNumber():
    num1 = getNumber('first')
    num2 = getNumber('second')
    try:
        result = int(num1) + int(num2)
    except ValueError: #  Ошибка  Тайп эрор возникает когда питон не может привести ожидаемый тип дпнных
        # В данном примере нужна ошибка ValueError так как мы не приводим тип данныех а передаем в функию int
        print('You did not enter number. Please try again ')
    else:
        print(result)
    finally:
        print('Done!')

chekAndReturnNumber()