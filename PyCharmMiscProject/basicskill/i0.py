favorite_places = {'jim':['france','china'],
                   'amy':['america','canada'],
                   'mike':['japan','russia','britain']}
for name,place in favorite_places.items():
    print(name)
    for pl in place:
        print(pl)               #应当要好好复习一下嵌套
message = input("Enter message: ")
print(message)
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!")
#使用input()，输入内容会被理解为字符串，于是我们会用int()来获取数值输入

height = input("How tall are you, in inches? ")
height = int (height)
if height >= 48:
    print("\nYou are tall enough to ride!")
else:
    print("\nYou will be able to ride when you are little older.")
#求模运算符%将两个数相除并返回余数   even_or_odd.py
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
#for循环勇于针对集合中的每个元素都执行一个代码块，而while循环则不断运行，知道指定的条件不满足为止


