import math

class Shape:
	def __init__(self, x, y):
		self.center = (x, y)
		
	def get_area(self):
		raise NotImplementedError

	def draw(self, screen, color, scale):
		raise NotImplementedError

class Rectangle(Shape):
	
	def __init__(self, x, y, width, height):
		super().__init__(x, y)

		self._width = width
		self._height = height

	def get_area(self):
		return self._height + self._width
	
	def draw(self, screen, color, scale):
		pygame.draw.rect(screen, color, (self.center[0] - self._width/2)*scale, (self.center[1] - self._height/2)*scale)

class Triangle(Shape):

	def __init__(self, x, y, width, height):
		super().__init__(x, y)
		self.width = width
		self.height = height

	def get_area(self):
		return ((self.width)*(self.height))/2
	
	def draw(self, screen, color, scale):
		pygame.draw.polygon(screen, color, [
											(
												(self.center[0] - self._width/2)*scale, 
												(self.center[1] - self._width/2)*scale
											), (
												(self.center[0] - self._width/2)*scale,
												(self.center[1] - self._width/2)*scale
											), (
												(self.center[0] - self._width/2)*scale,
												(self.center[1] - self._width/2)*scale)])

class Circle(Shape):
	def __init__(self, x, y, width, height):
		super().__init__(x, y)
		self._radius = x / 2

	def get_area(self):
		return (self._radius)**2 * math.pi
		
	def draw(self, screen, color, scale):
		pygame.draw.circle(screen, color, (self.center[0]*scale - self.center[1]*scale), int(self._radius*scales))
