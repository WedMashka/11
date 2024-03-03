import os

str_path = os.getcwd()  # адрес пути текущей директории
folder = 'result'
all_file = os.walk(str_path)
list_file = []
print(str_path)
for file1 in all_file:
    list_file = file1[2]
print(list_file)
if not os.path.exists(os.path.join(str_path, folder)):
    os.mkdir(os.path.join(str_path, folder))