from flask import Flask, render_template, request, redirect, flash, Markup, url_for, jsonify
import urllib2, json, random, os
from util import misc
from util import database
import requests

app = Flask(__name__)
app.secret_key = os.urandom(128)

API_KEYS = misc.get_keys()
CLEVERBOT_KEY = API_KEYS["Cleverbot"]
CLEVERBOT_BASE_URL = "https://www.cleverbot.com/getreply?key=" + CLEVERBOT_KEY
print CLEVERBOT_BASE_URL


# c = requests.get(CLEVERBOT_BASE_URL)
# j = c.json()
# CS = j["cs"] # cs is the conversation history parameter passed in the cleverbot url
# CONV_ID = j["conversation_id"]
# OUTPUT = j["output"]
#
# for key in j:
#     print key +": " + j[key]

# @app.route("/")
# def home():
#     return redirect(url_for create_conv)

@app.route("/create_conv")
def create_conv():
    c = requests.get(CLEVERBOT_BASE_URL)
    j = c.json()
    clever_output = j["output"]
    clever_output = "cleverbot: " + clever_output + ","
    cs = j["cs"] # cs is the conversation history parameter passed in the cleverbot url
    conv_id = j["conversation_id"]
    database.create_thread(conv_id, clever_output, "")
    return redirect(url_for("conversation", conv_id = conv_id, cs = cs, clever_output = clever_output))

# displays webpage
@app.route("/conversation?conv_id=<conv_id>?cs=<cs>?initial_output=<clever_output>")
def conversation(conv_id, cs, clever_output):
    return render_template("convo.html", conv_id = conv_id, cs = cs, clever_output = clever_output)

# responds to an ajax call that gives a user input and sends the outut of cleverbot
@app.route("/clever_output")
def clever_output():
    clever_params = {"input": request.args.get("clever_input"), "conv_id": request.args.get("conv_id"), "cs":request.args.get("cs")}
    c = requests.get(CLEVERBOT_BASE_URL, params=clever_params)
    j = c.json()
    clever_output = j["output"]
    # database.update_thread(request.form["conv_id"], clever_output)
    print "\n\nit worked up to here\n"
    return jsonify(result=clever_output)

    

if __name__ == "__main__":
	app.debug = True
	app.run()
