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
## Create the risk table
######################################################################

# DDL statement to drop the risk table
try:
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

######################################################################
## Create the managedobject table
######################################################################
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

######################################################################
## Create the control table
######################################################################
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
          ,control_name              VARCHAR(255)  NOT NULL
          ,control_value             INT           NOT NULL        
          ,control_description       TEXT          NOT NULL
          ,CIA_rating                INT           NOT NULL    
          ); '''

    # Execute the create table command
    cursor.execute(ddl_create_table)
    connection.commit()
    print("Table ca_db.control is created successfully.")

except (Exception, Error) as error:
    print("Error while creating the ca_db.control.", error)

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
          evidence_id               serial  NOT NULL PRIMARY KEY,
          control_id                INT     NOT NULL,
          evidence_value            INT, 
          evidence_time             TEXT
          ); '''

    # Execute the create table command
    cursor.execute(ddl_create_table)
    connection.commit()
    print("Table ca_db.evidence is created successfully.")

except (Exception, Error) as error:
    print("Error while creating the ca_db.evidence.", error)

######################################################################
## Create the evidence table
######################################################################

# DDL statement to drop the evidence table
try:
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
          evidence_id               serial  NOT NULL PRIMARY KEY,
          control_id                INT     NOT NULL,
          evidence_value            INT, 
          evidence_time             TEXT
          ); '''

    # Execute the create table command
    cursor.execute(ddl_create_table)
    connection.commit()
    print("Table ca_db.evidence is created successfully.")

except (Exception, Error) as error:
    print("Error while creating the ca_db.evidence.", error)


finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")