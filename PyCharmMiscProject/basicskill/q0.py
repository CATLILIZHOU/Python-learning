from random import randint,choice
i = randint(1,6)
print(i)
players = ['charles','martina','michael','florence','eli']
first_up = choice(players)
print(first_up)
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())
#read()达到文件末尾会返回一个空字符串，要删除可以加上rstrip()
#如果在文件路径中直接使用反斜杠将引发错误，打两个反斜杠或者直接使用正常鞋号
#with open('text_files/filename.txt') as file_object:
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
#创建一个包含文件各行内容的列表
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())
#readlines()从文件中读取每一行并将其存储在一个列表中
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))
#写入文件，将输出写入文件，即使终端窗口关闭，这些输入也依然存在
filename = 'pi_digits.txt'
with open(filename,'a') as file_object:
    file_object.write("\nthis is pi")
#打开文件时可以指定第二个实参，‘r’读取，‘w'写入，’a'附加，‘r+’读写模式
#如果要写入的文件不存在，那么open()函数将自动创建它
#数值数据记得转化为字符串进行存储
#'w'是会覆盖原有的内容，如果不愿意的话，就采取附加模式
