class Priveleges():
    def __init__(self, *privelegesList):
        self.priveleges = []

        for v in privelegesList:
            for v2 in v:
                self.priveleges.append('Разрешено ' + v2)

    def show_priveleges(self):
        for v in self.priveleges:
            print(v)


#--------------------------------------------------------------------------------
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

#--------------------------------------------------------------------------------
class Admin(User):
    def __init__(self, first_name, last_name, gender, age, *priveleges):
        super().__init__(first_name, last_name, gender, age)
        self.priveleges = Priveleges(priveleges)



