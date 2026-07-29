#测试，使用unittest中的工具来测试代码
import unittest
from basicskill.n0 import get_formatted_name
class NameTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('john', 'doe')
        self.assertEqual(formatted_name, 'John Doe')
#以上使用了该类最有用的功能：断言方法
#将formatted_name的值与字符串jon doe相比较，若相同万事大吉，若不同请知会一声
#方法名必须以test_打头
if __name__ == '__main__':
    unittest.main()
#断言方法归类
#assertEqual(a,b）核实a==b
#assertNotEqual（a,b)核实a!=b
#assertTrue(x)核实x为True
#assertFalse(x)核实x为False
#assertIn(item,list)核实item在list中
#assertNotIn(item,list)核实item不在list中
class AnonymousSurvey:
    def __init__(self,question):
        self.question = question
        self.responses = []
    def show_questions(self):
        print(self.question)
    def show_responses(self,new_response):
        self.responses.append(new_response)
    def show_results(self):
        print("Survey result:")
        for response in self.responses:
            print(f"-{response}")
