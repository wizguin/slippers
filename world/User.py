from world.dataHandler.PacketManager import PacketManager


class User(object):
    """
    A class that defines a Club Penguin user, user data is passed in from a
    database along with other in game data.
    """

    def __init__(self, transport):
        self.transport = transport
        self.data = None

    def get_string(self):
        """Generates a user string, from user data."""
        return "|".join((self.data.id, self.data.username,
                        self.data.color, self.data.head,
                        self.data.face, self.data.neck,
                        self.data.body, self.data.hand,
                         self.data.feet, self.data.flag,
                         self.data.photo, self.data.x,
                         self.data.y, self.data.frame,
                         "1", "0"))

    def get_int_id(self, rooms):
        """Gets a user's internal room id."""
        if self.data.room in rooms:
            return rooms[self.data.room]["internal"]
        # Igloos
        elif int(self.data.room) > 999:
            return str(int(self.data.room) - 1000)
        # Unknown room
        else:
            return "-1"

    def send(self, packet):
        """Sends a packet to user."""
        if type(packet) is list:
            packet = PacketManager.make(*packet)
        self.transport.write((str(packet) + "\x00").encode())
