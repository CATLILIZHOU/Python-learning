def greet_users(names):
    for name in names:
        mag = f"Hello, {name.title()}"
        print(mag)
usernames = ['hannah','ty','margot']
greet_users(usernames)
#将列表传递给函数后，函数就可对其进行修改。在函数中做出的修改是永久性的
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['phone case','robot pendant','dodecahedron']
#英文知识：最后的单词意思是十二面体
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
#分划函数来执行不同的任务，避免将两个不同的任务写在一个函数里面
#创建列表的副本来禁止函数·修改原有的列表
def show_messages(brief_messages):
    for brief_message in brief_messages:
        print(brief_message)
def send_messages(sent_messages,brief_messages):
    while brief_messages:
        sent_message =brief_messages.pop()
        print(sent_message)
        sent_messages.append(sent_message)
brief_messages = ['bitch','fuck you','lick my ass']
sent_messages = []
show_messages(brief_messages)
send_messages(sent_messages,brief_messages[:])
print(brief_messages)
#传递任意数量的实参
def make_pizza(*toppings):
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')
#结合使用位置实参和任意数量实参时，必须在函数定义中将接纳任意数量实参的形参放在最后，并使用星号创建新元组
def make_pizza(size,*toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")
make_pizza(16,'pepperoni')
make_pizza(12,'mushroom','green peppers','extra cheese')
#任意数量的关键字实参，利用两个星号创建一个空字典
def build_profile(first,last,**user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('albert','einstein',location='princeton')
print(user_profile)
#导入整个模块，模块是扩展名为.py的文件，包括要导入到程序中的代码
import pizza
pizza.make_pizza(16, 'pepperoni')
#还可以导入模块中的特定的函数
#from module_name import function_name
from pizza import make_pizza as mp
mp(16,'pepperoni')
#使用as给函数指定别名
#也可以给模块指定别名   import module_name as mn
#给形参指定默认值时等号两边不要有空格，所有import语句应当放在文件开头
