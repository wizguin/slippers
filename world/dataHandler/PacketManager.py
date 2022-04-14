class PacketManager(object):
    """
    Deconstructs and constructs packets.
    """

    def __init__(self, rooms):
        self.rooms = rooms

    @staticmethod
    def make(packet, *args):
        return "%" + "%".join(["xt", packet, "%".join(map(str, args))]) + "%"

    @staticmethod
    def parse(packet):
        parsed = list(filter(None, packet.split("%")))  # Split packet by % and filter out None values
        if len(parsed) > 3:
            return {"action": parsed[2], "args": parsed[3:]}

    def send_room(self, packet, room_id):
        """Sends a packet to all users in a given room."""
        [i.send(packet) for i in self.rooms[room_id]["users"]]
