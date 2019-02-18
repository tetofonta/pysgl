import pygame

from .gameglobals import Globals
from .gamestate import GameStateManager

PYGAME_MODULES_LOAD = {
    'FONTS': lambda: pygame.font.init(),

}

PYGAME_MODULES_UNLOAD = {
    'FONTS': lambda: pygame.font.quit(),

}


class GameManager(object):

    _internal_state = {

    }

    def __init__(self):
        self.__dict__ = self._internal_state
        self.pygameModules = []
        pygame.init()
        self.globals = Globals()
        self.globals.playtime = 0.0
        self.globals.FPS = 60
        self.globals.clock = pygame.time.Clock()
        self.gameStateManager = GameStateManager()
        self.SCREEN_SIZE = (800, 600)
        self.caption = "test"
        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)
        pygame.display.set_caption("DEMO 01")

    def init(self, module):
        self.pygameModules.append(module)
        PYGAME_MODULES_LOAD[module]()

    def addGameState(self, gameStateClass):
        # if len(self.gameStateManager.states) == 0:
        #    self.gameStateManager.set_current(gameStateClass.__name__)
        self.gameStateManager.add(gameStateClass(self.screen))

    def SetCurrentGameState(self, gameState):
        self.gameStateManager.set_current(gameState)

    def GetCurrentGameState(self):
        return self.gameStateManager.current

    currentGameState = property(GetCurrentGameState, SetCurrentGameState)

    def run(self):
        do_loop = True
        while do_loop:
            # print(self.currentGameState)
            gameState = self.currentGameState
            dt = self.globals.clock.tick(self.globals.FPS)
            self.globals.playtime += dt / 1000.0
            # events
            for event in pygame.event.get():
                gameState.processEvent(event)
                if event.type == pygame.QUIT:
                    do_loop = False
            # aggiornamento
            gameState.update()
            # draw
            gameState.draw()
            pygame.display.flip()

        for module in self.pygameModules:
            PYGAME_MODULES_UNLOAD[module]()
        pygame.quit()
