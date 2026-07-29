sandwich_orders = ['a','b','c','d']
finished_sandwiches = []
"""
for sandwich in sandwich_orders:
    print(f"I have finished your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)
    sandwich_orders.remove(sandwich)
print(sandwich_orders)
print(finished_sandwiches)    
"""
#这一串系错误代码
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich}.")
    finished_sandwiches.append(sandwich)
print(f"\nThe following order have been finished:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwiches)
sandwich_orders = ['pastrami','vegetable','pastrami','fruit','salad','pastrami']
print('pastrami has been sold out.')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)

