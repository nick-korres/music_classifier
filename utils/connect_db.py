import sys
import os
current_script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_script_dir)
sys.path.append(parent_dir)

import psycopg2
from utils.attributes import Attributes

saved_attributes =[attribute.value for attribute in Attributes]

def conenct_db():
    conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="music",
    user="root",
    password="root"
    )
    return conn

def run_query(query):
    conn = conenct_db()
    cursor = conn.cursor()
    cursor.execute(query)
    try:
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        
        result= {"rows":rows, "columns":columns}
    except:
        result = None
  
    conn.commit()
    cursor.close()
    conn.close()
    return result

def insert_song(song):
    columns=""
    values=""

    if song == None:
        return
    
    for key in saved_attributes:
        columns += key + ", "
        value = song[key]
        values += str(value) + ", "

    columns = f'({columns.rstrip(", ")})'
    values = f'({values.rstrip(", ")})'

    query = f"INSERT INTO public.track_attributes {columns} VALUES {values} ;"
    run_query(query)