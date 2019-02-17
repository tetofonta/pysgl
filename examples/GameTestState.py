import pygame

from pysgl.gamestate import GameState
from pysgl.game_manager import GameManager


class DemoState(GameState):

    def __init__(self, screen):
        super().__init__(screen)
        self.gameManager = GameManager()
        self.font = pygame.font.SysFont('helvetica', 20, 1)

    def draw(self):
        textToBlit = self.font.render(
            "BENVENUTO.\npremi a per continuare", True, (0, 100, 255, 255))
        self.screen.fill((0, 0, 0))
        self.screen.blit(textToBlit, (200, 200))

    def keyPressed(self, unicode, key, mod):
        if unicode == 'a':
            self.gameManager.currentGameState = "DemoState"

        if unicode == 'd':
            print(unicode, key, mod, self.gameManager.globals.playtime)
