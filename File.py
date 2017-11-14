#!user/bin/env python3
# -*-coding:utf-8-*-
import os

files = open('test.txt', 'w+')
files.write('new file second line one \nnew file second line two')
files.close()

with open('test.txt', 'r') as file:
    print(file.read())

# 获取文件状态
filestat = os.stat('test.txt')
print(filestat)

with open('test.txt', 'r') as file:
    while(True):
        line = file.readline()
        if not line:
            break
        print(line,end='')