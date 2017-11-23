from flask import Flask, render_template, request, redirect, flash, Markup
import urllib2, json, random, os
from util import database, misc

app = Flask(__name__)
app.secret_key = os.urandom(128)

# root route // access and render NASA information
@app.route("/")
def home():
    database.db_setup()
    return render_template("home.html")

@app.route("/new")
def new():
    return render_template("create_convo.html")

@app.route("/old")
def old():
    return render_template("old_convo.html")

if __name__ == "__main__":
	app.debug = True
	app.run()
