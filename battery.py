

class Battery():
	def __init__(self, battery_size=70):
		self.battery_size = battery_size
		
		
	def describe_battery(self):
		print("Battery size is " + str(self.battery_size))
		
		
	def get_range(self):
		if self.battery_size == 70:
			crange = 240
		elif self.battery_size == 85:
			crange = 270
			
		message = "This car can go approx " + str(crange)
		message += " miles on a full charge."
		print(message)
		
		
	def upgrade_battery(self):
		if self.battery_size < 85:
			self.battery_size = 85
		
    
