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
number1 = Tile(0, 0, "number1.png", 180, 180)
number2 = Tile(180, 0, "number2.png", 180, 180)
number3 = Tile(360, 0, "number3.png", 180, 180)
number4 = Tile(0, 180, "number4.png", 180, 180)
number5 = Tile(180, 180, "number5.png", 180, 180)
number6 = Tile(360, 180, "number6.png", 180, 180)
number7 = Tile(0, 360, "number7.png", 180, 180)
number8 = Tile(180, 360, "number8.png", 180, 180)


r = 255
g = 255
b = 255
run = True
start_game = False

orderfornumber1 = (180, 100)
orderfornumber2 = (360, 100)
orderfornumber3 = (0, 100)
orderfornumber4 = (180, 180)
orderfornumber5 = (360, 180)
orderfornumber6 = (0, 180)
orderfornumber7 = (180, 360)
orderfornumber8 = (360, 360)


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if spsb.rect.collidepoint(event.pos):
                start_game = True
            if number1.rect.collidepoint(event.pos) == True and start_game == True:
                number1.shrink_image(170, 170)
            else: 
                number1.shrink_image(180, 180)
            if start_game == True and number2.rect.collidepoint(event.pos):
                number2.shrink_image(170, 170)
            else:
                number2.shrink_image(180, 180)
            if start_game == True and number3.rect.collidepoint(event.pos):
                number3.shrink_image(170, 170)
            else:
                number3.shrink_image(180, 180)
            if start_game == True and number4.rect.collidepoint(event.pos):
                number4.shrink_image(170, 170)
            else:
                number4.shrink_image(180, 180)
            if start_game == True and number5.rect.collidepoint(event.pos):
                number5.shrink_image(170, 170)
            else:
                number5.shrink_image(180, 180)
            if start_game == True and number6.rect.collidepoint(event.pos):
                number6.shrink_image(170, 170)
            else:
                number6.shrink_image(180, 180)
            if start_game == True and number7.rect.collidepoint(event.pos):
                number7.shrink_image(170, 170)
            else:
                number7.shrink_image(180, 180)
            if start_game == True and number8.rect.collidepoint(event.pos):
                number8.shrink_image(170, 170)
            else: 
                number8.shrink_image(180, 180)
                
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

