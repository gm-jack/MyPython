#!user/bin/env python3
# -*-coding: utf-8 -*-
import sys
import pprint
import os
import random

if (__name__ == "__main__"):
    print(dir(zip))

print(sum(i * i for i in range(10)))

num = ['1', '2', '3', '4']


def test():
    # print(i for i in num)
    # for i in num:
    #     print(i)
    yield num


# while len(num) > 0:
# nu=num.pop()
# print(test().__next__)
# test()

print(i for i in test())

pprint.pprint(pprint.__all__)
pprint.pprint(pprint.__doc__)
pprint.pprint(pprint.__file__)

mList = ['1111', '2222', '3333']
print(list(enumerate(mList)))

print(list(one.strip() for one in mList))

list = list(random.randint(0, 100) for num in range(40))
print(list)


def sumNum(l=[]):
    sum = 0;
    for num in l:
        sum += num
    return sum


sums = sumNum(list)
score = sums / len(list)
newList = sorted(list, reverse=True)
print('总和 %s , 平均  %s ' % (sums, score))
print(newList)

line1 = 'How are  you!'
lineList = [line for line in line1.split(' ') if line != '']
print(' '.join(lineList))


def funcx(*args):
    sum = 0
    for x in args:
        sum += x
    print('this is %s' % sum)


bars = {1, 2, 3, 4}
funcx(*bars)
# print(str.__doc__)
