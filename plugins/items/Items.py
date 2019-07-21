from world.dataHandler.pluginManager.Plugin import Plugin


class Items(Plugin):
    """
    A plugin that enables adding and wearing items.
    """

    def __init__(self, users, rooms, packet):
        self.ITEMS = [
            "color",
            "head",
            "face",
            "neck",
            "body",
            "hand",
            "feet",
            "flag",
            "photo"
        ]

        super(Items, self).__init__(users, rooms, packet)

    def add_item(self, data, user):
        """Adds an item to user's inventory."""
        item_id = int(data["args"][1])

        if item_id in user.inventory:
            user.send(["e", "-1", "400"])
        else:
            user.inventory.append(item_id)
            user.db.session.add(user.db.Inventory(userId=user.data.id, itemId=item_id))
            user.db.session.commit()
            user.data.coins -= 0

            user.send(["ai", "-1", item_id, user.data.coins])

    def update_player(self, data, user):
        """Updates users worn items."""
        new_items = data["args"][1:]

        # Verify length of new_items
        if len(new_items) == len(self.ITEMS):
            # Update each item type in self.ITEMS with the new items
            for count, i in enumerate(new_items):
                # Verify item
                if int(i) in user.inventory or int(i) == 0:
                    setattr(user.data, self.ITEMS[count], i)

            user.db.session.commit()

            string = "|".join(map(str,
                                  (user.data.id,
                                   user.data.username,
                                   "|".join(new_items),
                                   user.x,
                                   user.y,
                                   user.frame)
                                  ))

            self.packet.send_room(["up", user.get_int_id(self.rooms),
                                   string], user.room)
