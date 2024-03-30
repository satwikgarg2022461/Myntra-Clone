from flask import Flask, render_template, request, redirect, url_for
from database import register,dispaly, login_check, product_list, fetch_product_data,add_product, fetch_inventory_data, fetch_feedback,fetch_deller_profile,fetch_customer_profile, fetch_customer_cart, transaction, remove_cart_item, add_product_to_cart, fetch_order_history, add_feedback
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
            set_customer_id(id)
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

@app.route('/deller/inventory')
def inventory():
    inventory_data = fetch_inventory_data()
    return render_template('inventory.html',inventory_data=inventory_data)

@app.route('/deller/feedback')
def feedback():
    feedback = fetch_feedback()
    return render_template('deller_feedback.html',feedback_data=feedback)
    
@app.route('/deller/profile')
def deller_profile():
    profile = fetch_deller_profile()
    return render_template('deller_profile.html',profile_data=profile)

@app.route('/customer/profile')
def customer_profile():
    profile = fetch_customer_profile()
    return render_template('customer_profile.html',profile_data=profile)

@app.route('/customer/cart')
def customer_cart():
    cart = fetch_customer_cart()
    total = 0
    for i in cart['cart_items']:
        total+=i['product_quantity']*i['price']
    return render_template('customer_cart.html',cart=cart,total=total)

@app.route('/customer/transaction')
def customer_transaction():
    transaction()
    return redirect(url_for('product'))

@app.route('/customer/remove-cart-item')
def customer_remove_cart_item():
    product_id = request.args.get('product_id')
    remove_cart_item(product_id=product_id)
    return  redirect(url_for('customer_cart'))

@app.route('/customer/cart_add')
def customer_cart_add():
    product_id = request.args.get('product_id')
    distribution_id = request.args.get('distribution_id')
    quantity = 1
    add_product_to_cart(product_id=product_id,distribution_id=distribution_id,quantity=quantity)
    return redirect(url_for('product'))

@app.route('/customer/order_history',methods=['GET'])
def customer_order_history():
    order_details = fetch_order_history()
    return render_template('order_history.html',order_details=order_details)

@app.route('/customer/add-feedback',methods=['POST'])
def customer_add_feedback():
    
    print("apphi")
    review = request.form
    product_id = request.args.get('product_id')
    add_feedback(product_id=product_id,review=review)
    return redirect(url_for('customer_order_history'))


if(__name__ == "__main__"):
    app.run(host="0.0.0.0",debug = True)
