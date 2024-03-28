from flask import Flask, render_template, request
from database import register,dispaly

app = Flask(__name__)

@app.route('/')
@app.route("/deller")
def deller_home():
    return render_template('distributor_home.html',home='deller')

@app.route("/customer")
def customer_home():
    return render_template('customer_home.html',home='customer')


@app.route("/register",methods=['GET'])
def register_distributor():
    return render_template('register.html')

@app.route('/submit-register', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        data = request.form
        register(data)
        dispaly()
        return f"Form submitted with data: {data}"

if(__name__ == "__main__"):
    app.run(host="0.0.0.0",debug = True)
