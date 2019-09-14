import random

class Coin(object):
	
	def __init__(self, sideup='Heads'):
		self.sideup = sideup
	
	def flip(self):
		side = random.randrange(0,2)
		if side == 0:
			self.sideup = 'Heads'
		else:
			self.sideup = 'Tails'
		
	def getstate(self):
		return self.sideup
	
	def __str__(self):
		return 'Current state : {}'.format(self.sideup)

def main():
	c = Coin()
	for i in range(10):
		c.flip()
		print(c)
	
	total = 0
	p_state = c.sideup;
	for i in range(1000):
		c.flip()
		if p_state == c.sideup == 'Heads':
			total += 1
		p_state = c.sideup
	
	print('The odds of two heads in a row is: {:.2f}'.format(total/1000))
	
if __name__ == '__main__':
	main()