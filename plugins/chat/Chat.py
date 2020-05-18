from world.dataHandler.pluginManager.Plugin import Plugin


class Chat(Plugin):
    """
    A plugin that enables sending messages and emotes.
    """

    def __init__(self, users, config, packet):
        super(Chat, self).__init__(users, config, packet)

    def send_message(self, data, user):
        """Sends a message to a room, limiting it to 80 characters."""
        msg = data["args"][2]
        self.packet.send_room(["sm", user.get_int_id(self.rooms),
                               user.data.id, msg[0:80]], user.room)

    def send_safe(self, data, user):
        msg = data["args"][1]
        self.packet.send_room(["ss", user.get_int_id(self.rooms),
                               user.data.id, msg], user.room)

    def send_joke(self, data, user):
        msg = data["args"][1]
        self.packet.send_room(["sj", user.get_int_id(self.rooms),
                               user.data.id, msg], user.room)

    def send_emote(self, data, user):
        emote = data["args"][1]
        self.packet.send_room(["se", user.get_int_id(self.rooms),
                               user.data.id, emote], user.room)
