import urllib.parse
import sqlalchemy
from sqlalchemy import create_engine, text

encoded_password = urllib.parse.quote_plus("Satwik@07")

connection_string = f"mysql+pymysql://root:{encoded_password}@localhost:3306/myntra"

engine = create_engine(connection_string)

def register(data,database):
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


        query = text(f'INSERT INTO {database} (name, address_line1, city, state, postal_code, country) VALUES (:name, :address_line1, :city, :state, :postal_code, :country)')
        result = conn.execute(query, {'name': name, 'address_line1': address_line1, 'city': city, 'state': state, 'postal_code': postal_code, 'country': country})
        conn.commit()
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
        if fetched_result:
            database_id = fetched_result[0]
            print(database_id)
        else:
            print("No matching record found")

def dispaly():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM customer"))
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

fetch_product_data(2)