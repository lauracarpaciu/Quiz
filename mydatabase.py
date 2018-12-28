import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="mirela",
  passwd="12345678"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mypython")