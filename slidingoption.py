import pygame

class Slidingoption:

  def __init__(self, x, y):
    self.x = x
    self.y = y
    DEFAULT_IMAGE_SIZE = (50, 50)
    self.image = pygame.image.load("Slidingoption.PNG")
    self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
    self.image_size = self.image.get_size()
    self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
