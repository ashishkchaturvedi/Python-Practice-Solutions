'''
Created on Sep 15, 2019

@author: achaturvedi
'''
from Chapter11_Testing.survey import AnonymousSurvey

question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

my_survey.show_questions()

print("Enter 'q' to quit at any time.\n")

while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_responses(response)
    
my_survey.show_responses()