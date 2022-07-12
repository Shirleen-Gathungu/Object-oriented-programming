
from datetime import datetime
from re import X


class Account:
    def __init__(self,account_number,account_name,pin_number):
        self.account_number=account_number
        self.account_name=account_name
        self.pin_number=pin_number
        self.transaction_fee=100
        self.balance=0
        self.date_time=datetime.now().strftime("%-d/%-m/%Y")
        self.full=[]
        self.loan_balance=0
        self.deposits=[]
        self.withdrawal=[]
    
    def deposit(self,amount):
        n=datetime.now()
        if amount<=0:
         return f"Insufficent funds"
       
        else:
            self.balance+=amount
            statement={"date":n,"amount":amount,"narration":f"Hello {self.account_name} you have deposited {amount} and your balance is {self.balance}"}
            self.deposits.append(statement)
            self.full.append(statement)
        print(self.deposits)
    
        # return f"Hello {self.account_name} you have deposited {amount} and your balance is {self.balance}"
        

    def withdraw(self,amount):
        n=datetime.now()
        if  amount>self.balance:
             return f"Insufficient funds"
        elif amount<=0:
            return f"Amount must be greater than zero"
        else:
            self.balance-=amount
            statement={"date":n,"amount":amount,"narration":f"Hello {self.account_name} you have withdrawn {amount} and your balance is {self.balance}"}
            self.balance-=self.transaction_fee
            self.full.append(statement)
            self.withdrawal.append(statement)
            print(self.withdrawal)
        # return(f"Hello {self.account_name} you have withdrawn {amount} and your balance is {self.balance}")
    
    def full_statement(self): 
       for states in self.full:
        date=states["date"]
        amounts=states["amount"]
        narration=states["narration"]
        print(f"{date}___________{amounts}_________{narration}")

    def borrow(self,amount):
        c=sum(self.deposits)
        loaning=(1/3)*c
        
        interest=(3/100)*amount
        if len(self.deposits)<10:
            return f"Dear {self.account_name} you can only borrow with more than ten deposits"
        elif amount<=100:
            return f"Dear {self.account_name} you have insufficient balance to take a loan"
        elif amount>loaning:
            return f"Dear{self.account_name} your loan request is greater than balance.Invalid"
        elif loaning>0:
            return f"Dear {self.account_name} you have an outstanding loan of {self.loan_balance}.Clear loan balance to take another loan"
        else:
            self.loan_balance+=amount
            self.loan_balance+=interest
            return f"You have successfully borrowed {amount} and your interest is {interest} and your loan is {self.loan}"


    def loan_repayment(self,amount):
        if amount<=0:
            return "invalid amount"
        if amount>self.loan_balance:
            remainder=amount-self.loan_balance
            self.loan_balance=0
            return f"Your loan balance is {self.loan_balance} { self.deposit(remainder)}"
        else:
            self.loan_balance-=amount
            return f"You have paid a loan of {amount} KSH and your current loan balance is {self.loan_balance} "   
    
    def transfer(self,amount,account_two,):
        if amount<=0:
            return "invalid amount"
        if amount>=self.balance:
            return "insufficient amount"
        else:
            self.balance-=amount
            # account_two.self.balance+=amount
            return f"Dear {self.account_name} you have transfered Ksh.{amount} to account {account_two}. Your new balance is {self.balance}"


    
    def deposit_statements(self):
        for deposits in self.deposits:
           print(f"Your deposits are {deposits}")


    def withdrawals_statements(self):
        for withdrawals in self.withdrawal:
            print(f"Your deposit is {withdrawals}")
       
    
    def current_balance(self):
        return  {self.balance}