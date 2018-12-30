import asyncio

from server.Protocol import Protocol


class Server(object):
    """
    Initialises a server.
    """

    def __init__(self, config, world_id, users, db, handler):
        self.loop = asyncio.get_event_loop()
        self.coro = self.loop.create_server(lambda: Protocol(users, db, handler),
                                            config["world"][world_id]["host"],
                                            config["world"][world_id]["port"])
        self.server = self.loop.run_until_complete(self.coro)

        print("[Server] Server started on {}".format(self.server.sockets[0].getsockname()))

        try:
            self.loop.run_forever()
        except KeyboardInterrupt:
            print("[Server] Closing server")
        finally:
            self.server.close()
            self.loop.close()
