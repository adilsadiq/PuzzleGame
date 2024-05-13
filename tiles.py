import pygame

class Tile:      
  def __init__(self, x, y, image, tilesizex, tilesizey):
    self.x = x
    self.y = y
    self.image = pygame.image.load(image)
    self.image = pygame.transform.scale(self.image, (tilesizex, tilesizey))
    self.image_size = self.image.get_size()
    self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
