from world.dataHandler.pluginManager.Plugin import Plugin


class Toy(Plugin):
    """
    A plugin that enables adding and removing a toy from a penguin.
    """

    def __init__(self, users, config, packet):
        super(Toy, self).__init__(users, config, packet)

    def add_toy(self, data, user):
        toy = data["args"][1]
        frame = data["args"][2]
        self.packet.send_room(["at", user.get_int_id(self.rooms),
                               user.data.id, toy, frame], user.room)

    def remove_toy(self, data, user):
        self.packet.send_room(["rt", user.get_int_id(self.rooms),
                               user.data.id], user.room)
