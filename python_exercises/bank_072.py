class BankAccount(object):
	
	def __init__(self, balance=0):
		self.balance = balance
		
	def deposit(self, cash):
		self.balance = self.balance + cash
		
	def withdraw(self, cash):
		if self.balance - cash > -1:
			self.balance = self.balance - cash
		else:
			print('Insufficient funds available')
	
	def __str__(self):
		return 'Your current balance is: {:.2f} euro'.format(self.balance)