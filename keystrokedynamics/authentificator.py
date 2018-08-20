"""Keystroke Dynamics Authenticator."""

DEFAULT_THRESHOLD = 0.65
WAIT_DELTA = 0.1
DEFAULT_CONSISTENCY_VECTOR_SIZE = 40


class Authenticator(object):
    """Authenticator class."""

    def __init__(self, user, threshold=DEFAULT_THRESHOLD):
        """Initialize authentificator with User and optional threshold.

        Args:
            user: User() object
            threshold(optional): authentication threshold (default 0.65)
        """
        self.threshold = threshold
        self.min_threshold = threshold - WAIT_DELTA
        self.user = user
        self.probability = None
        self.norm_vector = []

    def validate(self, data):
        for d in data:
            v = self.user.get_model.validate(d)
            if v != -1:
                self.norm_vector.append(v)
        self.probability = float(sum(self.norm_vector))/float(len(self.norm_vector))


    def get_probability(self):
        """Current probability."""
        return self.probability

    def get_decision(self):
        """Authentication decision based on threshold."""
        if self.probability <= self.min_threshold:
            print("Access Denied: " + str(self.probability) + " <= " + str(self.min_threshold))
            self.norm = 0
            return 0
        elif self.probability >= self.threshold:
            print("Access Permitted", self.probability, " >= ", self.threshold)
            self.norm = 0
            return 1
        else:
            return -1
