
class User():
    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def describe_user(self):
        print(self.first_name, ', ', self.last_name, ', ',self.gender, ', ',self.age)

    def greet_user(self):
        print("Hellow ", self.first_name)

user1 = User('Сара','Коннор','женщина','39')
user3 = User('Том','Редл','мужчина','24')
user2 = User('Льюис','Хемилтон','мужчина','27')

user1.describe_user()
user1.greet_user()
print('---------------------------------------------')
user2.describe_user()
user2.greet_user()
print('---------------------------------------------')
user3.describe_user()
user3.greet_user()