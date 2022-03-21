from flask import Flask, request
from markupsafe import escape
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello!'

@app.route("/home")
def facto():
    return render_template('fact.html',factorial='')

@app.route("/fact")
def fact():
    if request.args['input_num']:
        num = int(request.args['input_num'])
        return render_template('fact.html',factorial=str(cal_fact(num)))
    else:
        return render_template('fact.html',factorial='')

def cal_fact(N):
    if N > 0 :
        fact=1
        for i in range(1,N+1):
            fact=fact*i
        return fact
    else:
        return -1
