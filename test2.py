class Customer:
	'''This class developed by mike 
	and descibes bank operations'''
	bankname = 'MYBANK'
	def __init__(self, name, balance = 0.0):
		self.name = name
		self.balance = balance
	def Deposit(self, amount):
		self.balance = self.balance + amount
		print('After deposit, balance: ', self.balance)
	def withdraw(self, amount):
		if amount > self.balance:
			print('Insufficient Funds...cannot perform this operation')
		else:
			self.balance = self.balance-amount
			print('After withdraw, balance: ', round(self.balance, 2))
print('Welcome to',Customer.bankname)
name = input('Enter your name: ')
c = Customer(name)
while True:
	print('d-Deposit \nw-withdraw \ne-exit')
	option = input('choose your option: ')
	if option.lower() == 'd':
		amount = float(input('Enter amount to deposit: '))
		c.Deposit(amount)
	elif option.lower() == 'w':
		amount = float(input('enter amount to withdraw: '))
		c.withdraw(amount)
	elif option.lower() == 'e':
		print('Thanks for banking')
		break
	else:
		print('your option is invalid... please select a valid option')

