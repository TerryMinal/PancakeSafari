from flask import Flask, render_template, request, redirect, flash, Markup, url_for, jsonify
import requests, os
from util import database, misc, giphy

app = Flask(__name__)
app.secret_key = os.urandom(128)

API_KEYS = misc.get_keys()
CLEVERBOT_KEY = API_KEYS["Cleverbot"]
CLEVERBOT_BASE_URL = "https://www.cleverbot.com/getreply?key=" + CLEVERBOT_KEY
GIPHY_KEY = API_KEYS["Giphy"]
GIPHY_BASE_URL = "http://api.giphy.com/v1/gifs/search?api_key=" + GIPHY_KEY + "&limit=1&q="

# root route // access and render NASA information
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/old")
def old():
    return render_template("old_convo.html", name=database.get_all_threads())

@app.route("/create_conv")
def create_conv():
    # checks if API keys are available
    if CLEVERBOT_KEY == "" or GIPHY_KEY == "":
        flash('API key(s) must be provided.')
        return redirect(url_for('home'))
    c = requests.get(CLEVERBOT_BASE_URL)
    j = c.json()
    clever_output = j["output"]
    clever_output = "cleverbot: " + clever_output
    cs = j["cs"] # cs is the conversation history parameter passed in the cleverbot url
    # print "\n" + cs + "\n"
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
    # print "\n" + clever_params["cs"] + "\n"
    # print clever_params["input"]
    user_input = clever_params["input"]
    database.update_thread(clever_params["conv_id"], "user: " + user_input)
    database.update_thread(clever_params["conv_id"], "cleverbot: " + clever_output)
    # print gif_array[0]
    gif_array = giphy.search_gif(user_input + " " + clever_output)
    print gif_array[0]
    return jsonify(result=clever_output, gif=gif_array[0],cs=j["cs"])

@app.route("/save_gif")
def save_gif():
    conv_id = request.args.get("conv_id")
    image = request.args.get("image")
    print "conv_id", conv_id
    print "image:", image
    database.update_image(conv_id, image)
    return jsonify(conv_id=conv_id, image=image);

if __name__ == "__main__":
    database.db_setup()
    app.debug = True
    app.run()
