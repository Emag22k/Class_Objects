# class Person:
#     name='Jordan'
#     age=23
#     job='programmer'


# class Oporamida:
#     def __init__(self,name,color,dpi):
#         self.name=name
#         self.color=color
#         self.dpi=dpi
#
# logitech=Oporamida('GproX2','pink',32000)
# # print(logitech.name)
# # print(vars(logitech))

class Youtube:
    def __init__(self,name,text,likes=0):
        self.name=name
        self.text=text
        self.likes=likes

    def like(self):
        print('Спасибо за оценку!')
    def next(self):
        print('Хотите посмотреть еще видео?')

project=Youtube(input('Введите ваше имя: '),input('Введите ваш коментарий: '))
print(vars(project))
project.like()
project.next()