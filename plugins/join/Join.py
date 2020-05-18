from random import choice

from world.dataHandler.pluginManager.Plugin import Plugin


class Join(Plugin):
    """
    A plugin that enables joining the server and rooms.
    """

    def __init__(self, users, config, packet):
        super(Join, self).__init__(users, config, packet)

    # Events

    def join_server(self, data, user):
        """Initial joining of the server."""
        # User will spawn in one of following rooms
        user.room = choice(("100", "300", "800", "804"))
        user.send(["js", "-1", "1", "1", "0", "0"])
        self.add(user)

    def join_room(self, data, user):
        """Joining a new room."""
        # Filters out | to prevent string injection
        data["args"] = [i.replace("|", "") for i in data["args"]]

        self.remove(user)

        user.room = data["args"][1]
        user.x = data["args"][2]
        user.y = data["args"][3]
        user.frame = "0"

        self.add(user)

    # TODO: add functionality
    def join_player(self, data, user):
        """Joining a player's igloo."""
        self.remove(user)

        user.room = "100"
        user.x = "0"
        user.y = "0"
        user.frame = "0"

        self.add(user)

    # Functions

    def add(self, user):
        """Adds a player in to their new room."""
        int_id = user.get_int_id(self.rooms)
        self.rooms[user.room]["users"].append(user)

        # Games
        if self.rooms[user.room]["isGame"] == "true":
            user.send(["jg", int_id, user.room])
        # Rooms
        else:
            user.send(["jr", int_id, user.room, self.get_strings(user.room)])
            self.packet.send_room(["ap", int_id, user.get_string()], user.room)

    def remove(self, user):
        """Removes a player from their current room."""
        self.packet.send_room(["rp", user.get_int_id(self.rooms),
                               user.data.id], user.room)
        self.rooms[user.room]["users"].remove(user)

    def get_strings(self, room_id):
        """Gets strings of all users in a given room."""
        return "%".join([i.get_string() for i in self.rooms[room_id]["users"]])
