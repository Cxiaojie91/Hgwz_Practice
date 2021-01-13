# @Time    : 2020/12/31 17:00
# @Author  : chenxiaojie
# @Email   : chenxiaojie4488@cvte.com
# @File    : global.py
# @details : 全局配置

# 通过class 关键字定义一个类
#
class Person:
    # 类变量
    name = "tester"
    age = 10
    gender = "male"
    weight = 50
    def __init__(self, name, age, gender, weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight
    # def set_param(self, name, age, gender, weight):
    #     self.name = name
    #     self.age = age
    #     self.gender = gender
    #     self.weight = weight
    # def set_age(self, age):
    #     self.age = age
    def eat(self):
        print(f'{self.name} eating')
    def play(self):
        print('playing')

zs = Person('zhangsan', 18, '男',120)
zs.eat()
print(f"姓名:{zs.name}, 年龄:{zs.age}, 性别:{zs.gender}, 体重:{zs.weight}")
ls = Person('lisi', 20, '男', 148)
ls.eat()
# zs.set_param('zhangsan')
# zs.set_age(18)
print(f"姓名:{ls.name}, 年龄:{ls.age}, 性别:{ls.gender}, 体重:{ls.weight}")
