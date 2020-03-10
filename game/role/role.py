from .flags import Flags
import asyncio
class Role:

    def __init__(self, player):
        self.player = player
        self.flags = {}
        self.lovers = {}

    async def on_gamestart(self, game):
        pass

    async def on_nightfall(self, game):
        pass

    async def on_sunrise(self, game):
        pass

    async def on_guard(self, game):
        ## TODO: you have been guarded
        self.flags.add(Flags.GUARDED)

    async def on_grace(self, game):
        ## TODO: you have been graced
        self.flags.add(Flags.GRACED)

    async def on_trial(self, game):
        ## TODO: you are on trial
        if Flags.GRACED in self.flags:
            pass

        #DO DEATH

    async def on_hang(self, game):
        ## TODO: you have been hanged
        pass

    async def on_playerdeath(self, game, player, muderer_class):
        game.players_alive.remove(player)

    async def on_ressurect(self, game):
        pass

    async def on_changerole(self, game, role):
        player.role = role

    async def on_inhibit(self, game):
        pass

    async def on_inlove(self, game, player):
        self.lovers.add(player)