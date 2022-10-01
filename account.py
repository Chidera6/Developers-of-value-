from datetime import date
class Account:
    def __init__(self,name, account_num,account_balance):
        self.name = name
        self.account_num = account_num
        self.account_balance = account_balance

    def show_menu(self):
        return f'Name:{self.name}\n\nBalance: {self.account_balance}\n\nDate: {date.today()}\n'

    def get_balance(self):
        return f'current balance is {self.account_balance}'

    def deposit(self,num):
        if num:
            total_balance = 0
            x = num + self.account_balance
            total_balance += x
            return f'Deposit Successful and Current Balance is {total_balance}'

    def withdraw(self,num):
        if num < self.account_balance:
            x = self.account_balance - num
            return f'Withdrawal Successful and Current Balance:{x}'
        elif num > self.account_balance:
            return "Insufficient funds"
        
    
    def transfer(self,account,num):
       x = self.withdraw(num)
       account = self.deposit(num)
       return True     

                 


y = Account("chidera","432222222",5000)
x = Account('stella','55555555',6000)

print(y.show_menu(),y.get_balance(),y.deposit(2000),y.withdraw(1000))
#print(x.account_balance)
#print(y.account_balance)
print(x.transfer(y.account_num,2000))
print(x.get_balance())
print(y.get_balance())