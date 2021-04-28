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
    # DDL statement to drop the risk table
    ddl_delete_table = '''DROP TABLE IF EXISTS risk'''
    cursor.execute(ddl_delete_table)
    connection.commit()
    print("Table ca_db.risk is dropped successfully.")

except (Exception, Error) as error:
    print("Error while dropping the ca_db.risk table", error)


try:
    # DDL statement to create the risk table
    ddl_create_table = '''CREATE TABLE risk
          (
          risk_id                    serial       NOT NULL PRIMARY KEY,
          risk_name                  VARCHAR(255) NOT NULL,
          risk_description           TEXT         NOT NULL
          ); '''

    # Execute the create table command
    cursor.execute(ddl_create_table)
    connection.commit()
    print("Table ca_db.risk is created successfully.")

except (Exception, Error) as error:
    print("Error while creating the table ca_db.risk.", error)

try:
    # DML statements to empty the table (should be empty anyhow after the create).
    dml_truncate_table = '''TRUNCATE TABLE risk'''
    cursor.execute(dml_truncate_table)
    connection.commit()
    print("Table ca_db.risk is truncated successfully")

except (Exception, Error) as error:
    print("Error while truncating the ca_db.risk table.", error)

try:
    # DML statements to insert records in the risk table.
    dml_insert_table = '''INSERT INTO risk (                    
              risk_id                    
             ,risk_name                      
             ,risk_description                
          )                       
          VALUES                  
          (                       
              1                   
             ,'Capacity risk'    
             ,'The risk of a full database which results in an unavailability from insert and update functions.' 
           );'''
    
    # Execute the create the table command
    cursor.execute(dml_insert_table)
    connection.commit()
    print("Table ca_db.risk is populated succesfully.")


except (Exception, Error) as error:
    print("Error while populating the risk table in ca_db", error)

# Test statement.
try:
    qry_test_table = '''SELECT COUNT(*) FROM risk'''
    cursor.execute(qry_test_table)
    (number,) = cursor.fetchone()
    print("Number of records in table ca_db.risk is:",number)

    connection.commit()
except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

