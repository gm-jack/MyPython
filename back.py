#!user/bin/env python3
# -*- coding: utf-8 -*-
import os, zipfile
import time
import heapq
from collections import deque
import calendar
from urllib import request, error

import pickle

basePath = 'C:\\Users\\yxy\\Desktop\\AR\\'
sourceDir = ['AR SDK\\StonesAndChips.dat', 'AR SDK\\StonesAndChips.xml']
targetDir = basePath + 'AR SDK' + "\\" + time.strftime('%Y-%m-%d-%H-%M-%S') + '.zip'
# zipCommad = zipfile.ZipFile(targetDir, 'w', zipfile.ZIP_DEFLATED)
# for pathName in sourceDir:
#     print('压缩文件目录  ' + basePath + pathName)
#     zipCommad.write(os.path.join(basePath + pathName))
# zipCommad.close()

# for path in os.listdir(basePath):
# print(path)

path = os.getcwd()
print(path)

pathList = os.listdir(basePath)
# 列表转化为堆
heapq.heapify(pathList)
print(pathList)
# 移除根节点
print(heapq.heappop(pathList))
print(pathList)

heap = []
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
heapq.heappush(heap, 3)
heapq.heappush(heap, 4)
heapq.heappush(heap, 5)
heapq.heappush(heap, 6)
heapq.heappush(heap, 7)
print(heap)

dList = deque(heap)
dList.appendleft(9)
print(dList)

print(calendar.month(2017, 9))
# 判断闰年
print(calendar.isleap(2017))
print(calendar.monthcalendar(2017, 2))


def get_url_data(url):
    page = ''
    try:
        response = request.urlopen(url)
        page = response.read().decode('utf-8')
    except error.HTTPError as e:
        print(e.code + '  ' + e.read().decode('utf-8'))
    return page

# get_url_data('http://www.itdiffer.com')
d={}
