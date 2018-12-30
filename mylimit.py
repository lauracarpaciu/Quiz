import mysql.connector
import random

mydb = mysql.connector.connect(
    host="localhost",
    user="mirela",
    passwd="12345678",
    database="mypython"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT name, team FROM players LIMIT 9 OFFSET 2")
myresult = mycursor.fetchall()

no_questions = 10

if no_questions >= len(myresult):
    print("Nu sunt decat " + str(len(myresult)) + " intrebari posibile!")

questions = []
index_deja_luat = []

index = random.randint()
for no_questions in range(no_questions + 1):
while(index_deja_luat.__contains__(index))
    l = len(myresult)
print(l)
res = myresult[5]
print(res)
print(res[0])
print(res[1])
