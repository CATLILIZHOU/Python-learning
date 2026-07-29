current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
prompt = "\nTell me something, and I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
#将变量message的初始值设置为空字符串，让首次执行while寓居有可供检查的东西
prompt = "\nTell me something, and I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program. "
active = True    #使用标志flag来进行判断
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
#运用True和False两种状态来决定该变量是否活跃
#使用break来退出循环
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit when you are finished.)"
while True:         #以while True打头的循环将不断地运行，知道遇到break语句
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue       #只是忽略余下的代码并返回循环的开头，而非直接退出循环
    print(current_number)
#应当避免无限循环，任何循环都应当由停止运行的途径