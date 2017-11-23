# from flask import Flask, render_template, request, redirect, flash, Markup
import urllib2, json, random, os
from util import misc
from util import database
import request

app = Flask(__name__)
app.secret_key = os.urandom(128)

API_KEYS = misc.get_keys()
CLEVERBOT_KEY = API_KEYS["Cleverbot"]
CLEVERBOT_BASE_URL = "https://www.cleverbot.com/getreply?key=" + CLEVERBOT_KEY
print CLEVERBOT_BASE_URL



# @app.route("/")
# def home():


# if __name__ == "__main__":
	# app.debug = True
	# app.run()
