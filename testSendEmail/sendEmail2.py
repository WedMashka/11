import smtplib                                              # Импортируем библиотеку по работе с SMTP
import os                                                   # Функции для работы с операционной системой, не зависящие от используемой операционной системы

# Добавляем необходимые подклассы - MIME-типы
import mimetypes                                            # Импорт класса для обработки неизвестных MIME-типов, базирующихся на расширении файла
from email import encoders                                  # Импортируем энкодер
from email.mime.base import MIMEBase                        # Общий тип
from email.mime.text import MIMEText                        # Текст/HTML
from email.mime.image import MIMEImage                      # Изображения
from email.mime.audio import MIMEAudio                      # Аудио
from email.mime.multipart import MIMEMultipart              # Многокомпонентный объект


addr_from = 'vmcpoliteh@yandex.ru'                 # Адресат
addr_to = 'regulusblack1991@gmail.com'             # Получатель
password = 'hsrpibujmevmnfwg'                      # Пароль



def send_msg():
    print(1)
    msg = MIMEMultipart()  # Создаем сообщение
    msg['From'] = addr_from  # Адресат
    msg['To'] = addr_to  # Получатель
    msg['Subject'] = 'Тема сообщения987' # Тема сообщения
    body = "Текст сообщения2"
    msg.attach(MIMEText(body, 'plain'))  # Добавляем в сообщение текст

    dirPath = 'C:\\Users\\regul\\PycharmProjects\\pythonProject\\testSendEmail\\attachmets'

    for fileInDir in os.listdir(dirPath):  # извелекаем все имена файлов из директории
        # print(fileInDir)
        filename = os.path.basename(fileInDir)  # получаем имя файла с расширением
        print(filename)
        ftype0, encoders1 = mimetypes.guess_type(
            fileInDir)  # получаем тип файла, и саб тип через слешь и получаем кодировку
        print(ftype0)
        ftype, fsubtype = ftype0.split('/')  # разделяем тип и сабтип по переменным
        with open(f'{dirPath}/{filename}', 'rb') as ff:
            ffile = MIMEBase(ftype, fsubtype)
            ffile.set_payload(ff.read().strip())
            encoders.encode_base64(ffile)

    # with open('/testSendEmail/attachmets/вложение1ю.txt', 'r', encoding='utf-8') as fileObj:
    #     file = MIMEText(fileObj.read().strip())
            ffile.add_header('content-disposition', 'attachment', filename=('utf-8', '', filename))
            msg.attach(ffile)

    print(2)
    server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)  # Создаем объект SMTP
    print(3)
    try:
        server.login(addr_from, password)  # Получаем доступ
        print(4)
        server.sendmail(addr_from, addr_to, msg.as_string())  # Отправляем сообщение
        print(5)
        server.quit()  # Выходим
    except Exception as _ex:
        print(f'{_ex} \n Check your  login or password')
    print(6)
    print('Done')


send_msg()

















#
# win = tk.Tk()
# win.geometry('500x400+300+200')
# win.title('Отправить сообщение')
# win.config(bg='#2f4f4f')
# labelSubjectLine = tk.Label(win, text='Subject Line')
# labelSubjectLine.place(x=10, y=16)
# entrySubjectLine = tk.Entry(win, width=53)
# entrySubjectLine.place(x=10, y=40)
# labelTextLetter = tk.Label(win, text='Text letter')
# labelTextLetter.place(x=10, y=66)
# textLetter = tk.Text(win, width=40, height=5)
# textLetter.place(x=10, y=90)
# labelAttachment = tk.Label(win, text='Attachments')
# labelAttachment.place(x=10, y=180)
# button = tk.Button(win, text='send', command=send_msg)
# button.place(x=10, y=210)
# labelReceiver = tk.Label(win, text='Receivers(separated by comas)')
# labelReceiver.place(x=10, y=243)
# textReceiver = tk.Text(win, width=40, height=3)
# textReceiver.place(x=10, y=270)
# win.mainloop()

