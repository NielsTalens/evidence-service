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

######################################################################
## Populate the risk table
######################################################################
try:
    print("-----------------------------------------------------------------")
    print("Populating Table ca_db.risk")

    # DML statements to empty the table.
    dml_truncate_table = '''TRUNCATE TABLE risk'''
    cursor.execute(dml_truncate_table)
    connection.commit()

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


except (Exception, Error) as error:
    print("Error while populating the risk table in ca_db", error)

# Test statement.
try:
    qry_test_table = '''SELECT COUNT(*) FROM risk'''
    cursor.execute(qry_test_table)
    (number,) = cursor.fetchone()
    print("Number of records in table ca_db.risk is:",number)
    print(" ")

    connection.commit()
except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)

######################################################################
## Populate the managedobject table
######################################################################
try:
    print("-----------------------------------------------------------------")
    print("Populating Table ca_db.managedobject")

    # DML statements to empty the table.
    dml_truncate_table = '''TRUNCATE TABLE managedobject'''
    cursor.execute(dml_truncate_table)
    connection.commit()

except (Exception, Error) as error:
    print("Error while truncating the ca_db.managedobject table.", error)

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

except (Exception, Error) as error:
    print("Error while populating the managedobject table in ca_db", error)

# Test statement.
try:
    qry_test_table = '''SELECT COUNT(*) FROM managedobject'''
    cursor.execute(qry_test_table)
    (number,) = cursor.fetchone()
    print("Number of records in table ca_db.managedobject is:",number)
    print(" ")

    connection.commit()
except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
######################################################################
## Populate the control table
######################################################################
try:
    print("-----------------------------------------------------------------")
    print("Populating Table ca_db.control")
    
    # DML statements to empty the table. 
    dml_truncate_table = '''TRUNCATE TABLE control'''
    cursor.execute(dml_truncate_table)
    connection.commit()

except (Exception, Error) as error:
    print("Error while truncating the ca_db.control table.", error)

try:
    # DML statements to insert records in the control table.
    dml_insert_table = '''INSERT INTO control (                    
              control_id                    
             ,risk_id
             ,mo_id
             ,control_name
             ,control_value
             ,control_description                
             ,CIA_rating                      
        )                       
          VALUES                  
        (                       
              11                   
             ,1
             ,1
             ,'Capacity risk control for SQL Server'  
             ,80
             ,'The control for the capacity risk is to monitor the capacity of the database on two levels: 60% (warning), 80% (exception)'
             ,222  
        );'''
    
    # Execute the create the table command
    cursor.execute(dml_insert_table)
    connection.commit()
        

except (Exception, Error) as error:
    print("Error while populating the control table in ca_db", error)

try:
    # DML statements to insert records in the control table.
    dml_insert_table = '''INSERT INTO control (                    
              control_id                    
             ,risk_id
             ,mo_id
             ,control_name
             ,control_value
             ,control_description                
             ,CIA_rating                      
        )                       
          VALUES                  
        (                       
              12                   
             ,1
             ,1
             ,'Availability risk control for SQL Server'  
             ,95
             ,'The control for the availability risk is to monitor the average availability.)'
             ,222  
        );'''
    
    # Execute the create the table command
    cursor.execute(dml_insert_table)
    connection.commit()

 

except (Exception, Error) as error:
    print("Error while populating the control table in ca_db", error)
    print(" ")

# Test statement.
try:
    qry_test_table = '''SELECT COUNT(*) FROM control'''
    cursor.execute(qry_test_table)
    (number,) = cursor.fetchone()
    print("Number of records in table ca_db.control is:",number)
    print(" ")

    connection.commit()
except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)

######################################################################
## Populate the evidence table
######################################################################
try:
    print("-----------------------------------------------------------------")
    print("Populating Table ca_db.evidence")
    
    # DML statements to empty the table (should be empty anyhow after the create).
    dml_truncate_table = '''TRUNCATE TABLE evidence'''
    cursor.execute(dml_truncate_table)
    connection.commit()

except (Exception, Error) as error:
    print("Error while truncating the ca_db.evidence table.", error)

try:
    # DML statements to insert records in the evidence table.
    dml_insert_table = '''INSERT INTO evidence 
        (
           evidence_id                         
          ,control_id                 
          ,evidence_value             
          ,evidence_time             
        )     
        VALUES                  
        (                       
            100                   
           ,11
           ,'81'
           ,'20210428 10:10'  
        );'''
        # Execute the create the table command
    cursor.execute(dml_insert_table)
    connection.commit()

except (Exception, Error) as error:
    print("Error while populating the evidence table in ca_db", error)

try:
    dml_insert_table = '''INSERT INTO evidence 
        (
           evidence_id                         
          ,control_id                 
          ,evidence_value             
          ,evidence_time             
        )     
        VALUES                  
        (                       
            101                  
           ,11
           ,'79'
           ,'20210428 10:10'  
        );'''
    # Execute the create the table command
    cursor.execute(dml_insert_table)
    connection.commit()

except (Exception, Error) as error:
    print("Error while populating the evidence table in ca_db", error)

# Test statement.
try:
    qry_test_table = '''SELECT COUNT(*) FROM evidence'''
    cursor.execute(qry_test_table)
    (number,) = cursor.fetchone()
    print("Number of records in table ca_db.evidence is:",number)
    print(" ")

    connection.commit()
except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
