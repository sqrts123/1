class BankAccount:
  bank_name = "Fred's Bank"
  num_account = 0
  BankAccount.num_account = num_account + 1

  def __init__(self, account_holder, balance):
    self.account_holder = account_holder
    self.balance = balance

  def withdraw(self, amount):
    self.balance = self.balance - 1

  @classmethod
  def display_bank_info(cls):
    print(cls, num_account)

account_1 = BankAccount("Charlie", 100)
account_2 = BankAccount("Mike", 200)
BankAccount.display_bank_info()
