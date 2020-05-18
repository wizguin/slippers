import json

import xmltodict
from observable import Observable

from world.dataHandler.PacketManager import PacketManager
from world.dataHandler.PluginManager import PluginManager


class DataHandler(object):
    """
    Handles game server data.
    """

    def __init__(self, users):
        self.users = users  # Socket assigned to user object

        rooms = open("config/rooms.json", "r")
        self.rooms = json.loads(rooms.read())

        items = open("config/items.json", "r")
        self.items = json.loads(items.read())

        self.packet = PacketManager(self.rooms)
        self.obs = Observable()
        self.plugins = PluginManager(self)

        self.POLICY = "<cross-domain-policy><allow-access-from domain='*' to-ports='*' /></cross-domain-policy>"

    def handle(self, data, user):
        """
        Handles incoming XML and XT packets.
        """
        for data in filter(None, data.rstrip().split("\x00")):
            print(data)

            if data == "<policy-file-request/>":
                user.send(self.POLICY)

            # Handling XML
            elif data.startswith("<"):
                try:
                    parsed = xmltodict.parse(data, dict_constructor=dict)
                    self.fire_event(parsed["msg"]["body"]["@action"], parsed, user)
                except Exception:
                    print("[DataHandler] Bad XML: {}".format(data))

            # Handling XT
            elif data.startswith("%xt%"):
                try:
                    parsed = self.packet.parse(data)
                    self.fire_event(parsed["action"], parsed, user)
                except Exception:
                    print("[DataHandler] Bad XT: {}".format(data))

    def fire_event(self, event, data, user):
        """Fires events to plugins."""
        self.obs.trigger("event", event, data, user)

    def close(self, user):
        """
        Closes a user, called by Protocol when a user disconnects.

        If a user is fully logged into the game, they must also be
        removed from their room.
        """

        if user.data:

            if user.room:
                if user in self.rooms[user.room]["users"]:
                    self.packet.send_room(["rp", user.get_int_id(self.rooms),
                                user.data.id], user.room)
                    self.rooms[user.room]["users"].remove(user)

            # Commit changes to database
            user.db.session.commit()

        self.users.remove(user)
        del user
