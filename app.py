from flask import Flask, render_template, request, redirect, url_for
from database import register,dispaly, login_check, product_list, fetch_product_data,add_product
from GlobalData import set_customer_id,set_deller_id,get_customer_id,get_deller_id

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
def customer_submit_sign_in():
    if request.method == 'POST':
        data = request.form
        id = login_check(data,'customer')
        if(id == -1):
            return "Wrong login details"
        else:
            set_customer_id = id
        # dispaly()
        return redirect(url_for('customer_home'))

@app.route('/deller/submit-sign-in', methods=['POST'])
def deller_submit_sign_in():
    if request.method == 'POST':
        data = request.form
        id=login_check(data,'distributor')
        if(id == -1):
            return "Wrong login details"
        else:
            set_deller_id(id)
            get_deller_id()
        # dispaly()
        return redirect(url_for('deller_home'))





@app.route('/customer/submit-register', methods=['POST'])
def customer_submit_form():
    if request.method == 'POST':
        data = request.form
        register(data,'customer')
        dispaly()
        return redirect(url_for('sign_customer_in'))
        

@app.route('/deller/submit-register', methods=['POST'])
def deller_submit_form():
    if request.method == 'POST':
        data = request.form
        register(data,'distributor')
        dispaly()
        return redirect(url_for('sign_deller_in'))
        




@app.route("/deller/home")
def  deller_home():
    return render_template('deller_home.html')

@app.route("/customer/home")
def  customer_home():
    return render_template('customer_home.html')



@app.route("/customer/products")
def  product():
    product_data = product_list()
    return render_template('product_list.html',product_data=product_data)

@app.route('/customer/product/<int:product_id>')
def product_detail(product_id):
    # Fetch product details based on the product_id from the database
    product_data,feedback_data = fetch_product_data(product_id)
    return render_template('product_individual_page.html',product_data=product_data,feedback_data = feedback_data)

@app.route("/deller/add-product", methods=["GET"])
def  add_product_page():
    return render_template('add_product.html')


@app.route('/deller/submit-product', methods=['POST'])
def deller_add_product_form():
    if request.method == 'POST':
        data = request.form
        add_product(data)
        dispaly()
        return redirect(url_for('deller_home'))


if(__name__ == "__main__"):
    app.run(host="0.0.0.0",debug = True)
