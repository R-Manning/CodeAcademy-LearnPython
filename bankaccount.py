class BankAccount(object):
  balance = 0
  
  def __init__(self, name):
    self.name = name
    
  def __repr__(self):
    return 'Account owner: %s\nBalance: %.2f' % (self.name, self.balance)\
  
  def show_balance(self):
    print('Balance: %.2f' % (self.balance))
    
  def deposit(self, amount):
    if amount <= 0:
      print('Cannot deposit zero or less into account.')
    else:
      print('Deposited: %.2f' % (amount))
      self.balance += amount
      self.show_balance()
  def withdraw(self, amount):
    if amount > self.balance:
      print('Cannot withdraw more than current balance %.2f' % (self.balance))
    else:
      print('Withdrawn: %.2f' % (amount))
      self.balance -= amount
      self.show_balance()
      
my_account = BankAccount('Stephie')
print(my_account)
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print(my_account)
