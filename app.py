from flask import Flask, render_template, request, session, redirect, flash
from flask_sqlalchemy import SQLAlchemy
import json
import os
import math
from datetime import datetime
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

with open('config.json', 'r') as c:
    params = json.load(c)["params"]

app = Flask(__name__)


app.secret_key = 'dont-tell-anyone'
app.config['UPLOAD_FOLDER'] = params['upload_location']
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///hambira.sqlite3'
#TODO:  MYSQL settings --->> change to PostgreSQL 
# local_server = True
# if(local_server):
#     app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
# else:
#     app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']


db = SQLAlchemy(app)

class Visitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer)

class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)



class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(40), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    img_file = db.Column(db.String(12), nullable=True)
    countcomm=db.Column(db.Integer, default=0)
    views=db.Column(db.Integer, default=0)



class Comments(db.Model):
    cid = db.Column(db.Integer, primary_key=True)
    postid = db.Column(db.Integer, db.ForeignKey('posts.sno'), nullable=False) 
    commentdate = db.Column(db.DateTime, nullable=True, default=datetime.now) 
    name = db.Column(db.String(50), nullable=False, unique=True)
    emailid = db.Column(db.String(65), nullable=False, unique=False)
    message = db.Column(db.String(550), nullable=False)

db.create_all()

@app.route("/profile")
def portfolio():
    return render_template('portfolio.html')

@app.route("/one")
def ig1():
    return render_template('accord_img_gallary.html')

@app.route("/two")
def ig2():
    return render_template('skew_grid.html')

@app.route("/three")
def ig3():
    return render_template('scroll_gallery.html')

@app.route("/")
def home():
    try:
        rec = db.session.query(Visitor).first()
        count_value = rec.count + 1
        rec.count = count_value
        db.session.commit()
    except :
        count_value = 1
        rec = Visitor(id=1,count = count_value)
        db.session.add(rec)
        db.session.commit()
        

    return render_template('birthday.html', params=params, visitor = count_value)






if __name__ == '__main__':
    # if params["deployment_type"] == "production":
    #     app.run(host='0.0.0.0',port=5050,debug=True)
    # else:
    app.run(host='0.0.0.0',port=5050,debug=True)
