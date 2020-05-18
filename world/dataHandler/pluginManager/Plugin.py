class Plugin(object):
    """
    A base for a Slippers plugin, used to respond to DataHandler events.
    """

    def __init__(self, users, config, packet):
        self.users = users
        self.rooms = config["rooms"]
        self.items = config["items"]
        self.packet = packet
