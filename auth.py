import digraph
import sqlite3
import getpost

class Auth:
    def __init__(self):
        self.temp = digraph.Digraph()

    def authentication(self, user, data):
        V = 0
        print "For ", user
        for item in data:
            key, value = self.temp.add(item)
            if key is not None and value is not None:
                print key, value
                expected_value, variance = self.get_from_sql(user, key)
                print expected_value, variance

                if expected_value is None or variance is None:
                    print Username, "is a new user. Thre is no record in data base"
                    return False
                else:
                    if (expected_value - (3 * variance)) <= value and (expected_value + (3 * variance)) >= value:
                        V += 1
                        print V

        mV = float(V)/float(len(data))
        print V, "/", len(data), " = ", mV
        if mV <= 0.5:
            print "Access Denied", mV, " <= ", 0.5
        elif mV >= 0.6:
            print "Access Permitted", mV, " >= ", 0.5

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
user, data = getpost.get_postAuth_data()
bioAuth.authentication(user, data)
