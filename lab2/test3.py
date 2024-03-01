def make_shirt(size, text):
    print(' Size = ', size, ', text = ', text)

make_shirt('XL', ' Симсоны!!! ')
make_shirt(size='XXXL', text=' Симсоны решают!!! ')

print('------------------------------------4-----------------------------------------')
def make_shirt_fixed_size(size = 'L', text = 'I love Java'):
    print(' Size = ', size, ', text = ', text)

make_shirt_fixed_size()
make_shirt_fixed_size('XXL', text=' Симсоны все еще решают!!! ')

print('------------------------------------5-----------------------------------------')

def describe_city(city, country = 'Россия'):
    print(city, ' is in ', country)
describe_city('Бирменгем','Англия')
describe_city('Бруклин','Англия')
describe_city('Бруклин','США')
describe_city('Каракас','Венесуэлла')
describe_city('Севастополь','Украина')
describe_city('Волгоград',)
describe_city('Пенза',)
describe_city('Берлин','Германия')
describe_city('Бейрут','Йемен')
describe_city('Иерусалим','Израиль')

print('------------------------------------6-----------------------------------------')
def city_country(city, country):
    print(city,', ', country)
city_country('Бирменгем','Англия')
city_country('Бруклин','Англия')
city_country('Бруклин','США')
city_country('Каракас','Венесуэлла')
city_country('Севастополь','Украина')
city_country('Волгоград', 'Россия')
city_country('Пенза','Россия')
city_country('Берлин','Германия')
city_country('Бейрут','Йемен')
city_country('Иерусалим','Израиль')

print('------------------------------------7-----------------------------------------')

def make_mendeleev(**element):
    for k,v in element.items():
        print( 'Элемент ',k, ',имеет  ', v, 'электронов ')
    return element
el = {}
el = make_mendeleev( водород =1, гелий=2, кислород=8, фтор=9, неон=10, натрий=11, магний=12, алюминий=13, вольфрам=74,ренний=75)


print('------------------------------------8-----------------------------------------')


print('------------------------------------9-----------------------------------------')

def show_scientist(list):
    for v in list:
        print(v)

list_scientist = ['Ньютон', 'Тесла', 'Кант', 'Гегель', 'Галилей', 'Юнг', 'Попов', 'Поппер']

show_scientist(list_scientist)

print('------------------------------------10-----------------------------------------')

def make_great(list):
    new_list =[]
    for v in list:
        v = 'Великий ' + v
        new_list.append(v)
    return new_list

new_list_scientist = make_great(list_scientist)
show_scientist(new_list_scientist)

print('------------------------------------11-----------------------------------------')
show_scientist(new_list_scientist)
show_scientist(list_scientist)