'''
Created on Sep 15, 2019

@author: achaturvedi
'''
import unittest

from Chapter11_Testing.survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    
    def setUp(self):
        
        question = "What language did you first learn?"
        
        self.my_survey = AnonymousSurvey(question)
        
        self.responses = ['C', 'C++', 'Java']
        
    def test_store_single_response(self):
        
        self.my_survey.store_responses(self.responses[0])
        
        self.assertIn(self.responses[0], self.my_survey.responses)
            
    def test_store_three_responses(self):
        
        for response in self.responses:
            self.my_survey.store_responses(response)
            
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)   
            
unittest.main() 