"""User class."""

from model import Model
from utils.db_helper import insert
import uuid

from sqlite3 import DatabaseError
from sqlite3 import Error
from sqlite3 import IntegrityError
from sqlite3 import NotSupportedError
from sqlite3 import OperationalError
from sqlite3 import ProgrammingError


class User(object):
    """User object in web application."""

    def __init__(self, name):
        """Create new user.

        Args:
            name: given user name
        """
        self.user_name = name
        self.id = uuid.uuid4()
        self.model = Model()

    def save_to_db(self):
        """Save user to SQLite."""
        try:
            insert(self)
        except (Error, DatabaseError, OperationalError, IntegrityError, ProgrammingError, NotSupportedError):
            # Log it
            raise DatabaseError

    def get_model(self):
        """Return user model object."""
        return self.fmodel

    def get_user_id(self):
        """Return user id.

        get_user_id() -> String
        """
        return self.id

    def get_user_name(self):
        """Return user name.

        get_user_name() -> String
        """
        return self.user_name

    def load_user_by_name(self, name, db_path):
        """Load user from DB by user name."""
        pass

    def load_user_by_id(self, name, db_path):
        """Load user from DB by user Id."""
        pass
