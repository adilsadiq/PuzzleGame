import pygame
from slidingstartoption import Slidingstartbutton
from tiles import Tile

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
number1 = Tile(0, 0, "number1.png", 50, 50)
number2 = Tile(50, 0, "number2.png", 50, 50)
number3 = Tile(100, 0, "number3.png", 50, 50)
number4 = Tile(0, 50, "number4.png", 50, 50)
number5 = Tile(50, 50, "number5.png", 50, 50)
number6 = Tile(100, 50, "number6.png", 50, 50)
number7 = Tile(0, 100, "number7.png", 50, 50)
number8 = Tile(50, 100, "number8.png", 50, 50)


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
        screen.blit(number4.image, number4.rect)
        screen.blit(number5.image, number5.rect)
        screen.blit(number6.image, number6.rect)
        screen.blit(number7.image, number7.rect)
        screen.blit(number8.image, number8.rect)
        
        pygame.draw.line(screen, line_color, (0, 0), (0, 550), width = 3)
        pygame.draw.line(screen, line_color, (0, 0), (550, 0), width = 5)
        pygame.draw.line(screen, line_color, (550, 0), (550, 550), width = 5)
        pygame.draw.line(screen, line_color, (0, 550), (550, 550), width = 5)

    pygame.display.update()

pygame.quit()
