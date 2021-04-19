import requests
import json
import os
import psycopg2
import datetime
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

    cursor = connection.cursor()
    # Executing a SQL query to insert datetime into table
    insert_query = """ SELECT evidence.id
                            , evidence.rule_description
                            , controls.id
                            , controls.control_description
                            , evidence.retrieved_value
                            , controls.control_value 
                       FROM evidence 
                       INNER JOIN controls ON evidence.control_id = controls.control_id;"""
    cursor.execute(insert_query)
    connection.commit()
    result = cursor.fetchall()
    print("RESULTS:")
    for row in result:
      print("The rule has succesfully passed...") if row[4] == row[5] else print("! ! ! ! ! ! ! The rule is NOT passed ! ! ! ! ! ! !")
      print("- Evidence rule description: ", row[1], )
      print("- Controls description: ", row[3])
      print("- Retrieved value: ", row[4], "Desired value: ", row[5])
      print("- - - - - - - - - -")

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")