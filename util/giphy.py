from flask import Flask, render_template, request, redirect, flash, Markup
import random, os
import requests
import misc

blacklist = ['and', 'because', 'to', 'from', 'with', 'who', 'whom', 'come', 'get', 'give', 'go', 'keep', 'let', 'make', 'put', 'seem', 'take', 'be', 'do', 'have', 'may', 'will', 'about', 'across', 'after', 'among', 'at', 'before', 'between', 'by', 'in', 'off', 'on', 'over', 'through', 'to', 'under', 'up', 'down', 'as', 'for', 'of', 'till', 'than', 'a', 'the', 'all', 'any', 'many', 'every', 'ever', 'no', 'other', 'some', 'such', 'that', 'this', 'i', 'he', 'she', 'they', 'them', 'you', 'but', 'or', 'if', 'though', 'while', 'how', 'however', 'when', 'whenever', 'where', 'wherever', 'why', 'again', 'against', 'far', 'forward', 'further', 'farther', 'here', 'near', 'now', 'out', 'still', 'then', 'there', 'together', 'well', 'almost', 'enough', 'even', 'little', 'much', 'not', 'continuously', 'only', 'quite', 'so', 'very', 'tomorrow', 'yesterday', 'please', 'yes', 'none', 'less', 'more', 'what', 'whatever', 'too', 'therefore', 'thus', 'consequently', 'are', 'similarly', 'additionally', 'furthermore', 'thereby', 'likewise', 'despite', 'regardless', 'notwithstanding', 'nonetheless', 'nevertheless', 'is', 'can']

API_KEYS = misc.get_keys()
GIPHY_KEY = API_KEYS["Giphy"]
GIPHY_BASE_URL = "http://api.giphy.com/v1/gifs/search?api_key=" + GIPHY_KEY + "&limit=1&q="

# With given entry, return random GIF and corresponding keyword as [gif_url, keyword]
def search_gif(entry):
    try:
        key = "" # insert API KEY here
        keyword = find_keyword(entry)
        # return empty list if there is no keyword
        if keyword == "":
            return []
        url = GIPHY_BASE_URL + keyword
        # access data as a {}
        d = retrieve_data(url)
        # print d
        url = d['data'][0]['images']['original']['url']
        return [url, keyword]
    except:
        print "NO GIF FOUND"
        return []
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
    # print d
    return d

if __name__ == "__main__":
    print blacklist
