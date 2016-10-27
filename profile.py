import json

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

    def printEtalon(self):
        for item in self.keylog.items():
            print item

class Profile:
    def __init__(self):
        self.profilelist = {}

    def createProfile(self, username, rawdata):
        self.profilelist[username] = Etalon()
        self.profilelist[username].addToEtalon(rawdata)

    def printProfile(self):
        for item in self.profilelist.items():
            print item[0]
            item[1].printEtalon()


#user = "Yuliia"
rinput = [["40", "1", "0.02"],["40", "0", "0.025"], ["23", "1", "0.029"],
            ["23", "0", "0.02299"], ["33",'1','0.03'], ["33",'0','0.04'],
            ["40", "1", "0.04006"],["40", "0", "0.05004"],["40", "1", "0.04126"],
            ["40", "0", "0.01052306"],["33",'1','0.03634'],["33",'0','0.0400032'],
            ["23", "0", "0.02299"], ["33",'1','0.03'], ["33",'0','0.04']]

myprofile = Profile()

with open("postreq.json", 'r') as f:
    postdata = f.read()

rawinput = json.loads(postdata)
user = "".join(rawinput.keys())
print user
data = []
for item in rawinput[user]:
    values = item.values()
    keylog = values[0].split(",")
    timelog = values[1].split(",")
    for i in xrange(len(keylog)):
        #print values[0][i]
        data.append([keylog[i],timelog[i]])
#print data

myprofile.createProfile(user, data)
myprofile.printProfile()
