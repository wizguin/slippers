from world.dataHandler.pluginManager.Plugin import Plugin


class Join(Plugin):
    """
    A plugin that enables joining the server and rooms.
    """

    def __init__(self, users, database, rooms, packet):
        super(Join, self).__init__(users, database, rooms, packet)

    # Events

    def join_server(self, data, user):
        """Initial joining of the server."""
        user.send(["js", "-1", "0", "1", "0", "0"])
        self.add(user)

    def join_room(self, data, user, x="0", y="0"):
        """Joining a new room."""
        # Filters out | to prevent string injection
        data["args"] = [i.replace("|", "") for i in data["args"]]

        self.remove(user)

        user.data.room = data["args"][1]
        user.data.x = x
        user.data.y = y
        user.frame = "0"

        self.add(user)

    # Functions

    def add(self, user):
        """Adds a player in to their new room."""
        int_id = user.get_int_id(self.rooms)

        self.rooms[user.data.room]["users"].append(user)
        user.send(["jr", int_id, user.data.room, self.get_strings(user.data.room)])
        self.packet.send_room(["ap", int_id, user.get_string()], user.data.room)

    def remove(self, user):
        """Removes a player from their current room."""
        self.packet.send_room(["rp", user.get_int_id(self.rooms),
                               user.data.id], user.data.room)
        self.rooms[user.data.room]["users"].remove(user)

    def get_strings(self, room_id):
        """Gets strings of all users in a given room."""
        return "%".join([i.get_string() for i in self.rooms[room_id]["users"]])
