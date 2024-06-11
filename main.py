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
tile_size = 180
number2 = Tile(0, 0, "number2.png", tile_size, tile_size)
number5 = Tile(180, 0, "number5.png", tile_size, tile_size)
number8 = Tile(360, 0, "number8.png", tile_size, tile_size)
number3 = Tile(0, 180, "number3.png", tile_size, tile_size)
number4 = Tile(180, 180, "number4.png", tile_size, tile_size)
number1 = Tile(360, 180, "number1.png", tile_size, tile_size)
number6 = Tile(0, 360, "number6.png", tile_size, tile_size)
number7 = Tile(180, 360, "number7.png", tile_size, tile_size)

correct_positions = {
    number1: (0, 0),
    number2: (180, 0),
    number3: (360, 0),
    number4: (0, 180),
    number5: (180, 180),
    number6: (360, 180),
    number7: (0, 360),
    number8: (180, 360)
}

tiles = [number2, number5, number8, number3, number4, number1, number6, number7]
empty_space = pygame.Rect(360, 360, tile_size, tile_size)
r = 255
g = 255
b = 255
run = True
start_game = False
selected_tile = None
the_clock = pygame.time.Clock()

def is_adjacent(tile_rect, empty_space):
    if (tile_rect.x == empty_space.x and abs(tile_rect.y - empty_space.y) == tile_size) or \
       (tile_rect.y == empty_space.y and abs(tile_rect.x - empty_space.x) == tile_size):
        return True
    return False
    
def check_win():
    for tile in tiles:
        if tile.rect.center != correct_positions[tile]:
            return False
    return True
    
while run:
    the_clock.tick(60)
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
                        if is_adjacent(tile.rect, empty_space):
                            selected_tile = tile
                            break
                            
        if event.type == pygame.MOUSEBUTTONUP:
            if selected_tile and is_adjacent(selected_tile.rect, empty_space):
                selected_tile.rect, empty_space = empty_space, selected_tile.rect
            selected_tile = None
    
    screen.fill((r, g, b))
    if not start_game:
        screen.blit(display_start_message, (180, 0))
        screen.blit(spsb.image, spsb.rect)
    else:
        for tile in tiles:
            screen.blit(tile.image, tile.rect)
        pygame.draw.line(screen, line_color, (0, 0), (0, 600), width=3)
        pygame.draw.line(screen, line_color, (0, 0), (600, 0), width=5)
        pygame.draw.line(screen, line_color, (600, 0), (600, 600), width=5)
        pygame.draw.line(screen, line_color, (0, 600), (600, 600), width=5)
    if check_win():
        win_message = my_font.render("You Win!", True, (0, 0, 0))
        screen.blit(win_message, (220, 270))
        pygame.display.update()


    pygame.display.update()

pygame.quit()
