import mysql.connector
import random

#Implement  a working question bank

db = mysql.connector.connect( #connects to MySQL Server for data to be accessed
    host = "host.docker.internal",
    user = "root",
    password = "xxxxxxxx"
)

mycursor = db.cursor()
mycursor.execute("Use discordbot") #connects to database

def question(anime, list, nums):

    num = list[nums]

    print(num)

    sql = f"SELECT * FROM {anime} LIMIT 1 OFFSET %s" #query statement

    mycursor.execute(sql, (num,))

    results = mycursor.fetchall()

    return results

#grabs the correct picture to display
def picture(anime):

    sql = f"Select picture from pictures where anime = '{anime}' "
    
    mycursor.execute(sql)

    results = mycursor.fetchall()

    return results

#Inserts User's progress 
def insertResults(id, correct, total, anime):
    sql = "Select exists(Select 1 FROM userData where UserID = %s and anime = %s)"

    mycursor.execute(sql, (id,anime))

    results = mycursor.fetchone()[0]

    if results == 0:
        query = "Insert into userData (UserID, correct, total, anime) values (%s, %s, %s, %s)"
        mycursor.execute(query,(id, correct, total, anime))
        db.commit()
    
    else:
        query = "Select correct, total from userData where UserID = %s and anime = %s"
        mycursor.execute(query,(id,anime))

        result1, result2 = mycursor.fetchone()

        result1 += correct

        result2 += total

        query = "Update userData set correct = %s, total = %s where UserID = %s and anime = %s" 
        mycursor.execute(query,(result1, result2, id, anime))
        db.commit()


#Grabs the previous history of correct and total answers
def getHistory(id, anime):

    sql = "Select correct, total from userData where UserID = %s and anime = %s"

    mycursor.execute(sql, (id, anime))

    result1, result2 = mycursor.fetchone()

    return result1, result2

#Creates a random number sequences (FIX THIS)
def randomNum(num):

    random_sequence = list(range(1,num))

    random.shuffle(random_sequence)

    return random_sequence


