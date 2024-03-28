from flask import Flask, render_template, request
from database import register,dispaly, login_check

app = Flask(__name__)

@app.route("/deller")
def deller_home():
    return render_template('distributor_home.html',home='deller')

@app.route('/')
@app.route("/customer")
def customer_home():
    return render_template('customer_home.html',home='customer')


@app.route("/register",methods=['GET'])
def register_distributor():
    return render_template('register.html')

@app.route("/sign_in",methods = ['GET'])
def  sign_in():
    return render_template('sign_in.html')

@app.route("/login",methods = ['POST'])
def  login():
    if request.method == 'POST':
        data = request.form
        login_check(data)
        return f"Logged in successfully: {data}"

# @app.route("/home_customer_logged_in")
# def home_customer_logged_in():
#     return render_template('home_customer_logged_in.html')

# @app.route("/home_distributor_logged_in")
# def home_distributor_logged_in():
#     return render_template("home_distributor_logged_in.html")

@app.route('/submit-register', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        data = request.form
        register(data)
        dispaly()
        return f"Form submitted with data: {data}"

if(__name__ == "__main__"):
    app.run(host="0.0.0.0",debug = True)
