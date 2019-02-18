import pygame


class SpriteSheet(object):

    def __init__(self, filename):
        try:
            self.spritesheet = pygame.image.load(filename).convert()
            self.spritesheet.set_colorkey((0, 0, 0), pygame.RLEACCEL)
        except:
            pass

    def image_at(self, rect):
        return self.spritesheet.subsurface(rect)
