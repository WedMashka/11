from lab7._3.userModul.User import User
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

class Admin(User):
    def __init__(self, first_name, last_name, gender, age, *priveleges):
        super().__init__(first_name, last_name, gender, age)
        self.priveleges = Priveleges(priveleges)



