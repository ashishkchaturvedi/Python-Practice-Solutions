'''
Created on Sep 15, 2019

@author: achaturvedi
'''
class AnonymousSurvey():
    
    def __init__(self, question):
        
        self.question = question
        self.responses = []
        
    def show_questions(self):
        
        print(self.question)
        
    def store_responses(self, new_response):
        
        self.responses.append(new_response)
        
    def show_responses(self):
        
        print("Survey Result:")
        for response in self.responses:
            print('- ' + response)
            