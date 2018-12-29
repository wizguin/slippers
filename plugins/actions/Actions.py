from world.dataHandler.pluginManager.Plugin import Plugin


class Actions(Plugin):
    """"
    A plugin that enables penguin movement and actions.
    """

    def __init__(self, users, database, rooms, packet):
        super(Actions, self).__init__(users, database, rooms, packet)

    def send_position(self, data, user):
        user.data.x = data["args"][1]
        user.data.y = data["args"][2]
        user.frame = "0"
        self.packet.send_room(["sp", user.get_int_id(self.rooms),
                               user.data.id, user.data.x, user.data.y], user.data.room)

    def send_frame(self, data, user):
        frame = data["args"][1]
        frame_type = data["action"][-1]

        if frame_type == "f":
            user.data.frame = frame

        self.packet.send_room(["s" + frame_type, user.get_int_id(self.rooms),
                               user.data.id, frame], user.data.room)

    def snowball(self, data, user):
        x, y = data["args"][1:]
        self.packet.send_room(["sb", user.get_int_id(self.rooms),
                               user.data.id, x, y], user.data.room)
