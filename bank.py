class Account:
    def __init__(self,account_number,account_name,pin_number,balance):
        self.account_number=account_number
        self.account_name=account_name
        self.pin_number=pin_number
        self.balance=balance
    
    def deposit(self,current_amount):
        current_balance=self.balance+current_amount
        return(f"Dear {self.account_name} your new Account Balance is {current_balance}")


    def withdraw(self,current_amount2):
        current_balance2=self.balance-current_amount2
        return(f"Dear {self.account_name} your new Account Balance is {current_balance2}")

