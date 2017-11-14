#!user/bin/env python3
# -*- coding:utf-8 -*-
from __future__ import division
import random

age = 20
name = """哈哈哈
2222222222
3333333333"""
# end去除换行符
print('{0}ssssss {1} '.format(age, name), end='')
print('{0}ssssss {1} '.format(age, name), end='')

# 字符转编码ord()  编码转字符chr()
print(ord('A'))
# 指定编码类型
print('中文'.encode("UTF-8"))
# byte转utf-8格式
print(b'ABC'.decode('UTF-8'))
print('%f%%' % (72 / 85 * 100))

names = ['1', '2', '3']
# names = ('1', 2, 3.0)
names.pop(2)
print(names.__getitem__(1))
for nam in names:
    print('{}  '.format(nam))
x = input('x=')
if int(x) > 200:
    print(x)
elif int(x) > 100:
    print(x)
else:
    print(x)

abs(-1)


def addEnd(l=[]):
    l.append("123")
    return l


print(addEnd([]))


def add(*numbers):
    sum = 0;
    for num in numbers:
        sum += num
    return sum


print(add(1, 2))
# 字典
map = {"1": 2, "2": 3, "3": "name"}
for ds in list(map.keys()):
    print('%s - %s' % (ds, map[ds]))
    if (ds == '1'):
        del map[ds]

print(addEnd(names) is names)


class Person(object):
    def __init__(self, name):
        self.name = name

    def getName(self):
        a = 30

        def innerFoo():
            a = 20
            print(a)

        return self.name

    name = '哈哈'
    age = 20


a = Person('哈哈哈哈哈哈')
# 静态属性
Person.x = "123"
print(a.getName())
print(a.x)


# @staticmethod  表示下面的方法是静态方法
# @classmethod   表示下面的方法是类方法
class Man(Person):
    def __init__(self):
        super(Man, self).__init__('名字')
        self.height = 160

    def __getattr__(self, item):
        return item

    def prints(self):
        print('%s,%d' % (self.name, self.height))

    @staticmethod
    def sMethond(*args):
        print(args)


m = Man()
m.prints()
Man.sMethond("456")
m.sMethond("123")

"""静态方法"""  # 局部文档
# 静态方法
Man.prints(m)
try:
    print(m.__getattribute__("num").rstrip(), m.__getattr__("names").rstrip())
except:
    print('error')


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/templates')])
    return [b'<h1>Hello, web!</h1>']
