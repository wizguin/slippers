import json

import xmltodict
from observable import Observable

from world.dataHandler.PacketManager import PacketManager
from world.dataHandler.PluginManager import PluginManager


class DataHandler(object):
    """
    Handles game server data.
    """

    def __init__(self, users, database):
        self.users = users  # Socket assigned to user object
        self.database = database

        file = open("config/rooms.json", "r")
        self.rooms = json.loads(file.read())

        self.packet = PacketManager(self.rooms)
        self.obs = Observable()
        self.plugins = PluginManager(self)

        self.POLICY = "<cross-domain-policy><allow-access-from domain='*' to-ports='*' /></cross-domain-policy>"

    def handle(self, data, user):
        for data in filter(None, data.rstrip().split("\x00")):
            if data == "<policy-file-request/>":
                user.send(self.POLICY)
            elif data.startswith("<"):
                parsed = xmltodict.parse(data, dict_constructor=dict)
                self.fire_event(parsed["msg"]["body"]["@action"], parsed, user)
            elif data.startswith("%xt"):
                parsed = self.packet.parse(data)
                self.fire_event(parsed["action"], parsed, user)

    def fire_event(self, event, data, user):
        """Fires events to plugins."""
        #print("[DataHandler] Event fired: {} {}".format(event, data))
        self.obs.trigger("event", event, data, user)

    def close(self, user):
        """
        Closes a user, called by Protocol when a user disconnects.

        If a user is fully logged into the game, they must also be
        removed from their room.
        """
        if user.data:
            self.packet.send_room(["rp", user.get_int_id(self.rooms),
                                   user.data.id], user.data.room)
            self.rooms[user.data.room]["users"].remove(user)

        self.users.remove(user)
        del user
