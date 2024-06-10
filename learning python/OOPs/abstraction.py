class car:
    def __init__(self):
        self.accelator = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.cluctch = True
        self.accelator = True
        print("Car started...")
    
car1 = car()
car1.start()


# WAP to create account class with 2 attribute balance and account number then create a method for debit(remove) and credit (Add) and print balance
class Account:
    def __init__(self, balance, accountnum):
        self.balance = balance
        self.accountnum = accountnum
    
    def debit(self, amount):
        self.balance = self.balance - amount
        print("Rs.", amount, "was debited")
        print("Total balance = ", self.get_balance())
    
    def credit(self, amount):
        self.balance = self.balance + amount
        print("Rs.", amount, "was credited")
        print("Total balance = ", self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = Account(100000, 123456789)
print(acc1.balance)
print(acc1.accountnum)
acc1.debit(20500)
acc1.credit(34000)