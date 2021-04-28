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
    # DDL statement to drop the control table
    ddl_delete_table = '''DROP TABLE IF EXISTS control'''
    cursor.execute(ddl_delete_table)
    connection.commit()
    print("Table ca_db.control is dropped successfully.")

except (Exception, Error) as error:
    print("Error while dropping the ca_db.control table", error)


try:
    # DDL statement to create the control table
    ddl_create_table = '''CREATE TABLE control
          (
           control_id                serial        NOT NULL PRIMARY KEY
          ,risk_id                   INT           NOT NULL
          ,mo_id                     INT           NOT NULL
          ,name                      VARCHAR(255)  NOT NULL
          ,CIA_rating                INT           NOT NULL                         
          ,description               TEXT          NOT NULL
          ); '''

    # Execute the create table command
    cursor.execute(ddl_create_table)
    connection.commit()
    print("Table ca_db.control is created successfully.")

except (Exception, Error) as error:
    print("Error while creating the ca_db.control.", error)

try:
    # DML statements to empty the table (should be empty anyhow after the create).
    dml_truncate_table = '''TRUNCATE TABLE control'''
    cursor.execute(dml_truncate_table)
    connection.commit()
    print("Table ca_db.control is truncated successfully")

except (Exception, Error) as error:
    print("Error while truncating the ca_db.control table.", error)

try:
    # DML statements to insert records in the control table.
    dml_insert_table = '''INSERT INTO control (                    
              control_id                    
             ,risk_id
             ,mo_id
             ,name
             ,CIA_rating                      
             ,description                
        )                       
          VALUES                  
        (                       
              1                   
             ,1
             ,1
             ,'Capacity risk control for SQL Server'  
             ,222  
             ,'The control for the capacity risk is to monitor the capacity of the database on two levels: 60% (warning), 80% (exception)'
        );'''
    
    # Execute the create the table command
    cursor.execute(dml_insert_table)
    connection.commit()
    print("Table ca_db.control is populated succesfully.")


except (Exception, Error) as error:
    print("Error while populating the control table in ca_db", error)

# Test statement.
try:
    qry_test_table = '''SELECT COUNT(*) FROM control'''
    cursor.execute(qry_test_table)
    (number,) = cursor.fetchone()
    print("Number of records in table ca_db.control is:",number)

    connection.commit()
except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

