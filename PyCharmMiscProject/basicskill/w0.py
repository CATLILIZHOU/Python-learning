class AnonymousSurvey:
    def __init__(self,question):
        self.question = question
        self.responses = []
    def show_questions(self):
        print(self.question)
    def store_responses(self,new_response):
        self.responses.append(new_response)
    def show_results(self):
        print("Survey result:")
        for response in self.responses:
            print(f"-{response}")
