import os
import psycopg2
from psycopg2 import Error

# Write your name to the env file
username = os.environ['USER']

try:
    # Connect to an existing database
    connection = psycopg2.connect(user= username,
                                  password="",
                                  host="localhost",
                                  port="5432",
                                  database="ca_db")

    # Create a cursor to perform database operations
    cursor = connection.cursor()

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)

try:
    # DDL statements to drop and create a table
    ddl_delete_table = '''DROP TABLE IF EXISTS managedobject'''
    cursor.execute(ddl_delete_table)
    connection.commit()
    print("Table ca_db.managedobject is dropped successfully.")

except (Exception, Error) as error:
    print("Error while dropping the ca_db.managedobject table", error)

try:
    # DDL statement to create the managedobject table
    ddl_create_table = '''CREATE TABLE managedobject
          (
          mo_id                      serial       NOT NULL PRIMARY KEY,
          name                       VARCHAR(255) NOT NULL,
          description                TEXT         NOT NULL
          ); '''

    # Execute the create the table command
    cursor.execute(ddl_create_table)
    connection.commit()
    print("Table ca_db.managedobject is created successfully.")

except (Exception, Error) as error:
    print("Error while creating the table ca_db.managedobject.", error)


try:
    # DML statements to insert records in the managedobject table.
    dml_insert_table = '''INSERT INTO managedobject (                    
              mo_id                    
             ,name                      
             ,description                
          )                       
          VALUES                  
          (                       
              1                   
             ,'MS SQL Server'    
             ,'The MS SQL Server managed object.' 
           );'''
    
    # Execute the create the table command
    cursor.execute(dml_insert_table)
    connection.commit()
    print("Table ca_db.managedobject is populated succesfully.")


except (Exception, Error) as error:
    print("Error while populating the managedobject table in ca_db", error)

# Test statement.
try:
    qry_test_table = '''SELECT COUNT(*) FROM managedobject'''
    cursor.execute(qry_test_table)
    (number,) = cursor.fetchone()
    print("Number of records in table ca_db.managedobject is:",number)

    connection.commit()
except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

