class Employee(object):
	
	def __init__(self, name, e_num):
		self.name = name
		self.e_num = e_num
	
	def wages(self):
		return 0
	
	def __str__(self):
		return 'Name: {}\nNumber: {}\nWages: {:.2f}'.format(self.name, self.e_num, self.wages())
		
class Manager(Employee):
	
	def __init__(self, name, e_num, salary):
		super().__init__(name, e_num)
		self.salary = salary
	
	def wages(self, weeks = 52):
		return self.salary / weeks
	

class AssemblyWorker(Employee):
	
	def __init__(self, name, e_num, hourly_rate, hours):
		super().__init__(name, e_num)
		self.hourly_rate = hourly_rate
		self.hours = hours
	
	def wages(self):
		return self.hourly_rate * self.hours

def main():

	e1 = Manager('Mary', 1, 50000)
	e2 = AssemblyWorker('Fred', 2, 15.50, 40)
	e3 = Employee('Sean', 3)
	
	print(e1)
	print(e2)
	print(e3)

if __name__ == '__main__':
	main()