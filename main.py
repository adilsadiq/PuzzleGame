import pygame
from slidingstartoption import Slidingstartbutton
from number1 import Number1
from number2 import Number2
from number3 import Number3
# from number4 import Number4
# from number5 import Number5
# from number6 import Number6
# from number7 import Number7
# from number8 import Number8

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Times New Roman', 15)
pygame.display.set_caption("Puzzle Game")

SCREEN_HEIGHT = 550
SCREEN_WIDTH = 550
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
line_color = (0, 0, 0)


start_message = "Click the sliding puzzle to start"
display_start_message = my_font.render(start_message, True, (0, 0, 0))


spsb = Slidingstartbutton(180, 100)
number1 = Number1(180, 100)
number2 = Number2(200, 150)
number3 = Number3(200, 200)

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
                
    if start_game == False:
        screen.fill((r, g, b))
        screen.blit(display_start_message, (180, 0))
        screen.blit(spsb.image, spsb.rect)
    if start_game == True:
        screen.fill((r, g, b))
        screen.blit(number1.image, number1.rect)
        screen.blit(number2.image, number2.rect)
        screen.blit(number3.image, number3.rect)
        pygame.draw.line(screen, line_color, (100, 100), (500, 100), width = 5)
    pygame.display.update()

pygame.quit()
