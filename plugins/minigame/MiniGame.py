from math import ceil

from world.dataHandler.pluginManager.Plugin import Plugin


class MiniGame(Plugin):
    """
    A plugin that handles the outcome of minigames.
    """

    def __init__(self, users, config, packet):
        self.MAX_COINS = 1000000
        # Minigames that give the score as their coin reward
        self.DEFAULT_SCORE_GAMES = ("904", "905", "906", "912", "916", "917", "918", "919", "950", "952")

        super(MiniGame, self).__init__(users, config, packet)

    # Events

    def game_over(self, data, user):
        """Finishes the minigame and prepares to exit."""
        score = int(data["args"][1])

        if self.rooms[user.room]["isGame"] == "true":
            # Disconnect the user if coin overdose is triggered
            if self.coin_overdose(score):
                user.send(["e", "-1", "1"])
                user.transport.close()
            else:
                # Coins to pay the user
                user.coins_earned = self.coins_earned(user.room, score)
                user.send(["zo", "-1"])

    def add_coins(self, data, user):
        """
        Adds coins and exits minigame. The user's coins will be updated by the following rules:

        1. Choose the maximum value between 0 and the new coin total,
        0 is used to ensure the user's coins does not go negative.

        2. Cap the new coin total at MAX_COINS.
        """
        if user.coins_earned and self.rooms[user.room]["isGame"] == "true":
            coins = max(0, min(int(user.data.coins) + user.coins_earned, self.MAX_COINS))
            user.data.coins = coins
            user.db.session.commit()

            user.send(["ac", "-1", user.data.coins])

        user.coins_earned = None

    # Functions

    def coin_overdose(self, score):
        """Detects if the user is gaining coins too quickly."""
        return False

    def coins_earned(self, room_id, score):
        """Calculated coins earned."""
        if room_id in self.DEFAULT_SCORE_GAMES:
            return score
        # Other games will give coins based on the score / 10
        else:
            return ceil(score / 10)
