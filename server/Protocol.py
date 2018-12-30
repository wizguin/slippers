import asyncio

from world.User import User


class Protocol(asyncio.Protocol):
    """
    Asyncio protocol, which manages connections and received data.
    Created every time a connection is made.
    """

    def __init__(self, users, db, handler):
        self.users = users
        self.db = db
        self.handler = handler

    def connection_made(self, transport):
        self.user = User(transport, self.db)
        self.users.append(self.user)

    def data_received(self, data):
        self.handler.handle(data.decode(), self.user)

    def connection_lost(self, exc):
        self.handler.close(self.user)
