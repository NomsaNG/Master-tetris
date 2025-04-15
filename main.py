# Tetris in PyGame
# Imports
import pygame
import random
import sys

pygame.init()

# Constant Variables
WIDTH, HEIGHT = 300, 500
FPS = 35

CELL = 20
ROWS = (HEIGHT - 120) // CELL
COLS = WIDTH // CELL

# Game Settings ~ screen, clock, title
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Tetris")

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BG_COLOR = (31, 25, 76)
GRID = (31, 25, 132)
WIN = (50, 230, 50)
LOSE = (252, 91, 122)

# Load / Store images
ASSETS = {
    1: pygame.image.load("assets/1.png"),
    2: pygame.image.load("assets/2.png"),
    3: pygame.image.load("assets/3.png"),
    4: pygame.image.load("assets/4.png"),
}

# Fonts
font = pygame.font.SysFont("verdana", 50)
font_small = pygame.font.SysFont("verdana", 15)








# Shape Class

    # Constructor
        

    # image ~ Choose correct image 

    # rotate ~ Rotate image


# Game Class
    # Constructor

    # make grid ~ Create the grid
    # make shape ~ Create a new shape
    # move ~ Move the shape
    # rotate ~ Rotate the shape
    # drop ~ Drop the shape
    # check_collision ~ Check for collision with walls and other shapes
    # clear_lines ~ Clear completed lines
    # game_over ~ Check if game is over

# Main Game Loop
def main():
    run = True
    while run: 
        SCREEN.fill(BG_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            
        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
    pygame.quit()