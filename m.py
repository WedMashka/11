import re

file = open('test2.xml', 'r')
data = file.read()
file.close()
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
ik = 0
count_login = 0
for f in date_list:
    print("*************")
    print(i)
    print(f)
    if count_login > 0 and f == '<reg:login>'+str_login+'<reg:login>':
        date_list.pop(ik)
    if count_login == 0 and f == '<reg:login>'+str_login+'<reg:login>':
        count_login = 5
    ik = ik+1

for f in date_list:
    print("*******                         ******")
    print(f)
str_res = ''.join(date_list)

new_res = re.sub(r'\t|\n|\s\s', ' ', str_res)

print("*******                         ******")
print(str_res)

print("*******                ************                         ******")
print(new_res)


f = '<?xml version="1.0" encoding="windows-1251"?>'