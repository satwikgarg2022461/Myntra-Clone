import urllib.parse
import sqlalchemy
from sqlalchemy import create_engine, text

encoded_password = urllib.parse.quote_plus("Satwik@07")

connection_string = f"mysql+pymysql://root:{encoded_password}@localhost:3306/myntra"

engine = create_engine(connection_string)



def register(data):
    with engine.connect() as conn:
        name = data.get("username")
        email = data.get("email")
        phone = data.get("Phone")
        address_line1 = data.get("AddressLine1")
        city = data.get("City")
        state = data.get("State")
        postal_code = data.get("Pincode")
        country = data.get("Country")
        query = text('INSERT INTO customer (name, address_line1, city, state, postal_code, country) VALUES (:name, :address_line1, :city, :state, :postal_code, :country)')
        result = conn.execute(query, {'name': name, 'address_line1': address_line1, 'city': city, 'state': state, 'postal_code': postal_code, 'country': country})
        result1 = conn.execute(text("SELECT * FROM customer"))
        print(result1.fetchall())


def dispaly():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM customer"))
        print(result.fetchall())  

