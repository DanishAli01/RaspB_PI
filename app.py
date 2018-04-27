# -*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify
from flask_restful import Resource, Api
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None

def select_all_temp(conn):
    cur = conn.cursor()
    print("connected")
    cur.execute("SELECT * FROM temps")
    print("executed")
    return cur.fetchall()



# Making instance of Flask Class
app = Flask(__name__)


# Pinpoints the address
@app.route('/')
def index():
    # Render Templates
     return render_template("home.html")

@app.route('/home')
def home():
    # Render Templates
     return render_template("home.html")

@app.route('/about')
def about():
    # Render Templates
     return render_template("about.html")

@app.route('/plot')
def plot():
    return render_template("plot.html")

@app.route('/api/get_temp')
def temperature():
    database = "/Users/tohir/Downloads/sqlite-autoconf-3230100/project"

    # create a database connection
    conn = create_connection(database)
    with conn:
        print("2. Query all temps")
        #select_all_temp(conn)
        rows = select_all_temp(conn)

    # build data
    temp = []
    humid = []
    for row in rows:
        print(row[0])
        temp.append(row[2])
        humid.append(row[3])

    return jsonify({'name' : 'temperature', 'data': temp}, {'name' : 'Humidity', 'data' : humid})
    #return jsonify(rows)

@app.route('/Power')
def power():
    # Render Templates
     return render_template(".html")

@app.route("/Reading")
def lab_temp():
    # Render Templates with conditional statements
	humidity, temperature = 1.2, 3.2
	if humidity is not None and temperature is not None:
		return render_template("Reading.html",temp=temperature,hum=humidity)
	else:
		return render_template("No_sensor.html")

if __name__ == '__main__':
    app.run()
