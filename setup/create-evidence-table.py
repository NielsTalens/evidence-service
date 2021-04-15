import os
import psycopg2
from psycopg2 import Error

# Write your name to the env file
username = os.environ['USERNAME']

try:
    # Connect to an existing database
    connection = psycopg2.connect(user= username,
                                  password="",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="ca_db")

    # Create a cursor to perform database operations
    cursor = connection.cursor()
    # SQL query to create a new table
    create_table_query = '''CREATE TABLE evidence
          (id serial NOT NULL PRIMARY KEY,
          rule_description           TEXT    NOT NULL,
          control_id           TEXT    NOT NULL,
          retrieved_value         TEXT); '''
    # Execute a command: this creates a new table
    cursor.execute(create_table_query)
    connection.commit()
    print("Table evidence created successfully in PostgreSQL ")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")