from datetime import date
class Account:
    def __init__(self,name, account_num,account_balance):
        self.name = name
        self.account_num = account_num
        self.account_balance = account_balance

    def show_menu(self):
        """
        the show_menu method would return your name , current date and your account balance in a nice and amazing string format
        to implement getting current date and time you 
        """
        #print(f'{self.name} balance is {self.account_balance} as of {date.today()}')
        return f'{self.name} balance is {self.account_balance} as of {date.today()}'

    def get_balance(self):

        print(f'{self.account_balance}')
        return f'current balance is {self.account_balance}'

    def deposit(self,num):
        """
        the deposit method takes a parameter of the amount(int) to be deposited
        and returns a message(string) saying deposit successful you can thin of better messages
"""
        if num:
            total_balance = 0
            x = num + self.account_balance
            total_balance += x
            return f'deposit successful and current balance is {total_balance}'

    def withdraw(self,num):
        if num < self.account_balance:
            x = self.account_balance - num
            return f'withdrawal successful and remaining balance is {x}'
        elif num > self.account_balance:
            return "Insufficient funds"
    """
        
        the withdrawal method takes a parameter(int) of the amount to be withdrawn and 
        checks if you have sufficient funds and might decline if you don't have sufficient funds or  return a message(string) 
        saying withdrawal successful you can think of better messages or insufficient funds depending on your account balance
        takes a parameter to be 
        the withdrawal method takes a parameter(int) of the amount to be w
        withdrawn and a second parameter which is the account object which you're about to transfer to, it also checks if you have sufficient funds and might decline if you don't have sufficient funds or  return a message(string) saying transfer successful you can think of better messages or insufficient funds depending on your account balance

        The transfer made must be deducted from the balance and added to the balance of the receiving account object
"""
        
    """
    def transfer(self,num,account_num1,account_num2):
        if self.account_num.withdraw(num):
            self.account_num.deposit(num)
            return f'{self.name} transfer  is successful,remaining balance is sucessful'
    """

y = Account("chidera","432222222",5000)
x = Account('stella','55555555',6000)
print(y.account_num)
print(y.withdraw(2000))
print(y.deposit(1000))
print(y.show_menu())
print(y.get_balance())