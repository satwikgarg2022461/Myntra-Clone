import urllib.parse
import sqlalchemy
from sqlalchemy import create_engine, text

encoded_password = urllib.parse.quote_plus("Satwik@07")

connection_string = f"mysql+pymysql://root:{encoded_password}@localhost:3306/myntra"

engine = create_engine(connection_string)

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM customer"))
    print(result.fetchall())  
