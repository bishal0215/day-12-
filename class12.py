'''
class car :
    
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def showdetails(self):
        print(f"brand:{self.brand},price:{self.price}")
        
c1=car("toyota",50000000)
c1.showdetails()
'''
class bank_account:
    def __init__(self,account_holder,balance):
        self.account_holder= account_holder
        self.balance=balance

    def deposite(self,amount):
        self.balance += amount
        print(f"deposite{amount}")
    def withdraw(self,amount):
        if amount> self.balance:
            print("insuff")
        else:
            self.balance -=amount
            print(f"withdraw{amount}")
        
    def check_balance(self):
        print(f"current balance{self.balance}")
b1=bank_account("ram",6000)
b1.check_balance()
b1.deposite(500)
b1.check_balance()
b1.withdraw(100000)

    

