from flask import Flask,render_template,request
import sqlite3
app = Flask(__name__)

@app.route('/')
def fun1():
    return "welcome to flask"


@app.route('/in',methods=['POST','GET'])
def fun2():
    if request.method=='POST':
        name=request.form['name']
        place=request.form['place']
        print(name,place)
        connection=sqlite3.connect("user.db")
        # connection.execute("create table table1 (name text,place text)")
        connection.execute("insert into table1(name,place)values(?,?)",(name,place))
        connection.commit()
    a=2024
    return render_template('index.html',data=a)

app.run()
