"""Digraph Class."""


class Digraph(object):
    """Digraph is extracted feature from raw data."""

    def __init__(self, pair):
        """Digraph contains id and value (duration of actions in miliseconds).

        Example:
        d = Digraph([(int,int),(int, int)])

        """
        self.id = pair[0][0] + pair[1][0]  # Int
        self.duration = abs(pair[0][1] - pair[1][1])  # Int
        self.m = self.duration  # mean or expected value
        self.v = 0  # variance
        self.c = 1  # counter

    def __eq__(self, obj):
        """Search by digraph id."""
        return self.id == obj.id

    def mutate(self, d):
        """Mutate digraph."""
        if self.id != d.get_id():
            return
        self.c += 1
        self.m = float(self.m + d.get_value())/float(self.c)
        self.v = float((d.get_value() - self.m) ** 2) / float(self.c - 1)

    def get_id(self):
        """Return Digraph ID."""
        return self.id

    def get_value(self):
        """Return Digraph Value."""
        return self.value

    def get_mean(self):
        """Return Mean."""
        return self.m

    def get_variance(self):
        """Return variance."""
        return self.v


class Digraph_Vector(object):
    """Digraph Vector is an vector of numerical features that represent unique keystroke."""

    def __init__(self):
        """Digraph Vector."""
        self.vector = []
        self.last_datapoint = None

    def insert(self, datapoint):
        """Insert raw data point from data stream to the Digraph_Vector.

        insert(datapoint) -> Void
        datapoint is tuple or list (). Example: [401400, 123743857]
        """
        n_d = self.normilize()
        if n_d is None:
            # Not enough datapoint to create digraph yet
            return

        idx = self.is_digraph_exists(n_d)
        if idx is None:
            self.vector.append(n_d)
        else:
            self.vector[idx].mutate(n_d)

    def get_digtraph_values(self, n_d):
        idx = self.is_digraph_exists(n_d)
        if idx is None:
            return None, None
        else:
            return self.vector[idx].get_mean(), self.vector[idx].get_variance()


    def is_digraph_exists(self, n_d):
        """Search for digrapn.

        Args:
            n_d: digraph to search

        Returns:
            idx in vectro list
            None is there's no digraph found

        """
        idx = next((d for d in self.vector if d.id == n_d.id), -1)  # finds index of existing digraph
        if idx == -1:
            return None
        else:
            return idx


    def normilize(self, datapoint):
        """Pairing dographs with overlap.

        normiliza(datapoint) -> Digraph()
        datapoint is tuple or list
        """
        if self.last_datapoint is None:
            self.last_datapoint = datapoint
            return None
        new_d = Digraph(self.last_datapoint, datapoint)
        self.last_datapoint = datapoint
        return new_d


    def size(self):
        """Size of the vector.

        size() -> int.
        """
        return len(self.vector)

    def get_vector(self):
        return self.vector


def main():
    """For testing."""

#     """
#     Yuliia|780651|0.0820000171661377|0.0|1
# Yuliia|890851|0.0840001106262207|0.0|1
# Yuliia|761760|0.0350833634535472|0.00127789499920226|4
# Yuliia|730651|0.0540000200271606|0.000576002334597092|2
# Yuliia|320781|0.296999931335449|0.0|1
# Yuliia|820321|0.0570001602172852|0.0|1
# Yuliia|730841|0.191999912261963|0.0|1
# Yuliia|780711|0.0470001697540283|0.0|1
# Yuliia|781780|0.0221666713555654|0.000620840826292954|5
# Yuliia|840821|0.195000171661377|0.0|1
# Yuliia|160691|0.118000030517578|0.0|1
# Yuliia|320831|0.829999923706055|0.0|1
# Yuliia|830321|0.130000114440918|0.00260098774339212|2
#     """
#     data = [[780651],[890851],[761760],[730651],[780651], [830321],[761760],[730651],]

if __name__ == "__main__":
    main()

    # def addModif(self, keyinput):
    #     """keyinput = [key+action,value]."""
    #     self.temp.insert(0, keyinput)  # insert keyinput to a queue.
    #     if len(self.temp) == 3:
    #         act1 = self.temp.pop()  # take away first value and store 2 others for next digraph
    #         act2 = self.temp[1]
    #         act3 = self.temp[0]
    #         time1 = abs(float(act1[1]) - float(act2[1]))
    #         time2 = abs(float(act3[1]) - float(act2[1]))
    #         time = float(time1/time2)
    #
    #         key = act1[0]  + act2[0] + act3[0]
    #         return key, time
    #     else:
    #         return None, None
    #
    # def add(self, keyinput):
    #         """keyinput = [[key+action,value],[],[]]."""
    #         self.temp.insert(0, keyinput)  # insert keyinput to a queue.
    #         if len(self.temp) == 2:
    #             act1 = self.temp.pop()  # take away first value and store 2 others for next digraph
    #             act2 = self.temp[0]
    #             time = abs(float(act1[1]) - float(act2[1]))
    #             key = act1[0] + act2[0]
    #
    #             return key, time
    #         else:
    #             return None, None
