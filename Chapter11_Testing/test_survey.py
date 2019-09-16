'''
Created on Sep 15, 2019

@author: achaturvedi
'''

import unittest

from Chapter11_Testing.survey import AnonymousSurvey

class TestSurvey(unittest.TestCase):
    
    def test_store_single_value(self):
        
        question = "What language did you first learn to speak?"
        
        my_survey = AnonymousSurvey(question)
        my_survey.store_responses('English')
        self.assertIn('English', my_survey.responses)
        
    def test_store_three_responses(self):
        
        question = "What language did you first learn to speak?"
        
        my_survey = AnonymousSurvey(question)
        responses = ['C', 'C++', 'Java']
        
        for response in responses:
            my_survey.store_responses(response)
            
        for response in responses:
            self.assertIn(response, my_survey.responses)
        
unittest.main()
    