class Shape(object):
	
	def __init__(self, points):
		self.points = points
	
	def sides(self):
		pass
	
	def perimeter(self):
		pass

class Point(object):
	
	def __init__(self, x = 0, y = 0):
		self.x = float(x)
		self.y = float(y)
	
	def distance(first, other):
		return ((first.x - other.x)**2 + (first.y - other.y)**2)**0.5

class Triangle(Shape):
	
	def __init__(self, points):
		super().__init__(points)
		
	def sides(self):
		distances = []
		distances.append(Point.distance(self.points[0], self.points[1]))
		distances.append(Point.distance(self.points[1], self.points[2]))
		distances.append(Point.distance(self.points[2], self.points[0]))
		
		return distances
	
	def perimeter(self):
		a = Point.distance(self.points[0], self.points[1])
		b = Point.distance(self.points[1], self.points[2])
		c = Point.distance(self.points[2], self.points[0])
		length = a + b + c
		return length
	
	def area(self):
		a = Point.distance(self.points[0], self.points[1])
		b = Point.distance(self.points[1], self.points[2])
		c = Point.distance(self.points[2], self.points[0])
		
		s = (a + b + c) / 2
		
		A = (s * (s - a) * (s - b) * (s - c)) ** 0.5
		
		return A
	
class Square(Shape):
	
	def __init__(self, points):
		super().__init__(points)
	
	def sides(self):
		distances = []
		distances.append(Point.distance(self.points[0], self.points[1]))
		distances.append(Point.distance(self.points[1], self.points[2]))
		distances.append(Point.distance(self.points[2], self.points[3]))
		distances.append(Point.distance(self.points[3], self.points[0]))
		
		return distances
	
	def perimeter(self):
		a = Point.distance(self.points[0], self.points[1])
		length = a * 4
		return length
	
	def area(self):
		a = Point.distance(self.points[0], self.points[1])
		A = a * a
		return A
	
def main():

	t1 = Triangle([Point(0,0), Point(3,4), Point(6, 0)])
	print(t1.sides())
	print(t1.perimeter())
	print(t1.area())
	
	t2 = Triangle([Point(0,0), Point(4,0), Point(4, 3)])
	print(t2.sides())
	print(t2.perimeter())
	print(t2.area())

	s1 = Square([Point(0,0), Point(5,0), Point(5,5), Point(0,5)])
	print(s1.sides())
	print(s1.perimeter())
	print(s1.area())

if __name__ == '__main__':
	main()
