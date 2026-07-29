'''import unittest
from w0 import AnonymousSurvey
class TestAnonymousSurvey(unittest.TestCase):
    def test_store_single_response(self):
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_responses('English')
        self.assertIn('English',my_survey.responses)
    def test_store_three_responses(self ):
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English','Mandarin','Spanish']
        for response in responses:
            my_survey.store_responses(response)
        for response in responses:
            self.assertIn(response,my_survey.responses)
    if __name__ == '__main__':
        unittest.main()'''

import unittest
from w0 import AnonymousSurvey
class TsetAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English','Mandarin','Spanish']
    def test_store_single_response(self):
        self.my_survey.store_responses(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)
    def test_store_three_reponses(self):
        for response in self.responses:
            self.my_survey.store_responses(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)
if __name__ == '__main__':
    unittest.main()
