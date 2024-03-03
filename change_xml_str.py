import os.path

str_path = os.getcwd()
def edit_file_xml(file_name_for_edit, str_path1): # принимает имя файла и его текщий каталог, создает в егокаталоге папку ресулт1 и вставляет туда отредактированный фаил
    file = open(os.path.join(str_path1, file_name_for_edit), 'r', encoding="windows-1251")
    data = file.read()
    file.close() # закрывем чтение т.к. уже сохранили результат чтения в переменную
    data = data.replace('trusted-ipilist="0" ', '').replace('allow-trusted-ip-only="0" ', '') # удалили атрибуты c ip
    if data.__contains__('<reg:login'):
        index_start = data.find('<reg:login')# индекс начало первого тега логин
        index_end = data.find('type="business"/>')+17 # индекс конеца первого тега логин
        index_login_start = data.find('<reg:login login="')+18 # индекс начало логина в теге логин
        index_login_end = data.find('" type="business"/>')#  индекс конеца логина в теге логин
        str_for_del = data[index_start:index_end] # сырой тег логин
        str_login = data[index_login_start:index_login_end] # логин
        new_tag_login = '*<reg:login>'+str_login+'</reg:login>*'  # тег логин нового образца, который применим в xml, по краям применяем звездочки для того что бы в дальнейшем было удобно создать лист с тегами логин и не логин по сепаратору *
        data = data.replace(data[index_start:index_end], new_tag_login) # меняем все старые теги логин на тег логин нового образца
        date_list = data.split('*') # создаем список, который состоит из тегов логин нового бразца и тегов не логин нового образца
        ik = 0 # индекс перебираемого элемента списка тегов логин и тегов не логин
        count_login = 0 # переменная для подсчета очередности тега логин
        for f in date_list:
            if count_login > 0 and f == '<reg:login>'+str_login+'</reg:login>':  # проверка на то элемент списка это тег логин и на то что это уже не первый такой тег
                date_list.pop(ik) # если это не первый тег логин который встречяется в списке то удаляем его
            if count_login == 0 and f == '<reg:login>'+str_login+'</reg:login>':  # проверка на то элемент списка это тег логин и на то что это первый такой тег
                count_login = 5 # повышаем на произвольную цифру тем самым обозначая что обнаруженные далее теги логин будут не первые.
            ik = ik+1
        data = ''.join(date_list) # делаем из отредактированого листа обратно строку

    while data.__contains__('\n'):
        data = data.replace('\n', '')  # удаление переноса строк
    while data.__contains__('\t'):
        data = data.replace('\t', ' ')  # удаление табуляции
    while data.__contains__('  '):
        data = data.replace('  ', ' ')  # удаление двойного пробела
    while data.__contains__('> <'):
        data = data.replace('> <', '><')  # удаление пробела между тегами
    r = open(os.path.join(str_path1, 'res', file_name_for_edit), 'w', encoding="windows-1251")  # содаем фаил куда пропишим результат
    r.write(data) #  прописываем результат в фаил
    r.close() # закрыли открытие


if not os.path.exists(os.path.join(str_path, 'res')):  # создаст папку ресулт в текущем каталоге, если ее нет
    os.mkdir(os.path.join(str_path, 'res'))

edit_file_xml('test3.xml', str_path)