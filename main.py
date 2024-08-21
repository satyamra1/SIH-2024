import sqlite3
import pandas as pd
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "test.db")
with sqlite3.connect(db_path) as db:
    
    a=pd.read_sql_query("SELECT * from Basic", db)

print(type(a))