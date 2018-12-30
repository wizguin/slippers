from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from world.database.Tables import User


class Database(object):
    """
    Creates a session with MySQL Database.
    """

    def __init__(self, config):
        engine = create_engine("mysql+mysqlconnector://{}:{}@{}/{}".format(
            *config["database"].values()))
        Session = sessionmaker(bind=engine)

        self.session = Session()

        # Table object references
        self.User = User

        # Test the connection
        try:
            self.session.execute("select 1")
            print("[Database] Connection successful")
        except:
            print("[Database] Could not connect to MySQL database")
