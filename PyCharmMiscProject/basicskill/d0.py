players = ["michael","harry","jim","emmily","harry"]
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
#运用切片，复制列表，可创建一个列表的副本
my_foods = ['apple','banana','pizza']
friend_foods = my_foods[:]#注意，如果只是将前者赋给后者则不能得到两个列表
friend_foods.append('orange')
print(my_foods)
for my_food in my_foods:
    print(my_food)
print(friend_foods)