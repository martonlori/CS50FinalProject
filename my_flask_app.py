import sqlite3
from flask import Flask, render_template, g, request
import os
import bcrypt

app = Flask(__name__)


#Opening database connection

def get_db_connection():
    connection = sqlite3.connect("shoppinglist.db")
    db = connection.cursor()
    return db, connection


#Password hashing

def hash_password():
    user_password = request.form.get("password")
    salt = bcrypt.gensalt(rounds=12)
    hashed_password = bcrypt.hashpw(user_password.encode('utf-8'), salt) 
    return hashed_password   



@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")

@app.route("/shoppinglist", methods=["GET"])
def shoppinglist():
    return render_template("shoppinglist.html")

@app.route("/shoppingmate", methods=["GET"])
def shoppingmate():
    return render_template("shoppingmate.html")

@app.route("/signup",methods=["GET"])
def signup():
    return render_template("signup.html")

@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html")

@app.route("/register", methods=["POST"])
def register():
    db, connection = get_db_connection()
    #commit on connection
    #close on connection
    hashed_password_bytestring = hash_password() #Get user password, hash it with adding salt, return it as hashed_password
    hashed_password = hashed_password_bytestring.decode('utf-8')
    username = request.form.get("username") #Get username from form
    print(username, hashed_password)
    db.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    connection.commit()
    connection.close()
    return render_template ("/")

