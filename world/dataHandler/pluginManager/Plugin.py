class Plugin(object):
    """
    A base for a Slippers plugin, used to respond to DataHandler events.
    """

    def __init__(self, users, rooms, packet):
        self.users = users
        self.rooms = rooms
        self.packet = packet
