from world.dataHandler.pluginManager.Plugin import Plugin


class Actions(Plugin):
    """
    A plugin that enables penguin movement and actions.
    """

    def __init__(self, users, config, packet):
        super(Actions, self).__init__(users, config, packet)

    def send_position(self, data, user):
        user.x = data["args"][1]
        user.y = data["args"][2]
        user.frame = "0"
        self.packet.send_room(["sp", user.get_int_id(self.rooms),
                               user.data.id, user.x, user.y], user.room)

    def send_frame(self, data, user):
        frame = data["args"][1]
        frame_type = data["action"][-1]

        if frame_type == "f":
            user.frame = frame

        self.packet.send_room(["s" + frame_type, user.get_int_id(self.rooms),
                               user.data.id, frame], user.room)

    def snowball(self, data, user):
        x, y = data["args"][1:]
        self.packet.send_room(["sb", user.get_int_id(self.rooms),
                               user.data.id, x, y], user.room)
