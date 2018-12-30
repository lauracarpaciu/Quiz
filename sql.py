import mysql.connector
import time
import datetime
import random

mydb = mysql.connector.connect(
  host="localhost",
  user="mirela",
  passwd="12345678"
)

mycursor = mydb.cursor()


def create_table():
    mycursor.execute("CREATE TABLE players (name VARCHAR(255), team VARCHAR(255))")

def data_entry():
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
    mycursor.close()
    mydb.close()

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix)).__str__("%Y-%m-%d %H: %M: %S")
    keyword = "Python"
    sql = "INSERT INTO players (unix, datestamp,keyword,value) VALUES (%s, %s)"
    mycursor.execute(sql)

def read_from_db():
    mycursor.execute("SELECT name, team FROM players LIMIT 9 OFFSET 2")
    myresult = mycursor.fetchall()


    create_table()
    data_entry()
    dynamic_data_entry()
    time.sleep(1)
    mycursor.close()
    mydb.close()

