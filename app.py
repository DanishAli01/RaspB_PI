# -*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_restful import Resource, Api
import sqlite3
from sqlite3 import Error

#constant for database
DATABASE = "sqlite-autoconf-3230100/project"

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None

def select_all_temp(conn, startDate, endDate):
    cur = conn.cursor()
    print("connected")
    sql = 'SELECT * FROM temps'
    if startDate != "0" :
        sql = sql + " where tdate >= ?"
    if endDate != "0" :
        sql = sql + " and tdate <= ?"
    print(sql)

    cur.execute(sql, [startDate, endDate])
    print("executed")
    return cur.fetchall()

def get_recent_setting(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM settings order by ROWID desc limit 1')
    return cur.fetchall()

def save_settings(conn, temperature, humidity, emergency_phone):
    cur = conn.cursor()
    #delete previous entries
    cur.execute('delete from settings')

    # insert new record inside table
    cur.execute('replace into settings values (?,?,?)', [temperature, humidity, emergency_phone])

    return conn.commit()

#Method to send SMS incase of emergency_phone
def send_emergency_message(conn):
    cur = conn.cursor()
    // fetch emergency phone number
    cur.execute('SELECT * FROM settings order by ROWID desc limit 1')



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

@app.route('/settings')
def settings():
    # create a database connection
    conn = create_connection(DATABASE)

    temp = 0
    humid = 0
    phone = ""

    with conn:
        print("Get last settings")
        #select_all_temp(conn)
        rows = get_recent_setting(conn)

    if rows:
        temp=rows[0][0]
        humid=rows[0][1]
        phone=rows[0][2]


    return render_template("settings.html", temp=temp, humid=humid, phone=phone)

@app.route('/processSettings', methods = ['POST', 'GET'])
def saveSettings():

    # get inputs from form

    temperature = request.form['temperature']
    humidity = request.form['humidity']
    emergency_phone = request.form['emergency_phone']

    # create a database connection
    conn = create_connection(DATABASE)
    with conn:
        print("Send temperature and humidity across")
        #select_all_temp(conn)
        rows = save_settings(conn, temperature, humidity, emergency_phone)

    #return render_template("settings.html", )
    return redirect(url_for('settings'))


@app.route('/api/get_temp', methods=["GET", "POST"])
def temperature():

    # get url params
    startDate = request.args.get('start_date')
    endDate = request.args.get('end_date')

    # create a database connection
    conn = create_connection(DATABASE)
    with conn:
        print("2. Query all temps")
        #select_all_temp(conn)
        rows = select_all_temp(conn, startDate, endDate)

    # build data
    temp = []
    humid = []
    dates = []
    for row in rows:
        temp.append(row[2])
        humid.append(row[3])
        dates.append(row[0])

    return jsonify({'temperature': temp, 'humidity' : humid, 'categories' : dates})
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
