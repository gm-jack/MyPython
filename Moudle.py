#!user/bin/env python3
# -*- coding:utf-8 -*-

# bInt = None
# aInt = int('AB34', 16)
# print(aInt)
# print(aInt is None)
# if (None):
#     print(bInt is None)
#
# print(divmod(20, 3))
# key, value = divmod(20, 3)
# l = [key, value]
# l.append('123')
# for l_value in l:
#     print(l_value)

import shelve
from datetime import datetime
from flask import Flask, request, render_template, redirect

app = Flask(__name__)
DATA_FILE = 'guestbook.dat'


def save_data(name, content, create_time):
    db = shelve.open(DATA_FILE)
    if 'greet_list' not in db:
        greet_list = []
    else:
        greet_list = db.get('greet_list')
    greet_list.insert(0, {
        'name': name,
        'content': content,
        'create_time': create_time
    })
    db['greet_list'] = greet_list
    db.close()


def get_data():
    db = shelve.open(DATA_FILE)
    if 'greet_list' not in db:
        greet_list = []
    else:
        greet_list = db.get('greet_list')
    db.close()
    return greet_list


def clear_data():
    db = shelve.open(DATA_FILE)
    db['greet_list'] = []
    db.close()


@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('main.html', greet_list=get_data())


@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    content = request.form['content']
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if name != '' and content != '':
        save_data(name, content, time)
    return render_template('main.html', greet_list=get_data())


app.run()
