
from flask import Flask, render_template, request, redirect, flash, Markup, url_for
import urllib2, json, random, os
from util import database, misc

app = Flask(__name__)
app.secret_key = os.urandom(128)

# root route // access and render NASA information
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/new")
def new():
    return render_template("create_convo.html")

@app.route("/insert_msg")
def insert_msg():
    # print("Database count:", database.db_count())
    database.create_thread(database.db_count(), '"text":"' + request.args['curr_message']
           + '"', "https://vignette3.wikia.nocookie.net/3__/images/a/ae/Hatsune3.png/revision/latest?cb=20150329103424&path-prefix=300-heroes") # random photo to be substituted with gif
    # print("Database count:", database.db_count())
    return redirect(url_for("new"))

@app.route("/old")
def old():
    return render_template("old_convo.html", name=database.get_all_threads())

if __name__ == "__main__":
    database.db_setup()
    app.debug = True
    app.run(port=8081)
