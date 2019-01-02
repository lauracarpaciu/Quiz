import mysql.connector
import random

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
    print("There are only " + str(len(myresult)) + " possible questions!")

score = 0
questions = []
index_already_taken = []
index_already_taken.clear()

for no_questions in range(no_questions + 1):

    index = random.randrange(len(myresult))

    while (index_already_taken.__contains__(index)):
        index_already_taken.__add__(index)

res = myresult[index]
player = res[0]
team = res[1]

questiontext = "Who is the captain of the team {kwarg}?".format(kwarg=team)
print(questiontext)


class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def get_text(self):
        return self.__text

    def set_text(self, text):
        self.__text = text

    def get_answer(self):
        return self.__answer

    def set_answer(self, answer):
        self.__answer = answer


questions.append(Question(questiontext, player))

try:
    for question in questions:
        print(question.get_text())

        username = input()

    if (username.__contains__(question.get_text())):
        print("Well done! Good answer!")
    else:
        print("Answer is not correct!")
        print("The correct answer is " + str(question.get_text()))

except:
    print("An error has occurred!")
