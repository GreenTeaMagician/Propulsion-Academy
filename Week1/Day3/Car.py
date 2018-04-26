
class Car:
	
	def __init__(self, color, tanksize, numberlaps, laplength, **kwargs):
		self.color = color
		self.tanksize = tanksize #given in liters
		self.numberlaps = numberlaps
		self.laplength = laplength # given in Km
		
	def run_laps():
		return self.tanksize - (self.laplength * 0.2)
		 
	def check_pit_stop():
		if self.tanksize < 10:
			return "Yo, you bette get sum moah gas dude. Dat fetch need fuel."
	
	
