from flask import Flask, render_template, request, redirect, flash, Markup
import urllib2, json, random, os
import requests

app = Flask(__name__)
app.secret_key = os.urandom(128)

# root route // access and render NASA information
@app.route("/")
def home():
    key = "" # insert API KEY here
    entry = "What's your name" # insert entry here
    keyword = find_keyword(entry)
    url = "http://api.giphy.com/v1/gifs/search?api_key=" + key + "&limit=1&q=" + keyword
    # access data as a {}
    d = retrieve_data(url)
    return render_template('test.html', img = d['data'][0]['images']['original']['url'], keyword = keyword)

def find_keyword(entry):
    keywords = []
    entered_words = entry.strip().split()
    for i in entered_words:
        for j in blacklist:
            if i.lower() == j:
                break
            if j == blacklist[-1] and i.lower() != j:
                keywords.append(i)
    return random.choice(keywords)

def generate_blacklist():
    l = []
    with open(os.path.abspath("blacklist.txt"), "rU") as f: #uses absolute path given
        for line in f:
            a = line.strip().lower()
            # first gets rid of any leading/trailing characters, then gets rid of all whitesplace, then makes
            # list with name of API and API key
            l.append(a)
    return l

# opens URL to be read and returns JSON data as a dict/list
def retrieve_data(url):
    data = requests.get(url)
    d = data.json()
    #print json.dumps(d)
    return d

blacklist = generate_blacklist()

if __name__ == "__main__":
    app.debug = True
    app.run()
