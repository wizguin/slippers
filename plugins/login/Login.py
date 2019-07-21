import random
import string
from types import SimpleNamespace

from world.dataHandler.pluginManager.Plugin import Plugin


class Login(Plugin):
    """
    A plugin that enables logging into the game.
    """

    def __init__(self, users, rooms, packet):
        self.VERSION = "097"
        self.LOGIN_KEY_LENGTH = 15

        super(Login, self).__init__(users, rooms, packet)

    # Events

    def version_check(self, data, user):
        """Verifies the version of the user's user."""
        if data["msg"]["body"]["ver"]["@v"] == self.VERSION:
            user.send("<msg t='sys'><body action='apiOK' r='0'></body></msg>")

    def login(self, data, user):
        """Verifies login and connects user to game."""
        nick = data["msg"]["body"]["login"]["nick"].lower()
        pword = data["msg"]["body"]["login"]["pword"]

        # Fetch user data from database session, and build it into user object
        user.data = user.db.session.query(user.db.User).filter_by(username=nick).first()
        user.inventory = [i[0] for i in
                          user.db.session.query(user.db.Inventory.itemId).filter_by(userId=user.data.id)]

        # Incorrect login key
        if str(pword) != user.data.loginKey:
            user.send(["e", "-1", "101"])
        else:
            self.update_login_key(user)
            user.send(["l", "-1"])

    # Functions

    def update_login_key(self, user):
        """Generates a new login key for user."""
        user.data.loginKey = "".join(random.choice(string.ascii_letters + string.digits)
                                     for i in range(self.LOGIN_KEY_LENGTH))
        user.db.session.commit()
