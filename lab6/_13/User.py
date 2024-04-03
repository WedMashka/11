
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


class Admin(User):
    def __init__(self, first_name, last_name, gender, age, *priveleges):
        super().__init__(first_name, last_name, gender, age)
        self.priveleges = list(priveleges)

    def showPriveleges(self):
        for val in self.priveleges:
            print('Разрешено ' + val)


admin1 = Admin('Jonah', 'Smith', 'male', 32,'банить пользователей', 'удалять сообщения',
                'публиковать новости', 'редактировать профиль')
admin1.showPriveleges()