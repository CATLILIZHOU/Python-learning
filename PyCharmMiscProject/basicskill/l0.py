#要在遍历列表的同时对其进行修改可以使用while循环
#通过将while循环同列表和字典结合起来使用，可以手机存储并组织大量输入，供以后查看和显示
#首先创建一个待验证用户列表，和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice','brian','candace']
confirmed_users =[]
#验证每个用户直到没有未验证用户为止，并将每一个通过验证的用户转移到已验证用户的列表中
while unconfirmed_users:
    current_users = unconfirmed_users.pop()
    print(f"Verifying {current_users.title()}")
    confirmed_users.append(current_users)
#显示所有已验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users :
    print(confirmed_user.title())
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)
responses = {}
#设置一个标志指出调查是否继续
polling_active = True
while polling_active:
    #提示输入被调查者的名字和回答
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb someday?")
    #将回答存储在字典中
    responses[name] = response
    #检测是否还有人要参与调查
    repeat = input("Would you like to let another person respond? (yes/no)")
    if repeat == 'no':
        polling_active = False
#调查结束，显示结果
print("\n---Poll Results---")
for name,response in responses.items():
    print(f"{name} would like to climb {response}.")
