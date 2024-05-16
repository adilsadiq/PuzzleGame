import pygame

class Tile:      
  def __init__(self, x, y, image, tilesizex, tilesizey):
    self.x = x
    self.y = y
    self.image = pygame.image.load(image)
    self.image = pygame.transform.scale(self.image, (tilesizex, tilesizey))
    self.image_size = self.image.get_size()
    self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
  def move(self, new_x, new_y):
    self.x = new_x
    self.y = new_y
    self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
  def shrink_image(self, newtilesizex, newtilesizey):
    self.image = pygame.transform.scale(self.image, (newtilesizex, newtilesizey))
    self.image_size = self.image.get_size()
    self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
