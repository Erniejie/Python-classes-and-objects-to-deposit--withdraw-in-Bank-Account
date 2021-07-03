#classes and objects to deposit/ withdraw in Bank Account

class Bank:
    def __init__(self):
        self.bal = 0
        print("The Bank Account Deposit/Widthdraw")

    def deposit(self):
        amt= float(input("Enter Amount [£] to be Deposited: "))
        self.bal = self.bal + amt
        print("Your New Account Balance is %f" % self.bal)

    def withdraw(self):
        amt = float(input("Enter Amount[£] to withdraw: "))
        if (self.bal>=amt):
            self.bal = self.bal - amt
            print("Your New Account Balance is[£]: %.3f" % self.bal)
        else:
            print("Insuficient Balance")

    def enquiry(self):
        print("Your New Account Balance is{£]: %.2f" % self.bal)


account =Bank()
account.deposit()
account.withdraw()
account.enquiry()
            


#"%.2f"%
