from flask import Flask, render_template

# Making instance of Flask Class
app = Flask(__name__)

# Pinpoints the address
@app.route('/home')
def index():
    # Render Templates
     return render_template("home.html")

@app.route('/about')
def about():
    # Render Templates
     return render_template("about.html")

@app.route('/Power')
def about():
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