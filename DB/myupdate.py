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
sql = "UPDATE players SET name = %s WHERE name = %s"
val = ("Keylor Navas", "Cristiano Ronaldo")

mycursor.execute(sql, val)

mydb.commit()