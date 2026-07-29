rivers = {'nile':'egypt','yangtze':'china','amazon':'brazil'}
for river,country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.\n")
for river in rivers.keys():
    print(river)
for country in rivers.values():
    print(country)
favorite_languages = {'jen':'python','sarah':'c','edward':'ruby','phil':'python'}
interests = ['jen','sarah','edward','leo','jed']
for interest in interests:
    if interest in favorite_languages.keys():
        print(f"Thanks for your cooperation! {interest.title()}.")
    else:
        print(f"We need your help, {interest.title()}.")
#经常需要在列表中包含大量的字典。例如你需要给网站的每个用户都创建一个字典，并将其存储在users的列表中
pizza = {'crust':'thick','toppings':['mushrooms','extra cheese'],}
print(f"You ordered a {pizza['crust']}-crust pizza" 
      "with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")
#每当在字典中将一个键关联到多个值时，即可在字典中嵌套一个列表
#下面是字典嵌套字典
users = {'aeinstein':{'first':'albert','last':'einstein','location':'princeton',},
         'mcurie':{'first':'marie','last':'curie','location':'paris'}}
for username, user_info in users.items():
    print(f"\nUsername:{username}")
    full_name = f"{user_info['first']} {user_info['last']}"  #将作为键值对中的值的字典
    location =  user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tlocation: {location.title()}")
