from world.dataHandler.PacketManager import PacketManager


class User(object):
    """
    A class that defines a user, user data is passed in from a
    database along with other in game data.
    """

    def __init__(self, transport, db):
        self.transport = transport
        self.db = db
        self.data = None
        self.inventory = None

        self.room = None
        self.x = "0"
        self.y = "0"
        self.frame = "0"
        self.coins_earned = None

    def get_string(self):
        """
        Generates a string from user data,
        map is used to string all variables.
        """
        return "|".join(map(str,
                            (self.data.id,
                             self.data.username,
                             self.data.color,
                             self.data.head,
                             self.data.face,
                             self.data.neck,
                             self.data.body,
                             self.data.hand,
                             self.data.feet,
                             self.data.flag,
                             self.data.photo,
                             self.x,
                             self.y,
                             self.frame,
                             "1",
                             "0")
                            ))

    def get_int_id(self, rooms):
        """Gets a user's internal room id."""
        if self.room in rooms:
            return rooms[self.room]["internal"]
        # Igloos
        elif int(self.room) > 999:
            return str(int(self.room) - 1000)
        # Unknown room
        else:
            return "-1"

    def send(self, packet):
        """Sends a packet to user."""
        if type(packet) is list:
            packet = PacketManager.make(*packet)
        self.transport.write((str(packet) + "\x00").encode())
