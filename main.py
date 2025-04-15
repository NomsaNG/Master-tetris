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
class Shape:
    VERSION ={
        'I': [[1, 5, 9, 13],[4, 5, 6, 7]],
        'Z': [[4, 5, 9, 10],[2, 6, 5, 9]],
        'S': [[6, 7, 9, 10],[1, 5, 6, 10]],
        'L': [[1, 2, 5, 9],[0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        'J': [[1, 2, 6, 10],[5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        'T': [[1, 4, 5, 6],[1, 4, 5, 9], [4, 5, 6, 10], [1, 5, 6, 10]],
        'O': [[1, 2, 5, 6]]
    }

    SHAPES  = ['I', 'Z', 'S', 'L', 'J', 'T', 'O']

    # Constructor
    def __init__(self):
        self.x = 0
        self.y = 0
        self.type = random.choice(self.SHAPES)
        self.shape = self.VERSION[self.type]
        self.color = random.randint(1, 4)
        self.orientation = 0
        

    # image ~ Choose correct image 
    def image(self):
        return self.shape[self.orientation]

    # rotate ~ Rotate image
    def rotate(self):
        self.orientation = (self.orientation + 1) % len(self.shape)


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