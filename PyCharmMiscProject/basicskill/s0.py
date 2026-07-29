#存储数据，使用模块json
import json
numbers = [2,3,5,7,11,13]
filename = 'numbers.json'
with open(filename,'w') as f:
    json.dump(numbers,f)
#通常使用文件扩展名json来指出文件的存储格式为json格式
#使用函数json.dump()将数字列表存储在文件中
#可使用函数json.load()来加载存储在该文件中的信息
import json
filename = 'username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name?")
    with open(filename,'w') as f:
        json.dump(username,f)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome back,{username}!")