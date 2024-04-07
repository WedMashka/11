from lab7._3.adminModul.Admin import Admin

testAdmin = Admin('Jonah', 'Smith', 'male', 32,'банить пользователей', 'удалять сообщения',
                'публиковать новости', 'редактировать профиль')
testAdmin.priveleges.show_priveleges()