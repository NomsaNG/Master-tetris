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
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT),  pygame.NOFRAME)
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
    def __init__(self, x, y):
        self.x = x
        self.y = y
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
class Tetris:
    # Constructor
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.score = 0
        self.level = 1
        self.grid = [[0 for j in range(cols)] for i in range(rows)]
        self.next = None
        self.end = False
        self.new_shape()

    # make grid ~ Create the grid
    def make_grid(self):
        for i in range(self.rows+1):
            pygame.draw.line(SCREEN, GRID, (0, CELL*i), (WIDTH, CELL*i))
        for j in range(self.cols+1):
            pygame.draw.line(SCREEN, GRID, (CELL*j, 0), (CELL*j, HEIGHT-120))

    # make shape ~ Create a new shape
    def new_shape(self):
        if not self.next:
            self.next = Shape(5,0)
        self.figure = self.next
        self.next = Shape(5,0)
    
    # COLLISION ~ Check for collision
    def collision(self) -> bool:
        for i in range(4):
            for j in range(4):
                if (i*4 + j) in self.figure.image():
                    block_row = self.figure.y + i
                    block_col = self.figure.x + j
                    if (block_row >= self.rows or block_col >= self.cols or block_col < 0 or self.grid[block_row][block_col] > 0):
                        return True
        return False
    
    # Remove Row
    def remove_row(self):
        rerun = False

        for y in range(self.rows-1, 0, -1):
            completed = True

            for x in range(0, self.cols):
                if self.grid[y][x] == 0:
                    completed = False
                    
            if completed:
                del self.grid[y]
                self.grid.insert(0, [0 for i in range(self.cols)])
                self.score += 1
                if self.score % 10 == 0:
                    self.level += 1
                rerun = True
        if rerun:
            self.remove_row()

    # Freeze
    def freeze(self):
        for i in range(4):
            for j in range(4):
                if (i*4 + j) in self.figure.image():
                    self.grid[i+self.figure.y][j+self.figure.x] = self.figure.color
       
        self.remove_row()
        self.new_shape()
        if self.collision():
            self.end = True
           
    # Move Down
    def move_down(self):
        self.figure.y += 1
        if self.collision():
            self.figure.y -= 1
            self.freeze()

    # Move Left
    def move_left(self):
        self.figure.x -= 1
        if self.collision():
            self.figure.x += 1

    # Move Right
    def move_right(self):
        self.figure.x += 1
        if self.collision():
            self.figure.x -= 1

    # freefall
    def free_fall(self):
        while not self.collision():
            self.figure.y += 1
        self.figure.y -= 1
        self.freeze()

    # Rotate
    def rotate(self):
        orientation = self.figure.orientation
        self.figure.rotate()
        if self.collision():
            self.figure.orientation = orientation
            
    def end_game(self):
        popup = pygame.Rect(50, 140, WIDTH-100, HEIGHT-350)
        pygame.draw.rect(SCREEN, BLACK, popup)
        pygame.draw.rect(SCREEN,LOSE, popup, 2)

        game_over = font_small.render("Game Over", True, WHITE)
        option1 = font_small.render("Press Q to Quit", True, WHITE)
        option2 = font_small.render("Press R to Restart", True, WHITE)
        SCREEN.blit(game_over, (popup.centerx - game_over.get_width()//2, popup.y + 20))
        SCREEN.blit(option1, (popup.centerx - option1.get_width()//2, popup.y + 80))
        SCREEN.blit(option2, (popup.centerx - option2.get_width()//2, popup.y + 120))

# Main Game Loop
def main():
    run = True
    tetris = Tetris(ROWS, COLS)
    counter = 0
    move = True
    space_pressed = False
    while run: 
        SCREEN.fill(BG_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
             # Event Loop

            keys = pygame.key.get_pressed()
            if not tetris.end:
                if keys[pygame.K_LEFT]:
                    tetris.move_left()
                elif keys[pygame.K_RIGHT]:
                    tetris.move_right()
                elif keys[pygame.K_DOWN]:
                    tetris.move_down()
                elif keys[pygame.K_UP]:
                    tetris.rotate()
                elif keys[pygame.K_SPACE]:
                    space_pressed = True  
            if keys[pygame.K_r]:
                tetris.__init__(ROWS, COLS)
            if keys[pygame.K_ESCAPE] or keys[pygame.K_q]:
                run = False
                 

        # Allows block to fall at constant rate
        counter += 1
        if counter >= 15000:
            counter = 0

        if move:
            if counter % (FPS // (tetris.level*2)) == 0:
                if not tetris.end:
                    if space_pressed:
                        tetris.free_fall()
                        space_pressed = False
                    else:
                        tetris.move_down()
                    


        tetris.make_grid()

        # Keep fallen shapes on screen
        for x in range(ROWS):
            for y in range(COLS):
                if tetris.grid[x][y] > 0:
                    value = tetris.grid[x][y]
                    image = ASSETS[value]
                    SCREEN.blit(image, (CELL * y, CELL * x))
                    pygame.draw.rect(SCREEN, WHITE, (CELL * y, CELL * x, CELL, CELL), 1)


        # Show Shape on Game Screen
        if tetris.figure:
            for i in range(4):
                for j in range(4):
                    if (i *4 + j) in tetris.figure.image():
                        shape = ASSETS[tetris.figure.color]
                        x = CELL * (tetris.figure.x + j)
                        y = CELL * (tetris.figure.y + i)
                        SCREEN.blit(shape, (x, y))
                        pygame.draw.rect(SCREEN, WHITE, (x, y, CELL, CELL), 1)
        
        # Control Panel
        if tetris.next:
            for i in range(4):
                for j in range(4):
                    if (i *4 + j) in tetris.next.image():
                        image = ASSETS[tetris.next.color]
                        x = CELL * (tetris.next.x + j -4)
                        y = HEIGHT - 100 + CELL * (tetris.next.y + i)
                        SCREEN.blit(shape, (x, y))
                        pygame.draw.rect(SCREEN, WHITE, (x, y, CELL, CELL), 1)

        if tetris.end:
            tetris.end_game()
       
        # Score
        score_text = font.render(str(tetris.score), True, WHITE)
        level_text = font_small.render("Level: " + str(tetris.level), True, WHITE)
        SCREEN.blit(score_text, (250 - score_text.get_width()//2, HEIGHT - 110))
        SCREEN.blit(level_text, (250 - level_text.get_width()//2, HEIGHT - 30))



        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
    pygame.quit()