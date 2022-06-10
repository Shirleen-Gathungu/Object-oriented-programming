


class Account:
    def __init__(self,account_number,account_name,pin_number):
        self.account_number=account_number
        self.account_name=account_name
        self.pin_number=pin_number
        self.transaction_fee=100
        self.balance=0
        self.deposits=[]
        self.withdrawal=[]

    
    def deposit(self,amount):
       if amount<=0:
        return f"Insufficent funds"
       
       else:
        self.balance+=amount
        self.deposits.append(amount)
        print(self.deposits)
    
        # return f"Hello {self.account_name} you have deposited {amount} and your balance is {self.balance}"
        

    def withdraw(self,amount):
        if  amount>self.balance:
            return f"Insufficient funds"
        elif amount<=0:
            return f"Amount must be greater than zero"
        else:
             self.balance-=amount
             self.balance-=self.transaction_fee
             self.withdrawal.append(amount)
             print(self.withdrawal)
        # return(f"Hello {self.account_name} you have withdrawn {amount} and your balance is {self.balance}")

    def deposit_statements(self):
        for deposits in self.deposits:
           print(deposits,end="\n")


    def withdrawals_statements(self):
        for withdrawals in self.withdrawal:
            print(withdrawals,end="\n")
       
    
    def current_balance(self):
        return f"Your balance is {self.balance}"