import urllib.parse
import sqlalchemy
from sqlalchemy import create_engine, text
from GlobalData import get_deller_id,get_customer_id

encoded_password = urllib.parse.quote_plus("Satwik@07")

connection_string = f"mysql+pymysql://root:{encoded_password}@localhost:3306/myntra"

engine = create_engine(connection_string)
def register(data, database):
    with engine.connect() as conn:
        name = data.get("username")
        email = data.get("email")
        phone = data.get("Phone")
        address_line1 = data.get("AddressLine1")
        city = data.get("City")
        state = data.get("State")
        postal_code = data.get("Pincode")
        country = data.get("Country")

        # Check if required fields are present
        if not all([name, email, phone, address_line1, city, state, postal_code, country]):
            print("Error: Missing required fields.")
            return

        # Insert data into customer table
        query = text(f'INSERT INTO {database} (name, address_line1, city, state, postal_code, country) VALUES ("{name}", "{address_line1}", "{city}", "{state}", "{postal_code}", "{country}");')
        result = conn.execute(query)

        # Retrieve the auto-generated customer_id
        customer_id = result.lastrowid

        # Insert data into customer_contact table
        query = text(f'INSERT INTO {database}_contact ({database}_id, phone_number, email) VALUES ({customer_id}, {phone}, "{email}");')
        conn.execute(query)

        # Commit the transaction
        conn.commit()

        # Print the updated customer table
        result1 = conn.execute(text("SELECT * FROM customer"))
        print(result1.fetchall())

def login_check(data,database):
    with engine.connect() as conn:
        
        name = data.get("username")
        email = data.get("email")
        query = text(f'SELECT c.{database}_id FROM {database} c JOIN {database}_contact cc ON c.{database}_id = cc.{database}_id WHERE c.name = "{name}" AND cc.email = "{email}";')
        result = conn.execute(query)
        conn.commit()
        fetched_result = result.fetchone()
        print(fetched_result)
        dispaly("customer")
        if fetched_result:
            database_id = fetched_result[0]
            return database_id
        else:
            return -1

def dispaly(data):
    print(data)
    with engine.connect() as conn:
        result = conn.execute(text(f'SELECT * FROM {data}'))
        print(result.fetchall())

def product_list():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM product"))
        product_data = result.fetchall()
        
        # List to store dictionaries for each product
        products = []
        for product_data[0] in product_data:
            product_dict = {
                'product_id': product_data[0][0],
                'distributor_id': product_data[0][1],
                'name': product_data[0][2],
                'description': product_data[0][3],
                'quantity': product_data[0][4],
                'price': product_data[0][5],
                'category': product_data[0][6]
            }
            products.append(product_dict)
        
        # print(products)
        
        return products

def fetch_product_data(product_id):
    with engine.connect() as conn:
        result = conn.execute(text(f'SELECT * FROM product WHERE product_id={product_id}'))
        feedback = conn.execute(text(f'SELECT review FROM feedback WHERE product_id={product_id}'))
        feedback_data = feedback.fetchall()
        product_data = result.fetchall()
        print(product_data)
        print(feedback_data)
        product_dict={}
        product_dict = {
            'product_id': product_data[0][0],
            'distributor_id': product_data[0][1],
            'name': product_data[0][2],
            'description': product_data[0][3],
            'quantity': product_data[0][4],
            'price': product_data[0][5],
            'category': product_data[0][6]
            }
        return product_dict,feedback_data

# fetch_product_data(2)

def add_product(data):
    with engine.connect() as conn:
        name = data.get("name")
        description = data.get("description")
        quantity = int(data.get("quantity"))
        price = int(data.get("price"))
        category = (data.get("category"))
        distribution_id = get_deller_id()
        query = text(f'INSERT INTO product (distributor_id, name, description, quantity, price, Category)VALUES ({distribution_id}, "{name}", "{description}", "{quantity}", "{price}", "{category}");')
        result = conn.execute(query)
        conn.commit()
        dispaly("product")

def fetch_inventory_data():
    with engine.connect() as conn:
        distributor_id = get_deller_id()
        result = conn.execute(text(f'SELECT p.product_id, p.name, p.description, p.quantity, p.price, p.Category FROM product p JOIN inventory i ON p.product_id = i.product_id WHERE i.distributor_id = {distributor_id};'))
        inventory_data = result.fetchall()
        print(inventory_data)
        
        # List to store dictionaries for each product
        inventories = []
        for product_data in inventory_data:
            product_dict = {
                'product_id': product_data[0],
                'name': product_data[1],
                'description': product_data[2],
                'quantity': product_data[3],
                'price': product_data[4],
                'category': product_data[5]
            }
            inventories.append(product_dict)
        
        print(inventories)
        
        return inventories

def fetch_feedback():
    with engine.connect() as conn:
        distributor_id = get_deller_id()
        result = conn.execute(text(f'SELECT f.review, p.product_id, p.name, p.description, p.quantity, p.price, p.Category, c.customer_id, c.name FROM Feedback f JOIN product p ON f.product_id = p.product_id JOIN Customer c ON f.customer_id = c.customer_id WHERE p.distributor_id = {distributor_id};'))
        feedback_data = result.fetchall()
        print(feedback_data)
        feedbacks = []
        for i in feedback_data:
            feedback_dic = {
                'product_id': i[1],
                'name': i[2],
                'description': i[3],
                'quantity': i[4],
                'price': i[5],
                'category': i[6],
                'feedback' : i[0],
                'customer_id': i[7],
                'customer name': i[8],
            }
            feedbacks.append(feedback_dic)
        print(feedbacks)
        return feedbacks

def fetch_deller_profile():
    with engine.connect() as conn:
        distributor_id = get_deller_id()  # Assuming you have a function to get distributor ID
        result = conn.execute(text(f'SELECT d.*, dc.phone_number, dc.email, p.product_id, p.name AS product_name FROM distributor d JOIN distributor_contact dc ON d.distributor_id = dc.distributor_id LEFT JOIN product p ON d.distributor_id = p.distributor_id WHERE d.distributor_id = {distributor_id};'))
        distributor_data = result.fetchall()
        
        distributors = []
        for row in distributor_data:
            distributor_dic = {
                'distributor_id': row[0],
                'name': row[1],
                'address_line1': row[2],
                'city': row[3],
                'state': row[4],
                'postal_code': row[5],
                'country': row[6],
                'phone_number': row[7],
                'email': row[8],
                'product_id': row[9],
                'product_name': row[10],
            }
            distributors.append(distributor_dic)
        print(distributors)
        
        return distributors

def fetch_customer_profile():
    with engine.connect() as conn:
        customer_id = get_customer_id()  # Assuming you have a function to get customer ID
        query = f"""
            SELECT c.customer_id, c.name AS customer_name, c.address_line1, c.city, c.state, c.postal_code, c.country,
                   cc.phone_number, cc.email,
                   f.review,
                   p.product_id, p.name AS product_name
            FROM customer c
            LEFT JOIN customer_contact cc ON c.customer_id = cc.customer_id
            LEFT JOIN Feedback f ON c.customer_id = f.customer_id
            LEFT JOIN product p ON f.product_id = p.product_id
            WHERE c.customer_id = {customer_id}
        """
        result = conn.execute(text(query))
        customer_data = result.fetchall()

        customers = []
        for row in customer_data:
            customer_dic = {
                'customer_id': row[0],
                'customer_name': row[1],
                'address_line1': row[2],
                'city': row[3],
                'state': row[4],
                'postal_code': row[5],
                'country': row[6],
                'phone_number': row[7],
                'email': row[8],
                'review': row[9],
                'product_id': row[10],
                'product_name': row[11]
            }
            customers.append(customer_dic)
        print(customers)
        return customers

# 
def fetch_customer_cart():
    with engine.connect() as conn:
        # Fetch customer details
        customer_id = get_customer_id()
        customer_query = f"""
            SELECT *
            FROM customer
            WHERE customer_id = {customer_id}
        """
        customer_result = conn.execute(text(customer_query))
        customer_details = customer_result.fetchone()

        # Fetch customer cart items
        cart_query = f"""
            SELECT p.product_id, p.name AS product_name, p.description, cart.quantity AS product_quantity, p.price, p.Category
            FROM cart cart
            INNER JOIN product p ON cart.product_id = p.product_id
            WHERE cart.customer_id = {customer_id}
        """
        cart_result = conn.execute(text(cart_query))
        cart_data = cart_result.fetchall()

        # Prepare data dictionary
        customer_data = {
            'customer_id': customer_details[0],
            'name': customer_details[1],
            'address_line1': customer_details[2],
            'city': customer_details[3],
            'state': customer_details[4],
            'postal_code': customer_details[5],
            'country': customer_details[6],
            'cart_items': []
        }

        for row in cart_data:
            cart_item = {
                'product_id': row[0],
                'product_name': row[1],
                'description': row[2],
                'product_quantity': row[3],
                'price': row[4],
                'category': row[5],
            }
            customer_data['cart_items'].append(cart_item)

        return customer_data

def transaction():
    changed_tables = []

    customer_id = 1  # Use a specific customer_id (e.g., 1)

    # Start a transaction
    with engine.connect() as conn:
        customer_id = get_customer_id()        

        # INSERT INTO transaction table
        insert_transaction = text("""
            INSERT INTO transaction (product_id, customer_id, distributor_id, quantity)
            SELECT c.product_id, c.customer_id, c.distributor_id, c.quantity
            FROM cart c
            WHERE c.customer_id = :customer_id
        """)
        conn.execute(insert_transaction, {'customer_id': customer_id})
        conn.commit()
        dispaly("customer_history")

        # UPDATE product table
        update_product = text("""
            UPDATE product p
            INNER JOIN cart c ON p.product_id = c.product_id
            SET p.quantity = p.quantity - c.quantity
            WHERE c.customer_id = :customer_id
        """)
        conn.execute(update_product, {'customer_id': customer_id})
        conn.commit()

        # UPDATE inventory table
        update_inventory = text("""
            UPDATE inventory i
            INNER JOIN cart c ON i.product_id = c.product_id AND i.distributor_id = c.distributor_id
            SET i.quantity = i.quantity - c.quantity
            WHERE c.customer_id = :customer_id
        """)
        conn.execute(update_inventory, {'customer_id': customer_id})
        conn.commit()

        # DELETE FROM cart
        try:
            delete_cart = text("""
                DELETE FROM cart
                WHERE customer_id = :customer_id
            """)
            conn.execute(delete_cart, {'customer_id': customer_id})
            conn.commit()
        except:
            print()

        dispaly("cart")

def remove_cart_item(product_id):
    with engine.connect() as conn:
        customer_id = get_customer_id()

        # Check if the item exists in the cart
        existing_query = text(f'SELECT * FROM cart WHERE customer_id = {customer_id} AND product_id = {product_id};')
        existing_result = conn.execute(existing_query)
        existing_item = existing_result.fetchone()
        
        if not existing_item:
            return "Item not found in the cart."
        
        # Remove the item from the cart
        delete_query = text(f'DELETE FROM cart WHERE customer_id = {customer_id} AND product_id = {product_id};')
        conn.execute(delete_query)
        conn.commit()
    dispaly("cart")
    return "Item removed from cart successfully."

def add_product_to_cart(product_id, distribution_id, quantity):
    with engine.connect() as conn:
        customer_id = get_customer_id()  # Assuming you have a function to get customer ID
        

        # Check if the item already exists in the cart for the customer
        check_query = text(f"SELECT * FROM cart WHERE customer_id = {customer_id} AND product_id = {product_id}")
        existing_item = conn.execute(check_query).fetchone()

        if existing_item:
            # Update quantity if the item already exists in the cart
            new_quantity = existing_item["quantity"] + quantity
            update_query = text(f"UPDATE cart SET quantity = {new_quantity} WHERE customer_id = {customer_id} AND product_id = {product_id};")
            conn.execute(update_query)
            conn.commit()
        else:
            # Insert new item into the cart if it doesn't exist
            insert_query = text(f"INSERT INTO cart (customer_id, product_id, quantity, distributor_id) VALUES ({customer_id}, {product_id}, {quantity}, {distribution_id});")
            conn.execute(insert_query)
            conn.commit()
        
        dispaly("cart")

        conn.commit()


def fetch_order_history():
    customer_id = get_customer_id()
    with engine.connect() as conn:
        query = text(f"""
            SELECT t.date_added AS order_date, t.product_id, p.name AS product_name, t.quantity, p.price
            FROM transaction t
            JOIN product p ON t.product_id = p.product_id
            WHERE t.customer_id = {customer_id}
        """)
        result = conn.execute(query)
        order_details = result.fetchall()
        print(order_details)
        

        # Convert the fetched data into a list of dictionaries
        order_list = []
        for row in order_details:
            order_dict = {
                'order_date': row[0],
                'product_id': row[1],
                'product_name': row[2],
                'quantity': row[3],
                'price': row[4]
            }
            order_list.append(order_dict)
            print(order_list)

        return order_list

def add_feedback(product_id, review):
    print("hi")
    customer_id = get_customer_id()
    review1=review.get('feedback')
    with engine.connect() as conn:
        query = text(f"""
            INSERT INTO Feedback (product_id, customer_id, review)
            VALUES ({product_id},{customer_id},"{review1}")
            ON DUPLICATE KEY UPDATE review = "{review1}"
        """)
        conn.execute(query)
        conn.commit()
        print("hi")
