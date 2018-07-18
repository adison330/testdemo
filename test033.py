#! /usr/bin/env python
class Car():

    def __init__(self, make, model, year):
    #初始化描述汽车的属性
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 55

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
     #打印一条指出汽车里程的消息
     print("This car has " + str(self.odometer_reading) + " miles on it. \n")

    def updata_odometer(self, mileage):
        """
        将里程表的数值设置为制定的数值，禁止回调
        :param mileage:
        :return:
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def  increment_odometer(self, miles):
        self.odometer_reading += miles

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

#my_new_car.odometer_reading = 19533
#my_new_car.read_odometer()

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(300)
my_used_car.read_odometer()