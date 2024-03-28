from flask import Flask, render_template, request
from database import register,dispaly, login_check

app = Flask(__name__)

@app.route("/deller")
def deller():
    return render_template('Before_Login_distributor.html',home='deller')

@app.route("/customer")
def customer():
    return render_template('Before_Login_customer.html',home='customer')


@app.route("/customer/register",methods=['GET'])
def register_customer():
    return render_template('register.html',name="customer")

@app.route("/deller/register",methods=['GET'])
def register_distributor():
    return render_template('register.html',name = 'deller')

@app.route("/customer/sign_in",methods = ['GET'])
def  sign_customer_in():
    return render_template('sign_in.html',name = 'customer')

@app.route("/deller/sign_in",methods = ['GET'])
def  sign_deller_in():
    return render_template('sign_in.html',name= 'deller')






@app.route('/customer/submit-sign-in', methods=['POST'])
def customer_sign_in():
    if request.method == 'POST':
        data = request.form
        login_check(data,'customer')
        # dispaly()
        return f"Form submitted with data: {data}"

@app.route('/deller/submit-sign-in', methods=['POST'])
def deller_sign_in():
    if request.method == 'POST':
        data = request.form
        login_check(data,'deller')
        # dispaly()
        return f"Form submitted with data: {data}"








@app.route('/customer/submit-register', methods=['POST'])
def customer_submit_form():
    if request.method == 'POST':
        data = request.form
        register(data,'customer')
        # dispaly()
        return f"Form submitted with data: {data}"


@app.route('/deller-submit-register', methods=['POST'])
def deller_submit_form():
    if request.method == 'POST':
        data = request.form
        register(data,'distributor')
        return f"Form submitted with data: {data}"

@app.route("/deller/home")
def  deller_home():
    return render_template('deller_home.html')

@app.route("/customer/home")
def  customer_home():
    return render_template('customer_home.html')


if(__name__ == "__main__"):
    app.run(host="0.0.0.0",debug = True)
