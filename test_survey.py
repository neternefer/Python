import unittest
from survey import AnonymousSurvey

class AnonymousSurveyTest(unittest.TestCase):
	
	def setUp(self):
		q = "Language?"
		self.my_survey = AnonymousSurvey(q)
		self.responses = ["Polish", "English", "German"]
	
	def test_store_single_response(self):
		self.my_survey.store_response(self.responses[0])
		self.assertIn(self.responses[0], self.my_survey.responses)
		
	def test_store_many_responses(self):
		for response in self.responses:
			self.my_survey.store_response(response)
		for response in self.responses:
			self.assertIn(response, self.my_survey.responses)
		
	    
unittest.main()
