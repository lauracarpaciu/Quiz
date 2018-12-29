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

mycursor = mydb.cursor()

sql = "DELETE FROM players WHERE name = %s"
nme = ("FC Real Madrid", "FC Villarreal", "FC Barcelona", "FC Atl. Madrid", "FC Valencia",
       "FC Ath. Bilbao",

       )

mycursor.execute(sql, nme)

mydb.commit()
