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
