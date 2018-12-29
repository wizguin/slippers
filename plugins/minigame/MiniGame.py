from world.dataHandler.pluginManager.Plugin import Plugin


class MiniGame(Plugin):
    """"
    A plugin that handles the outcome of minigames.
    """

    def __init__(self, users, database, rooms, packet):
        super(MiniGame, self).__init__(users, database, rooms, packet)
