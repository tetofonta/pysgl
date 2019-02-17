
import pygame

EVENTTYPE_TO_CBNAME = {
    # pygame.MOUSEMOTION: {'name': 'mouseMotion', 'params': ['pos', 'rel', 'buttons']},
    pygame.KEYDOWN: {'name': 'keyPressed', 'params': ['unicode', 'key', 'mod']},
}


class GameState:

    def __init__(self, screen):
        self.screen = screen

    def processEvent(self, event):
        eventDescription = EVENTTYPE_TO_CBNAME.get(event.type, None)
        if eventDescription is None:
            return

        cbName = eventDescription.get('name')

        cbParams = {}
        for param in eventDescription['params']:
            cbParams[param] = getattr(event, param)

        #print("{}({})".format(cbName, cbParams))
        cbFunction = getattr(self, cbName, None)

        if cbFunction:
            cbFunction(**cbParams)

    def update(self):
        pass

    def draw(self):
        pass


class GameStateManager(object):
    _state = {

    }

    def __init__(self):
        super()
        self.__dict__ = self._state
        self.states = {}
        self.current = None

    def add(self, gameState):
        print(gameState.__class__.__name__)
        self.states[gameState.__class__.__name__] = gameState

    def set_current(self, name):
        self.current = self.states.get(name)
