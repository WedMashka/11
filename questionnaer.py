

list_name_for_survey =[]# лист тех кто должен пройти опрос
question1 = input('Enter question: ')# вопрос на который нужно ответить
list_name_who_try = []# лист тех кто попытался ответить
dictionary_name_answer = {}# словарь имен кто прошел опрос с листом его ответов

def check_int(n): # проверяет есть ли в строке цифра, вернет тру если есть
    for kk in n:
        if kk.isnumeric():
            return True
    else:
        return False


def chec_name_smal(list_n): # проверяет список имен-исключений короче 2 символа и выводит предупреждение на экран не добалены
    if len(list_n)>0:
        str_survay = 'Не добавлен(ы): '
        str_survay2 = ' т.к. имя меньше двух символов'
        print(str_survay,str(list_n).replace('[',' ').replace(']',' '), str_survay2)

def chec_name_isdigit(list_n): # проверяет список имен-исключений содержащих цифру и выводит предупреждение на экран не добалены
    if len(list_n)>0:
        str_survay = 'Не добавлен(ы): '
        str_survay2 = 'т.к. имя содержит цифру'
        print(str_survay,str(list_n).replace('[',' ').replace(']',' '), str_survay2)

def chec_name_try(list_n): # проверяет список имен-исключений уже прошедших опрос и выводит предупреждение на экран не добалены
    if len(list_n)>0:
        str_survay = 'Не добавлен(ы): '
        str_survay2 = ' т.к. уже прошли опрос'
        print(str_survay,str(list_n).replace('[',' ').replace(']',' '), str_survay2)

def chec_name_survey(list_n): # проверяет список имен-исключений уже добавленных для опроса и выводит предупреждение на экран не добалены
    if len(list_n)>0:
        str_survay = 'Не добавлен(ы): '
        str_survay2 = ' т.к. уже были в списке для опроса'
        print(str_survay,str(list_n).replace('[',' ').replace(']',' '), str_survay2)


def show_wrong_names(l_survey, l_try, l_number, l_small): # собирает ошибки при вводе и добавлении имени и выводит их
    chec_name_survey(l_survey)
    chec_name_try(l_try)
    chec_name_isdigit(l_number)
    chec_name_smal(l_small)

def survey_name_check(n, list_name): # проверяет есть ли имя в списке
    res = False
    for name1 in list_name:
        if n == name1:
            res = True
            break
    return res


def append_new_name():# добавляет новые имена для опроса
    app_name = input('Enter the names who should take a survey separated by commas: ').split(',')
    list_name_already_on_list_for_survey =[] # список имен исключений т.к.  есть в списке на опрос
    list_name_already_on_list_try = [] # список имен исключений т.к.  данные имена а уже прошли опрос
    list_name_with_number = [] # список имен исключений т.к.  данные имена содежрат цифрырек
    list_small_name = [] # список имен исключений т.к.  данные имена меньше двух символов
    for n in app_name:
        n = n.strip()
        if len(n) < 2: # проверяем что имя дляинее 1 символа
            list_small_name.append(n)
        elif check_int(n): # проверяем что имя не содержит цифр
            list_name_with_number.append(n)
        elif n in list_name_for_survey:  # проверяем что имя отсутствует в списке на опрос
            list_name_already_on_list_for_survey.append(n.strip())
        elif n in list_name_who_try:  # проверяем что имя отсутствует в списке тех кто прошел опрос
            list_name_already_on_list_try.append(n.strip())
        else:
            list_name_for_survey.append(n.strip())
    show_wrong_names(list_name_already_on_list_for_survey, list_name_already_on_list_try, list_name_with_number, list_small_name)

def check_ansvwer():

def survey():
    name_s = input('Enter your name: ')
    name_s = name_s.strip()
    if survey_name_check(name_s, list_name_who_try):
        print('You have already completed the survey')
        # и запук метода который предолжит выбор возможностей
    elif survey_name_check(name_s, list_name_for_survey):
        print(question1)
        answer1 = input('Enter your answer: ')
        answer2 = answer1.split(',')
        if len(answer2) < 1:
            print('Вы не ввели ответ на вопрос ')
            # предложить выбор попробовать еще раз ответить на вопрос или выйти в главное меню
        answer3 = []
        for ans in answer2:
            ans = ans.strip()
            answer3.append(ans)









