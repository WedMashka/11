

list_name_for_survey =[]# лист тех кто должен пройти опрос
question1 = [] # вопрос на который нужно ответить
list_name_who_try = []# лист тех кто попытался ответить
dictionary_name_answer = {}# словарь имен кто прошел опрос с листом его ответов
choice12 = [1] # переменная положения меню
def check_int(n): # проверяет есть ли в строке цифра, вернет тру если есть
    for kk in n:
        if kk.isnumeric():
            return True
    else:
        return False


def check_name_smal_for_apped(list_n): # проверяет список имен-исключений короче 2 символа и выводит предупреждение на экран не добалены
    if len(list_n) > 0:
        str_survay = 'Не добавлен(ы): '
        str_survay2 = ' т.к. имя меньше двух символов'
        print(str_survay,str(list_n).replace('[',' ').replace(']',' '), str_survay2)

def check_name_isdigit_for_apped(list_n): # проверяет список имен-исключений содержащих цифру и выводит предупреждение на экран не добалены
    if len(list_n) > 0:
        str_survay = 'Не добавлен(ы): '
        str_survay2 = 'т.к. имя содержит цифру'
        print(str_survay,str(list_n).replace('[',' ').replace(']',' '), str_survay2)

def check_name_try_for_apped(list_n): # проверяет список имен-исключений уже прошедших опрос и выводит предупреждение на экран не добалены
    if len(list_n) > 0:
        str_survay = 'Не добавлен(ы): '
        str_survay2 = ' т.к. уже прошли опрос'
        print(str_survay,str(list_n).replace('[',' ').replace(']',' '), str_survay2)

def check_name_survey_for_apped(list_n): # проверяет список имен-исключений уже добавленных для опроса и выводит предупреждение на экран не добалены
    if len(list_n) > 0:
        str_survay = 'Не добавлен(ы): '
        str_survay2 = ' т.к. уже были в списке для опроса'
        print(str_survay,str(list_n).replace('[',' ').replace(']',' '), str_survay2)


def show_wrong_names_to_add(l_survey, l_try, l_number, l_small): # собирает ошибки при вводе и добавлении имени и выводит их
    check_name_survey_for_apped(l_survey)
    check_name_try_for_apped(l_try)
    check_name_isdigit_for_apped(l_number)
    check_name_smal_for_apped(l_small)


def check_name_try_for_dell(list_n): # проверяет список имен-исключений уже прошедших опрос и выводит предупреждение на экран не добалены
    if len(list_n) > 0:
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
        if question1:
            start_program_menu()
        else:
            enter_question()
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
    start_program_menu()

def check_answer(name_s): # проверяет ответ и добавляет его с именем в словарь
    print(question1[len(question1)-1])
    answer1 = input('Enter your answer: ')
    answer2 = answer1.split(',')
    answer3 = [] # список который в итоге добавим в словарь с ключем имя
    if len(answer2) < 1:
        print('Вы не ввели ответ на вопрос ')
        check_answer(name_s) # рекурсия
    else:
        for ans in answer2:
            ans = ans.strip()
            answer3.append(ans)
        dictionary_name_answer[name_s] = answer3 # добавляем в словарь имя и ответ
        list_name_who_try.append(name_s)
        list_name_for_survey.remove(name_s)


def survey():
    name_s = input('Enter your name: ')
    name_s = name_s.strip()
    if survey_name_check(name_s, list_name_who_try): # проверяет есть ли имя в списке тех кто уже прошел опрос
        print('You have already completed the survey')
        start_program_menu() # запускает меню пользователя
    elif survey_name_check(name_s, list_name_for_survey):# проверяю есть ли имя в списке тех кто должен пройти  опрос
        check_answer(name_s)# проверяет ответ и добавляет его с именем в словарь
        start_program_menu()
    else:
        print('Данного имени нет в списке на участие в опосе')
        start_program_menu()

def statistic_survey():
    print('Всего учавствовало в опросе : ', len(list_name_for_survey) + len(list_name_who_try), ' человек')
    print('Прошло опрос : ', len(list_name_who_try), ' человек')
    print('Не прошло опрос : ', len(list_name_for_survey), ' человек')
    statistic_list = []
    statistic_list_unique_value = []
    if len(dictionary_name_answer) > 0: # собираем список всех ответов
        for k, v in dictionary_name_answer.items():
            statistic_list.append(v)
    for val in statistic_list:  # собираем список всех уникальных ответов
        bol = False
        for val1 in statistic_list_unique_value:
            if val1 == val:
                bol = True
        if not bol:
            statistic_list_unique_value.append(val)
    for val3 in statistic_list_unique_value:
        str11 = str(val3).replace('[',' ').replace(']', ' ')
        print( str11, ' ответило ', statistic_list.count(val3), ' человек')




def admin_menu():
    choice_admin = int(input('''Добавить имена введите 5,
        Удалить имена введите 6,
        создать новый опрос  7,
        Выйти из программы 9,
        Введите число: '''))
    if choice_admin == 5 or choice_admin == 6 or choice_admin == 7 or choice_admin == 3 or choice_admin == 9:
        choice12.append(choice_admin)
    else:
        print("Не коректный ввод")
        admin_menu()


def start_program_menu():
        cho33 = input('''
            Начать опрос введите 2,
            Вывести статистику введите 3,
            Выйти в меню администратора (Там можно добавить и удалить имя) введите 4,    
            Введите цифру: ''')
        if len(cho33) > 2:
            print(' Некорректный ввод попрубуйте еще раз ')
            start_program_menu()
        elif cho33.isnumeric():
            cho = int(cho33)
            if cho == 2 or cho == 3 or cho == 4:
                choice12.append(cho)
            else:
                print(' Некорректный ввод попрубуйте еще раз ')
                start_program_menu()
        else:
            print(' Некорректный ввод попрубуйте еще раз ')
            start_program_menu()
def enter_question(): #устанавливает вопрос рекурсия если вопрос не введен
    question2 = input('Enter your question : ').strip()
    if len(question2) > 0:
        question1.append(question2)
        return True
    else:
        print("Некоректный ввод вопроса, повторите ввод вопроса")
        enter_question()

def start_program():
    append_new_name()
    # enter_question()
    while(choice12[len(choice12)-1]>=1):
        if choice12[len(choice12)-1] == 1:
            start_program_menu()
        elif choice12[len(choice12)-1] == 2:
            survey()
        elif choice12[len(choice12)-1] == 3:
            statistic_survey()
            start_program_menu()
        elif choice12[len(choice12)-1] == 4:
            admin_menu()
        elif choice12[len(choice12)-1] == 5:
            append_new_name()
        elif choice12[len(choice12)-1] == 6:
            delete_name()
        elif choice12[len(choice12)-1] == 7:
            list_name_for_survey.clear()
            list_name_who_try.clear()
            dictionary_name_answer.clear()
            choice12.append(1)
            question1.clear()
            start_program()
        elif choice12[len(choice12)-1] == 9:
            return ''
        else:
            start_program_menu()


start_program()












