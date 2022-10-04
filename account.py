from datetime import date
"""
This is a bank application system that shows menu,gets balance,withdraws and transfers
"""
class Account:
    def __init__(self,name, account_num,account_balance):
        self.name = name
        self.account_num = account_num
        self.account_balance = account_balance
    
    def show_menu(self):
        return f'Welcome {self.name}\n\nyour Current Balance is {self.account_balance}\n\nas of {date.today()}\n'

    def get_balance(self):
        return f'Current Balance is {self.account_balance}'

    def deposit(self,num):
        self.account_balance += num
        return f'Deposit Successful and Current Balance is {self.account_balance}'

    def withdraw(self,num):
        if num < self.account_balance:
            x = self.account_balance - num
            return f'Withdrawal Successful and Current Balance:{x}'
        elif num > self.account_balance:
            return "Insufficient funds"
    
    def transfer(self,account,num):
        if self.account_balance > num:
             self.account_balance -= num
             account.account_balance += num
             return f'Transfer Successfully made to {account.name} \nYour Available Balance is {self.account_balance}'
        return f"Insufficient Funds"

chidera = Account("chidera","432222222",5000)
stella = Account('stella','55555555',6000)
print(stella.transfer(chidera,3000))
print(chidera.deposit(1000))
print(chidera.show_menu())
print(chidera.withdraw(10000))
print(chidera.transfer(stella,4000))
