class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sit(self):
        print(f'{self.name} is now sitting.')
    def roll_over(self):
        print(f"{self.name} rolled over")
#类中的函数称为方法，与前面所学函数唯一区别就是调用方法的方式
#__init__()是一个特殊方法，根据该类创建新实例的时候都会被自动陨星
my_dog = Dog('Willie',6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
my_new_car = Car('audi','a4',2019)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
#三种修改属性的方法，直接修改，通过方法进行设置，以及通过方进行递增
class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer_reading(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odoment(self,miles):
        self.odometer_reading += miles
#继承，如果编写的一个类是另一个类的特殊版本，就可以使用继承
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size = 75
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
my_tesla = ElectricCar('tesla','madel s',2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
#对于弗莱德方法，只要它不符合子类模拟的事物的行为，都可以进行重写
#为此刻在子类中定义一个与要重写的父类方法同名的方法，这样便不会考虑这个父类方法，可以理解为代码覆盖
#super()是一个特殊函数，让你呢狗狗去调用父类的方法
class Battery:
    def __init__(self,battery_size=75):
        self.battery_size = battery_size
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"THis car can go about {range} miles on a full charge.")
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()
my_tesla = ElectricCar('tesla','model s',2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
