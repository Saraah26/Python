class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance # private

    def get_balance(self):
        return self.__balance

    def deposit(self,amount):
        if amount > 0:
            self.__balance+= amount
        else:
            print("amount cant be negative!")

acc_1 = BankAccount('Taylor', 1000)
print(acc_1.owner)
print(acc_1.get_balance())
acc_1.deposit(-700)
print(acc_1.get_balance())