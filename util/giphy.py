from flask import Flask, render_template, request, redirect, flash, Markup
import urllib2, json, random, os
import requests
from util import misc

API_KEYS = misc.get_keys()
GIPHY_KEY = API_KEYS["Cleverbot"]
GIPHY_BASE_URL = "http://api.giphy.com/v1/gifs/search?api_key=" + GIPHY_KEY + "&limit=1&q="

# With given entry, return random GIF and corresponding keyword as [gif_url, keyword]
def search_gif(entry):
    key = "" # insert API KEY here
    keyword = find_keyword(entry)
    # return empty list if there is no keyword
    if keyword == "":
        return []
    url = GIPHY_BASE_URL + keyword
    # access data as a {}
    d = retrieve_data(url)
    url = d['data'][0]['images']['original']['url']
    return [url, keyword]

def find_keyword(entry):
    keywords = []
    entered_words = entry.strip().split()
    for i in entered_words:
        for j in blacklist:
            # if word found, continue and do not append entered word to keywords
            if i.lower() == j:
                break
            # if the last word of the blacklist does not match, append entered word to keywords
            if j == blacklist[-1] and i.lower() != j:
                keywords.append(i)
    if keywords == []:
        return ""
    return random.choice(keywords)

def generate_blacklist():
    l = []
    with open(os.path.abspath("blacklist.txt"), "rU") as f: #uses absolute path given
        for line in f:
            # remove spaces and lowercases each word to be appended into list l
            a = line.strip().lower()
            l.append(a)
    return l

# opens URL to be read and returns JSON data as a dict/list
def retrieve_data(url):
    data = requests.get(url)
    d = data.json()
    return d

blacklist = generate_blacklist()

if __name__ == "__main__":
    print blacklist
