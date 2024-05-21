import numpy as np
from flask import Flask, request, jsonify, render_template
import sqlite3
import numpy as np
import pandas as pd
import pickle
from feature import FeatureExtraction

app = Flask(__name__)

file = open("model_1.pkl","rb")
model = pickle.load(file)
file.close()

file = open("model_2.pkl","rb")
model1 = pickle.load(file)
file.close()


file = open("model_3.pkl","rb")
model2 = pickle.load(file)
file.close()



@app.route("/signup")
def signup():

    username = request.args.get('user','')
    name = request.args.get('name','')
    email = request.args.get('email','')
    number = request.args.get('mobile','')
    password = request.args.get('password','')
    con = sqlite3.connect('signup.db')
    cur = con.cursor()
    cur.execute("insert into `info` (`user`,`email`, `password`,`mobile`,`name`) VALUES (?, ?, ?, ?, ?)",(username,email,password,number,name))
    con.commit()
    con.close()
    return render_template("signin.html")

@app.route("/signin")
def signin():

    mail1 = request.args.get('user','')
    password1 = request.args.get('password','')
    con = sqlite3.connect('signup.db')
    cur = con.cursor()
    cur.execute("select `user`, `password` from info where `user` = ? AND `password` = ?",(mail1,password1,))
    data = cur.fetchone()

    if data == None:
        return render_template("signin.html")    

    elif mail1 == 'admin' and password1 == 'admin':
        return render_template("home.html")

    elif mail1 == str(data[0]) and password1 == str(data[1]):
        return render_template("home.html")
    else:
        return render_template("signup.html")


@app.route("/url", methods=["GET", "POST"])
def url():
    url = request.form["url"]
    
    obj = FeatureExtraction(url)
    x = np.array(obj.getFeaturesList()).reshape(1, 30)

    y_pred = model.predict(x)[0]
    print(y_pred)
    
    
    return render_template('result.html', result=y_pred)
           
   
        
        
        

@app.route("/url1", methods=["GET", "POST"])
def url1():
    url = request.form["url"]
    
    obj = FeatureExtraction(url)
    x = np.array(obj.getFeaturesList()).reshape(1, 30)

    y_pred = model1.predict(x)[0]
    print(y_pred)

    
    
    return render_template('result.html', result=y_pred)
        


@app.route("/url2", methods=["GET", "POST"])
def url2():
    url = request.form["url"]
    
    obj = FeatureExtraction(url)
    x = np.array(obj.getFeaturesList()).reshape(1, 30)

    y_pred = model1.predict(x)[0]
    print(y_pred)

    
    
    return render_template('result.html', result=y_pred)
        
        
    




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index')
def home():
    return render_template('home.html')


@app.route('/index1')
def index1():
    return render_template('index1.html')

@app.route('/index2')
def index2():
    return render_template('index2.html')

@app.route('/index3')
def index3():
    return render_template('index3.html')

@app.route('/logon')
def logon():
	return render_template('signup.html')

@app.route('/login')
def login():
	return render_template('signin.html')

@app.route('/notebook')
def notebook():
    return render_template('notebook.html')

@app.route('/notebook1')
def notebook1():
    return render_template('notebook1.html')

@app.route('/notebook2')
def notebook2():
    return render_template('notebook2.html')


if __name__ == "__main__":
    app.run(debug=True)
