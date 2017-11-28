from flask import Flask, render_template, request, redirect, flash, Markup, url_for
import urllib2, json, random, os
from util import database, misc

app = Flask(__name__)
app.secret_key = os.urandom(128)

API_KEYS = misc.get_keys()
CLEVERBOT_KEY = API_KEYS["Cleverbot"]
CLEVERBOT_BASE_URL = "https://www.cleverbot.com/getreply?key=" + CLEVERBOT_KEY

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
    return jsonify(result=clever_output)

if __name__ == "__main__":
    database.db_setup()
    app.debug = True
    app.run()
