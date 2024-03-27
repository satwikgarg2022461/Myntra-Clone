from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route("/deller")
def home():
    return render_template('distributor_home.html')

@app.route("/register_customer")
def register_customer():
    return render_template('register_customer.html')

@app.route("/register_distributor")
def register_distributor():
    return render_template('register_distributor.html')

if(__name__ == "__main__"):
    app.run(host="0.0.0.0",debug = True)
