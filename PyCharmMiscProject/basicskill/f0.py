#编写一个for 循环，以一种方式处理列表中的大多数元素，并以另一种方式处理包含特定值的元素
cars = ['audi','bmw','saburu','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
#布尔表达式，无非就是条件测试的别名
#if conditional_test；
#   do something
requested_toppings = ['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

requested_toppings = ['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry,we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")
#到目前为止，我们对处理的每个列表都做了基本的假设，假设他们都至少包含一个元素
#在运行for循环之前确认自己的列表是否为空很重要


available_toppings = ['mushrooms','olives','green peppers','extra cheese',
                      'pepperoni','pineapple',]
requested_toppings = ['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")
#如果披萨店的原料是固定的，那么实际上你可以用元组来进行表达

