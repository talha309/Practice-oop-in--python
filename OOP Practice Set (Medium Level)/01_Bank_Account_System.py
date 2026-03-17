class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if (amount > 0):
            self.__balance += amount
            print("Rs.",amount,"was Deposit.")
            print("Total Balance is Rs =",self.get_balance())
        else:
            print("invalid deposit amount.")
        
        

    def withdraw(self, amount):
        if(amount > self.balance): # if balance is less than withdraw then show messsage.
            return "Insufficient balance!"
        elif (amount <= 0):
            return "INvalid withdraw Amount."
        else:
            self.__balance -= amount
            print("Rs.",amount,"was Withdraw.")
            print("Total Balance is Rs =",self.get_balance()) 


acc1 = BankAccount("Anas",90000)
print ("Total Balance in account is =",acc1.get_balance())
acc1.deposit(342352)
acc1.withdraw(500)


        