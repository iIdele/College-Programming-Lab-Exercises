class Point(object):
	
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
	
	def distance(self, point):
		(x2, y2) = (point.x, point.y)
		return ( ( (self.x - x2) ** 2) + ( (self.y - y2) ** 2) ) ** 0.5
	
	def __str__(self):
		return '({:.1f}, {:.1f})'.format(self.x, self.y)

class Segment(object):
	
	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2
	
	def midpoint(self):
		mid_x = ((self.p1.x + self.p2.x)) / 2
		mid_y = ((self.p1.y + self.p2.y) ) / 2
		return (mid_x ,mid_y)
	
	def length(self):
		return self.p1.distance(self.p2)

class Circle(object):
	
	def __init__(self, centre, radius):
		self.centre = centre
		self.radius = radius
		
	def overlaps(self, circle2):
		x1,y1,r1 = self.centre.x,self.centre.y,self.radius
		x2,y2,r2 = circle2.centre.x,circle2.centre.y,circle2.radius
		return (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) < (r1 + r2) ** 2