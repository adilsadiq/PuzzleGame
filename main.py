
import pygame
from slidingstartoption import Slidingstartbutton
from tiles import Tile

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Times New Roman', 15)
pygame.display.set_caption("Puzzle Game")

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600
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
tiles = [number1, number2, number3, number4, number5, number6, number7, number8]

r = 255
g = 255
b = 255
run = True
start_game = False
selected_tile = None
clock = pygame.time.Clock()


while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not start_game:
                if spsb.rect.collidepoint(event.pos):
                    start_game = True
            else:
                for tile in tiles:
                    if tile.rect.collidepoint(event.pos):
                        selected_tile = tile
                        break
        if event.type == pygame.MOUSEBUTTONUP:
            selected_tile = None
        if event.type == pygame.MOUSEMOTION and selected_tile:
            selected_tile.rect.center = event.pos

    screen.fill((r, g, b))
    if not start_game:
        screen.blit(display_start_message, (180, 0))
        screen.blit(spsb.image, spsb.rect)
    else:
        for tile in tiles:
            screen.blit(tile.image, tile.rect)
            
        pygame.draw.line(screen, line_color, (0, 0), (0, 600), width = 3)
        pygame.draw.line(screen, line_color, (0, 0), (600, 0), width = 5)
        pygame.draw.line(screen, line_color, (600, 0), (600, 600), width = 5)
        pygame.draw.line(screen, line_color, (0, 600), (600, 600), width = 5)

    pygame.display.update()

pygame.quit()



pygame.quit()

