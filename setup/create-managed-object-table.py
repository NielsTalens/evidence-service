import os
import psycopg2
from psycopg2 import Error

# Write your name to the env file
username = os.environ['USER']

try:
    # Connect to an existing database
    connection = psycopg2.connect(user= username,
                                  password="pgadmin",
                                  host="localhost",
                                  port="5432",
                                  database="ca_db")

    # Create a cursor to perform database operations
    cursor = connection.cursor()

    # DDL statements to drop and create a table
    ddl_delete_table = '''DROP TABLE IF EXISTS managedobject'''
    cursor.execute(ddl_delete_table)
    
    ddl_create_table = '''CREATE TABLE risk
          (
          mp_id                      serial       NOT NULL PRIMARY KEY,
          name                       VARCHAR(255) NOT NULL,
          description                TEXT         NOT NULL
          ); '''
    # Execute the create the table command
    cursor.execute(ddl_create_table)
    connection.commit()
    print("Table managedobject created successfully in PostgreSQL ")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")