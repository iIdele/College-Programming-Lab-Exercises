class Point(object):
	
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
	
	def midpoint(self, other):
		mid_x = ((self.x + other.x)) / 2
		mid_y = ((self.y + other.y) ) / 2
		return Point(mid_x ,mid_y)
	
	def __str__(self):
		return '({:.1f}, {:.1f})'.format(self.x, self.y)	

class Circle(object):
	
	def __init__(self, centre=Point(), radius=0):
		self.centre = centre
		self.radius = radius
		
	def __add__(self, circle):
		new_x = (self.centre.x + circle.centre.x) / 2
		new_y = (self.centre.y + circle.centre.y) / 2
		new_r = (self.radius + circle.radius)
		return Circle(Point(new_x, new_y), new_r)
		
	def __str__(self):
		return 'Centre: ({:.1f}, {:.1f})\nRadius: {}'.format(self.centre.x, self.centre.y,self.radius)
	

def main():
	p1 = Point()
	p2 = Point(4,6)
	c1 = Circle(p1, 10)
	c2 = Circle(p2, 5)
	c3 = c1 + c2
	print(c3)
	
	p3 = Point(10,10)
	c4 = Circle(p3,15)
	c5 = c2 + c4
	print(c5)


if __name__ == '__main__':
	main()