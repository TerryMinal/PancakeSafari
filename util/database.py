#PancakeSafari
#Adam Abbas, Terry Guan, Irene Lam, Shannon Lau (PM)
#SoftDev pd7
#P01 -- ArRESTed Development

global db
# from flask import flash
import sqlite3, random  # enable control of an sqlite database
import hashlib
from time import gmtime, strftime
import os
#opens a database
def open_db():
    global db
    f = os.path.abspath("database.db")
    db = sqlite3.connect(f, check_same_thread=False)  # open if f exists, otherwise create
    # c = db.cursor()    #facilitate db ops
    return

#closes the database
def close():
    global db
    db.commit()  # save changes
    db.close()  # close database
    return

#sets up the database
def db_setup():
    global db
    open_db()
    c = db.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS threads (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        time DEFAULT CURRENT_TIMESTAMP NOT NULL,
        message_log TEXT NOT NULL,
        gif_url TEXT NOT NULL)''')
    close()
    return

#adds a new entry into the table with a given conversation log and a gif url
def create_thread(input_log, input_url):
    global db
    try:
        open_db()
        c = db.cursor()
        command = '''INSERT INTO threads (time, message_log, gif_url)
            VALUES (date('now'), ?, ?)'''
        # print command
        c.execute(command, (input_log, input_url,))      # input_log and input_url are from user/db
        close()
    except:
        print "Error creating thread"
        return False
    return True

#gets a specific thread given a index
def get_thread(index):
    global db
    try:
        open_db()
        c = db.cursor()
        c.execute("SELECT message_log FROM threads WHERE id=?", (index,))      # input_log and input_url are from user/db
        rows = c.fetchall()

        for i in rows:
            print i

        close()
    except:
        print "Error creating thread"
        return False
    return True



if __name__ == "__main__":
    db_setup()
    create_thread('"text":"Today was a happy day"',
              "https://i.pinimg.com/736x/de/c5/d1/dec5d1d75fa4333d771e6fed6c97c958--dessin-ghibli-ghibli-watercolor.jpg")
    create_thread('"text":"Today was another happy day"',
              "https://i.pinimg.com/736x/de/c5/d1/dec5d1d75fa4333d771e6fed6c97c958--dessin-ghibli-ghibli-watercolor.jpg")
    create_thread('"text":"I hope it continues to be like this"',
              "https://i.pinimg.com/736x/de/c5/d1/dec5d1d75fa4333d771e6fed6c97c958--dessin-ghibli-ghibli-watercolor.jpg")
    get_thread(1)
    get_thread(3)
