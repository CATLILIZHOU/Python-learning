#元组，不可变的列表
#例如，如果有一个大小不应改变的矩形，可将其长度和宽度存储在一个元组中，从而确保它们是不能修改的
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
#dimensions[0]=250会报错如下
#Traceback (most recent call last):
  #File "C:\Users\李锦庭\PyCharmMiscProject\e0.py", line 6, in <module>
   # dimensions[0]=250
    #~~~~~~~~~~^^^
#TypeError: 'tuple' object does not support item assignment

#重新定义这个元组
dimensions = (200,50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400,100)
print("\nNew dimensions:")
for dimension in dimensions:
    print(dimension)         #实际上就是重新弄一个元组，将它赋给变量