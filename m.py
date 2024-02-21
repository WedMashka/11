file = open('test2.xml', 'r')
data = file.read()
print(data)
data = data.replace('trusted-ipilist="0" ','').replace('allow-trusted-ip-only="0" ','')
print(data," **********", "удалил айпи")
index_start = data.find('<reg:login')#начало первого тега логин
index_end = data.find('type="business"/>')+17#начало конец тега логин
index_login_end = data.find('" type="business"/>')#конец логина в теге логин
index_login_start = data.find('<reg:login login="')+18#начало логина в теге логин
# print(index_start,index_end,index_login_start,index_login_end)
str_for_del = data[index_start:index_end]
print(str_for_del)
str_login = data[index_login_start:index_login_end]
new_tag_login = '*<reg:login>'+str_login+'<reg:login>*'
data = data.replace(data[index_start:index_end],new_tag_login)
print(data," **********", "поменял логин")
i = data.count(new_tag_login)# сколько всего логинов документе
date_list =data.split('*')
co = 1
for word in date_list:
    if co ==1