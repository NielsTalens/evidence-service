import requests
import json
import os
import psycopg2
import datetime
from psycopg2 import Error

# Write your name to the env file
username = os.environ['USER']

response = requests.get('http://xkcd.com/23/info.0.json')
print(response)

# Map the retrieved information
rule_description = response.json()['title']
retrieved_value = response.json()['month']
control_id = "MAN-1X"
retrieval_time = datetime.datetime.now()

try:
    # Connect to an existing database
    connection = psycopg2.connect(user= username,
                                  password="",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="ca_db")

    cursor = connection.cursor()
    # Executing a SQL query to insert datetime into table
    insert_query = """ INSERT INTO evidence (rule_description, control_id, retrieved_value) VALUES (%s, %s, %s, %s)"""
    item_tuple = (rule_description, control_id, retrieved_value)
    cursor.execute(insert_query, item_tuple)
    connection.commit()
    print("1 item inserted successfully")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")