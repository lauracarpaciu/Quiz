import mysql.connector

'''Connect() will open a connection to a
    MySQL server and return a MySQLConnection object.'''

mydb = mysql.connector.connect(
    host="localhost",
    user="mirela",
    passwd="12345678",
    database = "mypython"
)

mycursor = mydb.cursor()  # Instantiates and returns a cursor
mycursor.execute("CREATE TABLE players (name VARCHAR(255), team VARCHAR(255))")