import pygame
from slidingoption import Slidingoption

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Times New Roman', 15)
pygame.display.set_caption("Puzzle Game")

SCREEN_HEIGHT = 550
SCREEN_WIDTH = 550
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

option_message = "Choose your puzzle!"
display_option_message = my_font.render(option_message, True, (0, 0, 0))

slidingpuzzleoption = Slidingoption(40, 40)

r = 255
g = 255
b = 255
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

  
    screen.fill((r, g, b))
    screen.blit(display_option_message, (185, 0))
    screen.blit(slidingpuzzleoption.image, slidingpuzzleoption.rect)

    pygame.display.update()

pygame.quit()
