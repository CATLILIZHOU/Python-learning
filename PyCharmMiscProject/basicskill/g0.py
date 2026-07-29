#python字典，类似于列表，但能够让你将不同的信息关联起来
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
#在python中，字典是一系列键值对。每个键都与一个值相关联，你可以使用键来访问相关联的值。
#与键相关的值可以是数、字符串、列表乃至字典
#alien_0 = {'color': 'green', 'points': 5}
alien_0['x_position'] = 0
alien_0['y_position'] = 25  #向字典中添加键值对
print(alien_0)
#修改字典中的值
alien_0['x_position'] = 1000
alien_0['y_position'] = 2000
print(alien_0)

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
 # 向右移动外星人。
 # 根据当前速度确定将外星人向右移动多远。
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

#运用del语句来删除键值对
del alien_0['speed']
print(alien_0)

#删除并非临时删除
#traceback问题可以返回一个默认的值来解决

alien_0 = {'color': 'green', 'speed':'slow'}
point_value = alien_0.get('points','No point value assigned.')
print(point_value)
#调用get()时，如果没有第二个参数且指定的键不存在，则会返回值None

user_0 = {'username':'efermi','first':'enrico','last':'fermi',}
for key, value in user_0.items():   #返回一个键值对列表
    print(f"\nKey:{key}")
    print(f"Value:{value}")

favorite_languages = {'jen':'python','sarah':'c','edward':'ruby','phil':'python'}
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll")
for language in set(favorite_languages.values()):
    print(language.title())
#在不需要使用字典中的值时，方法keys()很有用,若只对值感兴趣则使用values()
#遍历字典时，应加上item()作为一个列表的话。什么都不加会默认遍历其所有的键，只是显式地使用key()让代码更易被理解
#剔除重复项使用集合set()
#同样可直接使用一对花括号直接创建集合，并在其中用逗号分隔元素
i = {'a','b','c','a','d'}
print(i)
#容易将集合同字典混淆


