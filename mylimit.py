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
mycursor.execute("SELECT name, team  FROM players LIMIT 8 OFFSET 2")

myresult = mycursor.fetchall()
for line in myresult:
  print(line)