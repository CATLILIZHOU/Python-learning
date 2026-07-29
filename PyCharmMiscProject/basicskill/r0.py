#异常处理
#当你认为可能会发生错误的时候可编写一个如下的程序来处理可能引发的异常
#ZeroDivisionError错误的处理
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)
#有些只有在try模块中成功执行才需要运行的代码就放在els语句中
#FileNotFoundError异常的处理
filename = 'alice_txt'
try:
    with open(filename, encoding='utf-8') as f:   #以怎样的编码格式来读取文件,是通用编码
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    words = contents.split()  #该方法会以空格为分隔符将字符串分割为多个部分，并存储至一个列表
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")
def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:  # 以怎样的编码格式来读取文件,是通用编码
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()  # 该方法会以空格为分隔符将字符串分割为多个部分，并存储至一个列表
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")
filenames = ['alice.txt','siddhartha.txt','moby_dick.txt','little_women']
for filename in filenames:
    count_words(filename)
#count()方法可以确定特定的单词或短语在字符串中出现了多少次






