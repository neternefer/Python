import unittest
from emplyee import Employee

class EmployeeTest(unittest.TestCase):
	
	def setUp(self):
		self.employee = Employee("Mark", "Brown", 2300)
		
	def test_give_default_raise(self):
		self.employee.give_raise()
		
		self.assertEqual(7300, self.employee.salary)
		
	def test_give_custom_raise(self):
		self.employee.give_raise(1000)
		self.assertEqual(3300, self.employee.salary)
		
		
unittest.main()
