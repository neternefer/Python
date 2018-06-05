class Car():
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		
		
	def get_descriptive_name(self):
		return str(self.year) + " " + self.make.title() + " " + self.model.title()
		
		
	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")
		
		
	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back odometer!")
			
			
	def increment_odometer(self, miles):
		self.odometer_reading += miles


