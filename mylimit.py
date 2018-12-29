import pandas as pd
import mysql.connector

'''Connect() will open a connection to a
    MySQL server and return a MySQLConnection object.'''

mydb = mysql.connector.connect(
    host="localhost",
    user="mirela",
    passwd="12345678",
    database="mypython"
)
sql = "SELECT name, team  FROM players LIMIT 8 OFFSET 2"
result = ""

try:
    df = pd.read_sql(sql, mydb)  # Read SQL query or database table into a DataFrame.

finally:
    mydb.close
