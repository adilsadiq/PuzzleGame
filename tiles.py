import pygame

class Tile:
    def __init__(self, x, y, image, tilesizex, tilesizey):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (tilesizex, tilesizey))
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.select = False
    def move(self, screen):
        if self.select:
            self.rect.center = pygame.mouse.get_pos()
        screen.blit(self.image, self.rect)
    def shrink_image(self, newtilesizex, newtilesizey):
        self.image = pygame.transform.scale(self.image, (newtilesizex, newtilesizey))
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
