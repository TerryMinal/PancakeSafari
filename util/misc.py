import os
#for miscallenous helper functions that don't belong in app.py

# returns a dictionary with format {API NAME: API KEY}
def get_keys():
    d = {}
    with open(os.path.abspath("keys.txt"), "rU") as f: #uses absolute path given
        for line in f:
            a = line.strip().replace(" ", "").split(":")
            # first gets rid of any leading/trailing characters, then gets rid of all whitesplace, then makes
            # list with name of API and API key
            d[a[0]] = a[1] # makes list into dictionary with format {API NAME: API KEY}
    return d

if __name__ == "__main__":
    print get_keys()
