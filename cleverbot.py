# from flask import Flask, render_template, request, redirect, flash, Markup
import urllib2, json, random, os
from util import misc
from util import database
import requests

# app = Flask(__name__)
# app.secret_key = os.urandom(128)

API_KEYS = misc.get_keys()
CLEVERBOT_KEY = API_KEYS["Cleverbot"]
CLEVERBOT_BASE_URL = "https://www.cleverbot.com/getreply?key=" + CLEVERBOT_KEY
print CLEVERBOT_BASE_URL


c = requests.get(CLEVERBOT_BASE_URL)
j = c.json()
CS = j["cs"] # cs is the conversation history parameter passed in the cleverbot url
CONV_ID = j["conversation_id"]
OUTPUT = j["output"]
    
# for key in j:
#     print key, j[key]
# @app.route("/")
# def home():


# if __name__ == "__main__":
	# app.debug = True
	# app.run()
