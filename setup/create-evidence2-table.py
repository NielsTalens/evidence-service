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
    # DDL statement to drop the evidence table
    ddl_delete_table = '''DROP TABLE IF EXISTS evidence'''
    cursor.execute(ddl_delete_table)
    connection.commit()
    print("Table ca_db.evidence is dropped successfully.")

except (Exception, Error) as error:
    print("Error while dropping the ca_db.evidence table", error)


try:
    # DDL statement to create the evidence table
    ddl_create_table = '''CREATE TABLE evidence
          (
          id                         serial  NOT NULL PRIMARY KEY,
          evidence_id                 TEXT    NOT NULL,
          retrieved_value            TEXT, 
          retrieval_time             TEXT
          ); '''

    # Execute the create table command
    cursor.execute(ddl_create_table)
    connection.commit()
    print("Table ca_db.evidence is created successfully.")

except (Exception, Error) as error:
    print("Error while creating the ca_db.evidence.", error)

try:
    # DML statements to empty the table (should be empty anyhow after the create).
    dml_truncate_table = '''TRUNCATE TABLE evidence'''
    cursor.execute(dml_truncate_table)
    connection.commit()
    print("Table ca_db.evidence is truncated successfully")

except (Exception, Error) as error:
    print("Error while truncating the ca_db.evidence table.", error)

try:
    # DML statements to insert records in the evidence table.
    dml_insert_table = '''INSERT INTO evidence 
        (
           id                         
          ,evidence_id                 
          ,retrieved_value             
          ,retrieval_time             
        )     
        VALUES                  
        (                       
            1                   
           ,1
           ,'80'
           ,'20210428 10:10'  
        );'''
    
    # Execute the create the table command
    cursor.execute(dml_insert_table)
    connection.commit()
    print("Table ca_db.evidence is populated succesfully.")


except (Exception, Error) as error:
    print("Error while populating the evidence table in ca_db", error)

# Test statement.
try:
    qry_test_table = '''SELECT COUNT(*) FROM evidence'''
    cursor.execute(qry_test_table)
    (number,) = cursor.fetchone()
    print("Number of records in table ca_db.evidence is:",number)

    connection.commit()
except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

