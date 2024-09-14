class Bankacc:
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance

    def deposit(self,cash_amount):
        self.balance += cash_amount
        print(f'Ваш аккаунт пополнен на {cash_amount} сумму')

    def cash(self,cash_amount):
        self.balance -=cash_amount
        print(f'С вашего счета снята {cash_amount} сумма')
    def my_balance(self):
        print(self.balance)

sasha= Bankacc('Саша')
print(sasha.balance())
