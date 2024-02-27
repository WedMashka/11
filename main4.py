
list_for_test = input('enter the names separated by a space who should test: ').split(' ') # список кто должен пройти опрос
question = input('Enter question: ') # какой язык програмирования вы знаете
list_why_try_test =[]
person_and_ansver = {}

for ro in list_for_test:
    name_who_try = input('enter yor name: ')
    print(question)
    ansver_who_try = input('Enter one or some ansver separated by a space : ').split(' ')
    person_and_ansver[name_who_try] = ansver_who_try
    list_why_try_test.append(name_who_try)
    for na in list_for_test:
        if na == name_who_try:
            indexName = list_for_test.index(name_who_try)
            list_for_test.pop(indexName)
    print("Еще должны пройти опрос :", list_for_test)

list_ansvers1 = []
for name_who,list_ansv in person_and_ansver.items():
    for ansv in list_ansv:
        list_ansvers1.append(ansv)

for res in list_ansvers1:
    print( res, "ansvered", list_ansvers1.count(res))


