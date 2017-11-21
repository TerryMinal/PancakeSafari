from flask import Flask, render_template, request, redirect, flash, Markup
import urllib2, json, random, os

app = Flask(__name__)
app.secret_key = os.urandom(128)

# root route // access and render NASA information
@app.route("/")
def home():
    # insert API KEY here
    url = "http://api.giphy.com/v1/gifs/search?api_key=&limit=1&q=money"
    # access data as a {}
    d = retrieve_data(url)
    return render_template('test.html', img = d['data'][0]['images']['original']['url'])


# opens URL to be read and returns JSON data as a dict/list
def retrieve_data(url):
    data = urllib2.urlopen(url)
    print "\n\nURL: "
    print data.geturl()
    print "\n\nINFO: "
    print data.info()
    d = json.loads(data.read())
    #print json.dumps(d)
    return d

if __name__ == "__main__":
    app.debug = True
    app.run()
