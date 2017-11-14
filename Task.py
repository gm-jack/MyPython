#!user/bin/env python3
# -*- coding:utf-8 -*-
import subprocess
import threading
import mysql.connector as connector

local_thread = threading.local()


def process_thread(name):
    local_thread.student = name
    print('Hello, %s (in %s)' % (local_thread.student, threading.current_thread().name))


t1 = threading.Thread(target=process_thread, args='1', name='Thread-1')
t2 = threading.Thread(target=process_thread, args='2', name='Thread-2')
t1.start()
t2.start()
t1.join()
t2.join()

conn = connector.connect(user='root', password='123456', database='test')
cursor = conn.cursor()
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])

conn.commit()
cursor.close()

cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)

cursor.close()
conn.close()


