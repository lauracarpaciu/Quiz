import mysql.connector
import random
import time
import datetime

# Returns MySQLConnection
mydb = mysql.connector.connect(
    host="localhost",
    user="mirela",
    passwd="12345678",
    database="mypython"
)

mycursor = mydb.cursor()  # Returns a cursor-object


def create_db():
    mycursor.execute("CREATE DATABASE mypython")


def create_table():
    mycursor.execute("CREATE TABLE players (name VARCHAR(255), team VARCHAR(255))")


def alter_table():
    mycursor.execute("ALTER TABLE players ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")


def alter_table_second():
    mycursor.execute("ALTER TABLE players ADD (datestamp VARCHAR (255),keyword VARCHAR(255)) ")


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
    mycursor.executemany(sql, val)  # Executes the given operation
    """Remove temporary save dir: rollback will no longer be possible."""
    mydb.commit()


def dynamic_data_entry():
    unix = time.time()  # Return the current time in seconds since the Epoch.
    date = str(datetime.datetime.fromtimestamp(unix).strftime(
        "%Y-%m-%d %H:%M:%S"))  # """Construct a datetime from a POSIX timestamp (like time.time()).
    print(date)
    keyword = "python"
    val = [
        ["FC Real Madrid", "Cristiano Ronaldo"], ["FC Villarreal", "Bruno Soriano"], ["FC Barcelona", "Lionel Messi"],
    ]

    mycursor.execute("INSERT INTO players(team,name,datestamp,keyword) VALUES (%s,%s,%s,%s)"(val, date, keyword))
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
# alter_table_second()
# alter_table()
# data_entry()
# dynamic_data_entry()
# read_from_db()
# delete_from_db()
# update_from_db()
# mycursor.close()
# mydb.close()


mycursor.execute("SELECT name, team FROM players LIMIT 9 OFFSET 2")

myresult = mycursor.fetchall()


class Question():

    def __init__(self, text, answer):
        self.__text = text
        self.__answer = answer

    def get_text(self):
        return self.__text

    def set_text(self, text):
        self.__text = text

    def get_answer(self):
        return self.__answer

    def set_answer(self, answer):
        self.__answer = answer

    def __str__(self):
        return str(self.text)

    def __str__(self):
        return str(self.answer)

    __repr__ = __str__


no_questions = 8

if no_questions >= len(myresult):
    raise ValueError("There are only " + str(len(myresult)) + " possible questions!")

score = 0
questions = []
players = []
index_already_taken = []
replay_user = ""
res = dict(myresult)
for player in res.keys(): {players.append(player)}

for i in range(1, no_questions + 1):
    player = players.__getitem__(random.randrange(len(players)))
    team = res.get(player)
    # teams.remove(random.randrange(len(teams)))
    questiontext = "Who is the captain of the team {kwarg}?".format(kwarg=team)
    questions.append(Question(questiontext, player))

try:
    start = time.time()

    for question in questions:
        print(question.get_text())
        username = input()
        if username in question.get_answer():
            print("Well done! Good answer!")
            score += 1
        else:
            print("Answer is not correct!")
            print("The correct answer is " + str(question.get_answer()) + "!")

except AttributeError:
    print("An error has occurred!")

done = True

end = time.time()

temp = end - start
hours = temp // 3600
temp = temp - 3600 * hours
minutes = temp // 60
seconds = temp - 60 * minutes

print("You have answered on %d:%d:%d seconds" % (hours, minutes, seconds))

print("Your final score is {kwarg}!".format(kwarg=score))

while replay_user != "d" and "n":

    print("Do you want to replay the game ? Y/N")

    replay_user = input()[0]

    if replay_user == "n":
        print("Good bye !. Press \"Enter!\"")
