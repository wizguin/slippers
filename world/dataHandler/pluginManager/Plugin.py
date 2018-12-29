class Plugin(object):
    """
    A base for a Slippers plugin, used to respond to DataHandler events.
    """

    def __init__(self, users, database, rooms, packet):
        self.users = users
        self.database = database
        self.rooms = rooms
        self.packet = packet
