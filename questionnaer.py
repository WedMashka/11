

list_name_for_survey =[]# лист тех кто должен пройти опрос
question1 = False# вопрос на который нужно ответить
list_name_who_try = []# лист тех кто попытался ответить
dictionary_name_answer = {}# словарь имен кто прошел опрос с листом его ответов
choice = 1 # переменная положения меню
def check_int(n): # проверяет есть ли в строке цифра, вернет тру если есть
    for kk in n:
        if kk.isnumeric():
            return True
    else:
        return False


def check_name_smal_for_apped(list_n): # проверяет список имен-исключений короче 2 символа и выводит предупреждение на экран не добалены
    if len(list_n)>0:
        str_survay = 'Не добавлен(ы): '
        str_survay2 = ' т.к. имя меньше двух символов'
        print(str_survay,str(list_n).replace('[',' ').replace(']',' '), str_survay2)

def check_name_isdigit_for_apped(list_n): # проверяет список имен-исключений содержащих цифру и выводит предупреждение на экран не добалены
    if len(list_n)>0:
        str_survay = 'Не добавлен(ы): '
        str_survay2 = 'т.к. имя содержит цифру'
        print(str_survay,str(list_n).replace('[',' ').replace(']',' '), str_survay2)

def check_name_try_for_apped(list_n): # проверяет список имен-исключений уже прошедших опрос и выводит предупреждение на экран не добалены
    if len(list_n)>0:
        str_survay = 'Не добавлен(ы): '
        str_survay2 = ' т.к. уже прошли опрос'
        print(str_survay,str(list_n).replace('[',' ').replace(']',' '), str_survay2)

def check_name_survey_for_apped(list_n): # проверяет список имен-исключений уже добавленных для опроса и выводит предупреждение на экран не добалены
    if len(list_n)>0:
        str_survay = 'Не добавлен(ы): '
        str_survay2 = ' т.к. уже были в списке для опроса'
        print(str_survay,str(list_n).replace('[',' ').replace(']',' '), str_survay2)


def show_wrong_names_to_add(l_survey, l_try, l_number, l_small): # собирает ошибки при вводе и добавлении имени и выводит их
    check_name_survey_for_apped(l_survey)
    check_name_try_for_apped(l_try)
    check_name_isdigit_for_apped(l_number)
    check_name_smal_for_apped(l_small)


def check_name_try_for_dell(list_n): # проверяет список имен-исключений уже прошедших опрос и выводит предупреждение на экран не добалены
    if len(list_n)>0:
        str_survay = 'Не удален(ы): '
        str_survay2 = ' т.к. уже прошли опрос'
        print(str_survay,str(list_n).replace('[',' ').replace(']',' '), str_survay2)

def check_name_not_found_for_dell(list_n): # проверяет список имен-исключений уже добавленных для опроса и выводит предупреждение на экран не добалены
    if len(list_n)>0:
        str_survay = 'Не удален(ы): '
        str_survay2 = ' т.к. нет в списках тех кто должен пройти и тех кто прошел опрос'
        print(str_survay,str(list_n).replace('[',' ').replace(']',' '), str_survay2)
def show_wrong_names_to_dell(l_not_found, l_try): # собирает ошибки при вводе и имен на удаление и выводит их
    check_name_try_for_dell(l_try)
    check_name_not_found_for_dell(l_not_found)


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
            list_name_already_on_list_for_survey.append(n)
        elif n in list_name_who_try:  # проверяем что имя отсутствует в списке тех кто прошел опрос
            list_name_already_on_list_try.append(n)
        else:
            list_name_for_survey.append(n.strip())
    show_wrong_names_to_add(list_name_already_on_list_for_survey, list_name_already_on_list_try, list_name_with_number, list_small_name)
    if len(list_name_for_survey) > 0:
        return True
    else:
        append_new_name()

def delete_name():
    name_d = input('Enter the names who want to delete from list who should take a survey separated by commas: ').split(',')
    list_name_already_on_list_try = []  # список имен исключений т.к.  данные имена а уже прошли опрос
    list_name_not_found_any_where = []  # список имен исключений т.к.  данные имена а уже прошли опрос
    for n in name_d:
        n = n.strip()
        if survey_name_check(n,list_name_who_try):  # проверяем что имя отсутствует в списке на опрос
            list_name_already_on_list_try.append(n) # список имен исключений т.к.  данные имена а уже прошли опрос
        elif survey_name_check(n,list_name_for_survey):  # проверяем что имя отсутствует в списке тех кто прошел опрос
            list_name_for_survey.remove(n)
        else:
            list_name_not_found_any_where.append(n)
    show_wrong_names_to_dell(list_name_not_found_any_where, list_name_already_on_list_try)

def check_answer(name_s): # проверяет ответ и добавляет его с именем в словарь
    print(question1)
    answer1 = input('Enter your answer: ')
    answer2 = answer1.split(',')
    answer3 = [] # список который в итоге добавим в словарь
    if len(answer2) < 1:
        print('Вы не ввели ответ на вопрос ')
        # предложить выбор попробовать еще раз ответить на вопрос или выйти в главное меню
        # check_answer(name_s)
    for ans in answer2:
        ans = ans.strip()
        answer3.append(ans)
    dictionary_name_answer[name_s] = answer3


def survey():
    name_s = input('Enter your name: ')
    name_s = name_s.strip()
    if survey_name_check(name_s, list_name_who_try):
        print('You have already completed the survey')
        # и запук метода который предолжит выбор возможностей
    elif survey_name_check(name_s, list_name_for_survey):# проверяю есть ли имя в списке тех кто должен пройти  опрос
        check_answer(name_s)

def statistic_survey():
    print(list_name_for_survey)
    print(list_name_who_try)
    print(dictionary_name_answer)

def start_menu(choice):
    print()

def admin_menu():
    choice_admin = int(input('''Добавить имена введите 5,
        Удалить имена введите 6,
        создать новый опрос  7,
        Отобразить статистику 8,
        Выйти из программы 9,
        Введите число: '''))
    if choice_admin == 5:
        append_new_name()
    elif choice_admin ==6:
        delete_name()
    elif choice_admin == 7:
        print("d")
    elif choice_admin == 8:
        print("d")
    elif choice_admin == 9:
        print("d")
    else:
        print("Не коректный ввод")
        admin_menu()


def start_program_menu(cho1):
        cho = int(input('''
            Начать опрос введите 2,
            Вывести статистику введите 3,
            Выйти в меню администратора (Там можно добавить и удалить имя) введите 4,    
            Введите цифру: '''))
        if cho != 2 or cho != 3 or cho != 4:
            print(' Некорректный ввод попрубуйте еще раз ')
            start_program_menu(cho1)
        else:
            cho1 = cho
def enter_question(question): #устанавливает вопрос рекурсия если вопрос не введен
    q = False
    question2 = input('Enter your question').strip()
    if len(question2) > 0:
        question = question2
        q = True
        return q
    else:
        print("Некоректный ввод вопроса, повторите ввод вопроса")
        enter_question(question)

def start_program(choi):
    append_new_name()
    enter_question(question1)
    while(choi):
        if choi == 1:
            start_program_menu(choice)
        elif choi == 2:
            survey()

start_program(choice)












