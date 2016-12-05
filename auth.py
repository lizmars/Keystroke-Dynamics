import digraph
import sqlite3
import getpost
import sys
import math

class Auth:
    def __init__(self):
        self.temp = digraph.Digraph()

    def authentication(self, user, data):
        V = 0
        print "For ", user
        for item in data:
            key, value = self.temp.add(item)
            if key is not None and value is not None:
                #print key, value
                expected_value, variance = self.get_from_sql(user, key)
                #print expected_value, variance

                if expected_value is None or variance is None:
                    print user, "is a new user. Thre is no record in data base"
                    return False
                else:
                    if (expected_value - (3 * math.sqrt(variance))) <= value and value <= (expected_value + (3 * math.sqrt(variance))):
                        print str(expected_value - (3 * math.sqrt(variance)))," <= ", value , " <= ", str(expected_value + (3 * math.sqrt(variance)))
                        V += 1
                        #print V

        mV = float(V)/float(self.sql_num_rows(user))
        print V, "/", self.sql_num_rows(user), " = ", mV
        if mV <= 0.5:
            print "Access Denied", mV, " <= ", 0.5
            V = 0
            return True
        elif mV >= 0.6:
            print "Access Permitted", mV, " >= ", 0.6
            V = 0
            return False
        else:
            return "Wait"

    def get_from_sql(self, username, digraph):
        conn = sqlite3.connect('keystroke.sqlite')
        cur = conn.cursor()
        username = str(username.replace(" ", ""))

        if not self.is_table_exists(username):
            #print Username, "is a new user. Thre is no record in data base"
            return None, None #new user

        cur.execute("SELECT expected_value, variance FROM "+username+" WHERE digraph_id = ? ", (digraph,))
        row = cur.fetchone()
        if row is None:
            return 0, 0 #new digraph
        else:
            return row[0], row[1]

    def sql_num_rows(self, name):
        conn = sqlite3.connect('keystroke.sqlite')
        cur = conn.cursor()
        cur.execute("SELECT * FROM " + name)
        return len(cur.fetchall())

    def is_table_exists(self, name):
        conn = sqlite3.connect('keystroke.sqlite')
        cur = conn.cursor()
        name = str(name.replace(" ", ""))
        cur.execute("SELECT * FROM sqlite_master WHERE type='table' AND name=?", (name,))
        row = cur.fetchone()
        cur.close()
        if row is not None:
            return True
        else:
            return False


bioAuth = Auth()
postfile = sys.argv[1]
#postfile = "Auth_CitrixPOST.json"
user, data = getpost.get_postAuth_data(postfile)
if bioAuth.authentication(user, data) == "Wait":
    pass
else:
    os.remove(postfile)
