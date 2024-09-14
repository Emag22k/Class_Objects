class User:
    def __init__(self,name,mail,age,number):
        self.name=name
        self.mail=mail
        self.age=age
        self.number=number

    def chane_name(self,new_name):
        self.name=new_name
    def change_number(self,new_number):
        self.number=new_number
    def chane_mail(self,new_mail):
        self.mail=new_mail

test=User('Damir','ttt@ttt',21,333777)
print(test.name)
test.chane_name('SSS')
print(test.name)
