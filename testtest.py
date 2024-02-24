


def check_int(n):
    for kk in n:
        if kk.isnumeric():
            return True
    else:
        return False



word = "HelloWorld0"

if check_int(word):
    print("Слово содержит числовое значение")
else:
    print("Слово не содержит числового значения")


