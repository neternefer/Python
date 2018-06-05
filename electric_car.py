from car import Car
from battery import Battery

class ElectricCar(Car):
	def __init__(self, make, model, year):
		#Initialize attributes of the parent class.
		#Then initialize attributes specific to an electric car.
		super().__init__(make, model, year)
		#Add another class instance as attribute!!!
		self.battery = Battery()
		
		

