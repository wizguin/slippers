from world.dataHandler.pluginManager.Plugin import Plugin


class Items(Plugin):
    """"
    A plugin that enables adding and wearing items.
    """

    def __init__(self, users, rooms, packet):
        super(Items, self).__init__(users, rooms, packet)
