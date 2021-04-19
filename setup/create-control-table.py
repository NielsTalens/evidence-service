# importing os module to get access to environment variables
import os

# importing the PostgreSQL database adapter
import psycopg2
from psycopg2 import Error

# Write your name to the env file
# USERNAME is not a know variable in my computer, so I used 'USER'
username = os.environ['USERNAME']

try:
    # Connect to an existing database
    connection = psycopg2.connect(user= username,
                                  password="pgadmin",
                                  host="localhost",
                                  port="5432",
                                  database="ca_db")

    # Create a cursor to perform database operations
    cursor = connection.cursor()
    # SQL query to create a new table
    create_table_query = '''CREATE TABLE controls
          (id                   serial  NOT NULL PRIMARY KEY,
          control_id            TEXT    NOT NULL,
          control_description   TEXT,
          control_value         TEXT); '''
    # Execute a command: this creates a new table
    cursor.execute(create_table_query)
    connection.commit()
    print("Table controls created successfully in PostgreSQL ")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")