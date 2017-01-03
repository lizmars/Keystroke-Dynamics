import json
import sqlite3
import digraph
import getpost
import sys
import os

class Etalon:
    def __init__(self):
        self.keylog = {} # formed digraphs

    def addToEtalon(self, data):
        newDigraph = digraph.Digraph()
        for item in data:
            #key, value = newDigraph.addModif(item)
            key, value = newDigraph.add(item)
            if key is not None and value is not None:
                if self.keylog.has_key(key):
                    self.keylog[key][2] = int(self.keylog.get(key)[2]) + 1
                    self.keylog[key][0] = float(self.keylog[key][0] + value) / float(self.keylog[key][2])
                    self.keylog[key][1] = float((value - self.keylog[key][0]) ** 2) / float(self.keylog[key][2] - 1)
                else:
                    self.keylog[key] = [value, "0", "1"]
    def getitems(self):
        return self.keylog.items()
    def getkeys(self):
        return self.keylog.keys()
    def getvalues(self):
        return self.keylog.values()

    def printEtalon(self):
        for item in self.keylog.items():
            print item

class Profile:
    def __init__(self):
        self.profilelist = {}

    def createProfile(self, username, rawdata):
        self.profilelist[username] = Etalon()
        self.profilelist[username].addToEtalon(rawdata)
        return self.profilelist

    def printProfile(self):
        for item in self.profilelist.items():
            print item[0]
            item[1].printEtalon()

def is_table_exists(name):
    conn = sqlite3.connect('keystroke.sqlite')
    cur = conn.cursor()
    name = str(name.replace(" ", ""))
    cur.execute("SELECT * FROM sqlite_master WHERE type='table' AND name=?", (name,))
    row = cur.fetchone()
    cur.close()
    if row is not None:
        print "Username alredy exists"
        return True
    else:
        return False

def push_to_sql(prof):
    table  = "".join(prof.keys())
    conn = sqlite3.connect('keystroke.sqlite')
    cur = conn.cursor()

    if is_table_exists(table):
        return False

    cur.execute('''
    CREATE TABLE IF NOT EXISTS ''' + table +''' (digraph_id INTEGER, expected_value REAL, variance REAL, frequency INTEGER)''')
    keys = prof["".join(prof.keys())].getkeys()
    values = prof["".join(prof.keys())].getvalues()
    for i in xrange(len(keys)):
        cur.execute('''INSERT INTO ''' + table +''' (digraph_id, expected_value, variance, frequency)
        VALUES ( ?, ?, ?, ? )''', (keys[i], values[i][0], values[i][1], values[i][2]))
    conn.commit()
    cur.close()
    return True

def new_profile(postfile):
    myprofile = Profile()
    #postfile = sys.argv[1]
    user, data = getpost.get_post_data(postfile)

    user_profile = myprofile.createProfile(user, data)
    if push_to_sql(user_profile):
        os.remove(postfile)
        return True
    else:
        return False
