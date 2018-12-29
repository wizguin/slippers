import random
import string
from types import SimpleNamespace

from world.dataHandler.pluginManager.Plugin import Plugin


class Login(Plugin):
    """"
    A plugin that enables logging into the game.
    """

    def __init__(self, users, database, rooms, packet):
        self.VERSION = "097"
        self.LOGIN_KEY_LENGTH = 15
        # User will spawn in one of following rooms
        self.SPAWN_ROOMS = ("100", "300", "800", "804")

        super(Login, self).__init__(users, database, rooms, packet)

    # Events

    def version_check(self, data, user):
        """Verifies the version of the user's user."""
        if data["msg"]["body"]["ver"]["@v"] == self.VERSION:
            user.send("<msg t='sys'><body action='apiOK' r='0'></body></msg>")

    def login(self, data, user):
        nick = data["msg"]["body"]["login"]["nick"].lower()
        pword = data["msg"]["body"]["login"]["pword"]
        user_data = self.database.select("users", "username", nick)

        # Incorrect login key
        if str(pword) != user_data["loginKey"]:
            user.send(["e", "-1", "101"])
        else:
            self.update_login_key(nick)
            # Builds user data into the user object as a namespace
            user.data = SimpleNamespace(** {**user_data, **{"room": random.choice(self.SPAWN_ROOMS),
                                                            "x": "0", "y": "0", "frame": "0"}})
            user.send(["l", "-1"])

    # Functions

    def update_login_key(self, user):
        new_key = "".join(random.choice(string.ascii_letters + string.digits) for i in range(self.LOGIN_KEY_LENGTH))
        self.database.update("users", "loginKey", new_key, "username", user)
