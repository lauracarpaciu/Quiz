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
sql = "INSERT INTO players (team, name) VALUES (%s, %s)"
val = [
    ["FC Real Madrid", "Cristiano Ronaldo"], ["FC Villarreal", "Bruno Soriano"], ["FC Barcelona", "Lionel Messi"],
    ["FC Atl. Madrid", "Gabriel Fernández"], ["FC Sevilla", "Julien Escudé"], ["FC Valencia", "Dani Parejo"],
    ["FC Ath. Bilbao", "Gorka Iraizoz"], ["FC Espanyol", "Javi López"], ["FC Valencia", "Dani Parejo"],
    ["FC Valencia", "K. Casilla"], ["FC Valencia", "Courtois"], ["FC Valencia", "Luca"],
    ["FC Valencia", "Carvajal"], ["FC Valencia", "Vallejo"], ["FC Valencia", "Sergio Ramos"],
    ["FC Valencia", "Varane"]
]

'''The executemany() method will execute the operation iterating
        over the list of parameters in seq_params.'''
mycursor.executemany(sql, val)

mydb.commit()
