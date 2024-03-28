class Account():
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance

    def deposit(self, money):
        if money > 0:
            self.balance += money
            print(f'Баланс пополнен, на счету: {self.balance}')

    def withdraw(self, money):
        if self.balance < money:
            print(f'недостаточно средств')
        else:
            self.balance -= money
            print(f'Произведено снятие средств в размере {money}, на счету: {self.balance}')

    def info(self):
        print(f'Текущий баланс вашего счета: {self.balance}')

man = Account('64566', 600)

man.info()
man.withdraw(450)
man.withdraw(800)
man.deposit(2000)




