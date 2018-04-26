
class Car2:
	
	def __init__(self, brand, model):
		self.brand = brand
		self.model = model
		
	def start_engine(self):
		return "The " + self.brand + "engine just started"
		
	def stop_engine(self):
		return "The " + self.brand + "engine just turned off"
		
	def make_noise(self):
		return "kata-ta-ta vroom... rrrrrrrr..."

class ElectroCar(Car2):
	
	def __init__(self, brand, model):
		super().__init__(brand, model)
		self.batttery = 60
	
	def make_noise(self):
		return "..........."
		
	def recharge(self):
		return "Recharging..."
