import mysql.connector

'''Connect() will open a connection to a
    MySQL server and return a MySQLConnection object.'''

mydb = mysql.connector.connect(
    host="localhost",
    user="mirela",
    passwd="12345678",
    database="mypython"
)

mycursor = mydb.cursor()  # Instantiates and returns a cursor
mycursor.execute("SELECT * FROM players LIMIT 5 OFFSET 2")

myresult = mycursor.fetchall()
for x in myresult:
  print(x)