import mysql.connector
import random
import Question

mydb = mysql.connector.connect(
    host="localhost",
    user="mirela",
    passwd="12345678",
    database="mypython"
)

mycursor = mydb.cursor()


def create_db():
    mycursor.execute("CREATE DATABASE mypython")


def create_table():
    mycursor.execute("CREATE TABLE players (name VARCHAR(255), team VARCHAR(255))")


def alter_table():
    mycursor.execute("ALTER TABLE players ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")


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


def read_from_db():
    mycursor.execute("SELECT name, team FROM players LIMIT 9 OFFSET 2")
    myresult = mycursor.fetchall()


def delete_from_db():
    sql = "DELETE FROM players WHERE team = %s"
    tm = ("FC Real Madrid", "FC Villarreal", "FC Barcelona", "FC Atl. Madrid", "FC Valencia",
          "FC Ath. Bilbao",

          )
    mycursor.execute(sql, tm)
    mydb.commit()


def update_from_db():
    sql = "UPDATE players SET name = %s WHERE name = %s"
    val = ("Keylor Navas", "Cristiano Ronaldo")

    mycursor.execute(sql, val)

    mydb.commit()


# create_db()
# create_table()
# alter_table()
# data_entry()
#  read_from_db()
# delete_from_db()
# update_from_db()
# mycursor.close()
# mydb.close()


mycursor.execute("SELECT name, team FROM players LIMIT 9 OFFSET 2")
myresult = mycursor.fetchall()

no_questions = 10

if no_questions >= len(myresult):
    print("Nu sunt decat " + str(len(myresult)) + " intrebari posibile!")

questions = []
index_deja_luat = []
for no_questions in range(no_questions + 1):

    index = random.randrange(len(myresult))
    while (index_deja_luat.__contains__(index)):
        index_deja_luat.append(index)

res = myresult[index]
player = res[0]
team = res[1]

questiontext = "Care este capitanul echipei {kwarg}?".format(kwarg=team)
questions.append(Question(questiontext,player))