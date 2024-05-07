import pygame
from slidingstartoption import Slidingstartbutton

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Times New Roman', 15)
pygame.display.set_caption("Puzzle Game")

SCREEN_HEIGHT = 550
SCREEN_WIDTH = 550
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

start_message = "Click the puzzle to start"
display_start_message = my_font.render(start_message, True, (0, 0, 0))


spsb = Slidingstartbutton(180, 100)


r = 255
g = 255
b = 255
run = True
start_game = False

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if spsb.rect.collidepoint(event.pos):
                start_game = True
            


    if start_game == False:
        screen.fill((r, g, b))
        screen.blit(display_start_message, (180, 0))
        screen.blit(spsb.image, spsb.rect)
    if start_game == True:
        screen.fill((r, g, b))
    pygame.display.update()

pygame.quit()
