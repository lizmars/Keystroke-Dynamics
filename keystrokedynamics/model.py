"""Keystroke user model class."""

from digraph import Digraph_Vector
import uuid
from math import sqrt

DEFAULT_MAX_VECTOR_SIZE = 770  # TODO: config env


class Model(object):
    """Keystroke user model."""

    def __init__(self, model_size=DEFAULT_MAX_VECTOR_SIZE):
        """Create new user model with random user Id once instanse created.

        Example:
            new_model = Model()
            new_model = Model(model_size=1000)
            new_model.get_id()
            new_model.get_model() saves model as an tuple (id, vector)
            new_model.is_trained() True/Flase

        Args:
            model_size: size of digrap vector (default 770)

        Returns:
            Model() object

        """
        self.id = uuid.uuid4()
        self.vector = Digraph_Vector()
        self.max_vector_lenght = model_size
        self.trained = (self.vector == self.max_vector_lenght)

    def get_model(self):
        """Return user model as an tuple.

        get_model() -> (int, Digraph_Vector())
        """
        if self.trained:
            return (self.userId, self.vector)
        else:
            return None

    def get_vector(self):
        """Return vector.

        get_vector() -> Digraph_Vector()
        """
        return self.vector

    def get_id(self):
        """Return model id.

        get_id() -> int
        """
        return self.id

    def is_trained(self):
        """Check is user model fully trained.

        is_trained() -> Bool
        """
        self.trained = (self.vector.size == self.max_vector_lenght)
        return self.trained

    def expend_model_size(self, new_length):
        """Expend model size.

        expend_model_size(new_length) -> Void

        Raises:
            ValueError: Decreasing model size is unavaliable

        """
        if new_length < self.vector.size:
            # TODO: Add logging. Unable to extand
            raise ValueError("Decreasing model size is unavaliable")
        elif new_length == self.vector.size:
            self.trained = True
            return
        self.max_vector_lenght = new_length

    def train(self, data):
        pass

    def validate(self, datapoint):
        """Validate datapoint if it belongs to trained model."""
        if not self.trained:
            raise BaseException("Unable to verify datapont. Model not trained yet")

        new_d = self.vector.normilize(datapoint)
        if new_d is None:
            return -1
        m, v = self.vector.get_digtraph_values(new_d)
        if m is None or v is None:
            return -1

        if (m - (3 * sqrt(v))) <= new_d.get_value() and new_d.get_value() <= (m + (3 * sqrt(v))):
            return 1
        else:
            return 0


def main():
    """For testing."""
    model = Model()
    data = []
    for datapoint in data:
        model.get_vector.insert(datapoint)
    print(model.get_vector)

if __name__ == "__main__":
    main()

# class Profile:
#     def __init__(self):
#         self.profilelist = {}
#
#     def createProfile(self, username, rawdata):
#         self.profilelist[username] = Etalon()
#         self.profilelist[username].addToEtalon(rawdata)
#         return self.profilelist
#
#     def printProfile(self):
#         for item in self.profilelist.items():
#             print item[0]
#             item[1].printEtalon()

# def is_table_exists(name):
#     conn = sqlite3.connect('keystroke.sqlite')
#     cur = conn.cursor()
#     name = str(name.replace(" ", ""))
#     cur.execute("SELECT * FROM sqlite_master WHERE type='table' AND name=?", (name,))
#     row = cur.fetchone()
#     cur.close()
#     if row is not None:
#         print "Username alredy exists"
#         return True
#     else:
#         return False
#
# def push_to_sql(prof):
#     table  = "".join(prof.keys())
#     conn = sqlite3.connect('keystroke.sqlite')
#     cur = conn.cursor()
#
#     if is_table_exists(table):
#         return False
#
#     cur.execute('''
#     CREATE TABLE IF NOT EXISTS ''' + table +''' (digraph_id INTEGER, expected_value REAL, variance REAL, frequency INTEGER)''')
#     keys = prof["".join(prof.keys())].getkeys()
#     values = prof["".join(prof.keys())].getvalues()
#     for i in xrange(len(keys)):
#         cur.execute('''INSERT INTO ''' + table +''' (digraph_id, expected_value, variance, frequency)
#         VALUES ( ?, ?, ?, ? )''', (keys[i], values[i][0], values[i][1], values[i][2]))
#     conn.commit()
#     cur.close()
#     return True
#
# def new_profile(postfile):
#     myprofile = Profile()
#     #postfile = sys.argv[1]
#     user, data = getpost.get_post_data(postfile)
#
#     user_profile = myprofile.createProfile(user, data)
#     if push_to_sql(user_profile):
#         os.remove(postfile)
#         return True
#     else:
#         return False
