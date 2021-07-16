from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request
from datetime import datetime
import json

with open("Templates/config.json","r") as c:
    params=json.load(c)["params"]

app=Flask(__name__,template_folder="Templates")

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/python pr'
db=SQLAlchemy(app)

class Data(db.Model):
    Sr_No = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(128), nullable=False)
    Phone_no = db.Column(db.String(64), nullable=False)
    Msg = db.Column(db.String(120), nullable=False )
    email = db.Column(db.String(60), nullable=False)
    Date = db.Column(db.String(50))

@app.route("/")
def index():
    return render_template("index.html", params=params)

@app.route("/about")
def about():
    return render_template("about.html", params=params)

@app.route("/contact", methods = ['GET','POST'])
def contact():
    if(request.method=='POST'):
        name=request.form.get('name')
        email=request.form.get('email')
        phone=request.form.get('Phone_no')
        message=request.form.get('Msg')
        entry = Data(Name=name, Phone_no=phone,email=email, Msg=message, Date=datetime.now())
        db.session.add(entry)
        db.session.commit()
    return render_template("contact.html", params=params)

@app.route("/post")
def post():
    return render_template("post.html",params=params)

if (__name__=="__main__"):
    app.run(debug=True)