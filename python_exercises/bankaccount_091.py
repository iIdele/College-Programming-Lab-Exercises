class BankAccount(object):
	account_num = 16555232
	account_type = 'General'
	
	def __init__(self, forename, surname, balance, acc_num = 0):
		self.forename = forename
		self.surname = surname
		self.balance = float(balance)
		self.acc_num = BankAccount.account_num
		BankAccount.account_num += 1
		
	def lodge(self, amount):
		self.balance += amount
	
	def withdraw(self, amount):
		if self.balance - amount >= 0:
			self.balance = self.balance - amount
		else:
			print('Insufficient funds available')
	
	def __str__(self):
		l = []
		l.append('Name: {} {}'.format(self.forename, self.surname))
		l.append('Account number: {}'.format(self.acc_num))
		l.append('Account type: {}'.format(self.account_type))
		l.append('Balance: {:.2f}'.format(self.balance))
		
		return '\n'.join(l)
	
class CurrentAccount(BankAccount):
	overdraft = -1000
	account_type = 'Current'

	def withdraw(self, amount):
		if self.balance - amount >= CurrentAccount.overdraft:
			self.balance = self.balance - amount
		else:
			print('Insufficient funds available')
	
	def __str__(self):
		l = []
		l.append(super().__str__())
		l.append('Overdraft: {:.2f}'.format(CurrentAccount.overdraft))
		
		return '\n'.join(l)

class SavingsAccount(BankAccount):
	interest_rate = 0.01
	account_type = 'Savings'
	
	def apply_interest(self):
		self.balance = self.balance + (self.balance * SavingsAccount.interest_rate)
	
	def __str__(self):
		l = []
		l.append(super().__str__())
		l.append('Interest rate: {:.2f}'.format(SavingsAccount.interest_rate))
		return '\n'.join(l)
	
def main():
	a1 = CurrentAccount('Joe', 'Murphy', 100)
	a2 = SavingsAccount('Mandy', 'Murray', 100)
	a3 = SavingsAccount('Jimmy', 'Smith', 200)
	a4 = BankAccount('Frank', 'Wrigley', 500)
	
	# Print base classes
	print('Base classes...')
	print(a1.__class__.__bases__)
	print(a2.__class__.__bases__)
	
	# Print account details
	print('Account details...')
	print(a1)
	print(a2)
	print(a3)
	print(a4)
	print('-' * 20)
	
	# Call some methods
	a1.lodge(50)
	a1.withdraw(100)
	a1.withdraw(100)
	a1.withdraw(1000)
	a2.withdraw(10)
	a2.withdraw(100)
	a2.lodge(20)
	a2.apply_interest()
	a4.lodge(20)
	a4.withdraw(20)
	a4.withdraw(1000)
	
	# Some methods should not exist
	try:
		a1.apply_interest()
	except AttributeError:
		print('No such method')
	try:
		a4.apply_interest()
	except AttributeError:
		print('No such method')
		print('-' * 20)
	
	# Print account details
	print('Account details...')
	print(a1)
	print(a2)
	print(a3)
	print(a4)

if __name__ == '__main__':
	main()
	
	
	