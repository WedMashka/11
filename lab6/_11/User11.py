import random


class User11():
    def __init__(self, first_name, last_name, gender, age, login_attempts = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.login_attempts = login_attempts

    def describe_user(self):
        print(self.first_name, ', ', self.last_name, ', ', self.gender, ', ', self.age)

    def greet_user(self):
        print("Hellow ", self.first_name)

    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User11('Сара','Коннор','женщина','39')
print(user1.login_attempts)
value_try = random.randint(3,8)

for i in range(value_try):
    user1.increment_login_attempts()

print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)