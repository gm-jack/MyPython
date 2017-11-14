#!user/bin/env python3
# -*- coding:utf-8 -*-
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('home.html')


@app.route('/signin', methods=['GET'])
def signin_form():
    # return '''<form action="/signin" method="post">
    #           <p>name<input name="username"></p>
    #           <p>password<input name="password" type="password"></p>
    #           <p><button type="submit">Sign In</button></p>
    #           </form>'''
    return render_template('form.html')


@app.route('/signin', methods=['POST'])
def signin():
    # if request.form['username'] == '123' and request.form['password'] == '123':
    #     return '<h1>Hello %s</h1>' % (request.form['username'])
    # return '<h1>Bad name or password</h1>'
    name = request.form['username']
    psw = request.form['password']
    if name == '123' and psw == '123':
        return render_template('sign-ok.html', username=name)
    return render_template('form.html', message='Bad username or password', username=name)


app.run()
