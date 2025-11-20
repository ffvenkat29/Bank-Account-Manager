class account:

    def __init__(self,no,name,bal):
        self.acc_no = no
        self.acc_name = name
        self.acc_bal = bal
        
    def deposit(self, amount):
        if amount > 0:
            self.acc_bal += amount
            return "deposited"
        return "NotDeposited"
    
    def withdraw(self, amount):
        if amount > 500:
            self.acc_bal -= amount
            return "withdraw sucessful"
        return "withdrawl notsucessful"

acc_1 = account(9849163061,"gopi",500000)
print(acc_1.acc_name)
print(acc_1.acc_bal)
print(acc_1.acc_bal)
acc_1.deposit(5000)
print(acc_1.acc_bal)
acc_1.withdraw(400)
print(acc_1.acc_bal)
acc_1.withdraw(10000)
acc_1.withdraw(100)
print(acc_1.acc_bal)