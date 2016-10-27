import json
import sqlite3

class Digraph:
    def __init__(self):
        self.temp = [] # temporarily queue

    def addModif(self,keyinput): #keyinput = [key+action,value]
        self.temp.insert(0,keyinput) #insert keyinput to a queue.
        if len(self.temp) == 3:
            act1 = self.temp.pop() # take away first value and store 2 others for next digraph
            act2 = self.temp[1]
            act3 = self.temp[0]
            time1 = abs(float(act1[1]) - float(act2[1]))
            time2 = abs(float(act3[1]) - float(act2[1]))
            time = float(time1/time2)
            #print "time 1 = ", time1
            #print "time 2 = ", time2
            #print "time = time1/time2 = ", time
            key = act1[0]  + act2[0] + act3[0]
            return key, time
        else:
            return None, None

    def add(self,keyinput): #keyinput = [key+action,value]
            self.temp.insert(0,keyinput) #insert keyinput to a queue.
            if len(self.temp) == 2:
                act1 = self.temp.pop() # take away first value and store 2 others for next digraph
                act2 = self.temp[0]
                time = abs(float(act1[1]) - float(act2[1]))
                key = act1[0]  + act2[0]

                return key, time
            else:
                return None, None

class Etalon:
    def __init__(self):
        self.keylog = {} # formed digraphs

    def addToEtalon(self, data):
        newDigraph = Digraph()
        for item in data:
            #key, value = newDigraph.addModif(item)
            key, value = newDigraph.add(item)
            if key is not None and value is not None:
                if self.keylog.has_key(key):
                    self.keylog[key][2] = int(self.keylog.get(key)[2]) + 1
                    self.keylog[key][0] = float(self.keylog[key][0] + value) / float(self.keylog[key][2])
                    self.keylog[key][1] = (float(value - self.keylog[key][0]) ** 2) / float(self.keylog[key][2] - 1)
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

def getpostdata():
    with open("postreq.json", 'r') as f:
        postdata = f.read()
    rawinput = json.loads(postdata)
    username = "".join(rawinput.keys())
    rdata = []
    for item in rawinput[username]:
        values = item.values()
        keylog = values[0].split(",")
        timelog = values[1].split(",")
        for i in xrange(len(keylog)):
            rdata.append([keylog[i],timelog[i]])
    return username, rdata

def pushtosql(prof):
    conn = sqlite3.connect('keystroke.sqlite')
    cur = conn.cursor()

    #cur.execute('''
    #DROP TABLE IF EXISTS Users''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS Users (user TEXT, digraph_id INTEGER, expected_value REAL, variance REAL, frequency INTEGER)''')
    uname = "".join(prof.keys())
    keys = prof["".join(prof.keys())].getkeys()
    values = prof["".join(prof.keys())].getvalues()
    for i in xrange(len(keys)):
        cur.execute('''INSERT INTO Users (user, digraph_id, expected_value, variance, frequency)
        VALUES ( ?, ?, ?, ?, ? )''', (uname, keys[i], values[i][0], values[i][1], values[i][2]))
    conn.commit()

myprofile = Profile()

user, data = getpostdata()

user_profile = myprofile.createProfile(user, data)

pushtosql(user_profile)

#myprofile.printProfile()
