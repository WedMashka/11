from lab7._2.adminModul.Admin import Admin

testAdmin = Admin('Jonah', 'Smith', 'male', 32,'банить пользователей', 'удалять сообщения',
                'публиковать новости', 'редактировать профиль')
testAdmin.priveleges.show_priveleges()