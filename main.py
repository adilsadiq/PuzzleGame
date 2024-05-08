import pygame
from slidingstartoption import Slidingstartbutton
from number1 import Number1

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
number1 = Number1(180, 100)

r = 255
g = 255
b = 255
run = True
start_game = False
border = False

orderfornumber1 = (180, 100)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if spsb.rect.collidepoint(event.pos):
                start_game = True
            if number1.rect.collidepoint(event.pos):
                border = True
                if border == True:
                    number1.move(180, 100)
                    number2 = pygame.image.load("number2.png")
                    screen.blit(number2, (180, 100))
                    pygame.display.update()

    if start_game == False:
        screen.fill((r, g, b))
        screen.blit(display_start_message, (180, 0))
        screen.blit(spsb.image, spsb.rect)
    if start_game == True:
        screen.fill((r, g, b))
        screen.blit(number1.image, number1.rect)
    pygame.display.update()

pygame.quit()
