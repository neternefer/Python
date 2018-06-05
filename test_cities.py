import unittest
from cities import cities

class CityTest(unittest.TestCase):
	
	def test_city_country(self):
		result = "Santiago, Chile - population 0"
		self.assertEqual(result, cities("santiago", "chile"))
		
	def test_city_country_population(self):
		result = "Santiago, Chile - population 5000000" 
		self.assertEqual(result, cities("santiago", "chile", 5000000))
		
unittest.main()
