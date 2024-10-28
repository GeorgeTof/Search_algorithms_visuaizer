import pygame 
import random

colors = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "red": (255, 0, 0),
    "green": (20, 100, 20),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "cyan": (0, 255, 255),
    "magenta": (255, 0, 255),
    "gray": (128, 128, 128),
    "orange": (255, 165, 0),
    "purple": (128, 0, 128),
    "pink": (255, 192, 203),
    "brown": (139, 69, 19),
}

WIDTH = 1000
HEIGHT = 600
DEST = 2
WALL = 1
START = -2
cols = WIDTH // 10
rows = HEIGHT // 10
matrix = [[0 for _ in range(cols)] for _ in range(rows)]

init_done = False
quit = False
canvas = pygame.display.set_mode((WIDTH, HEIGHT)) 
mouse_pressed = 0
start = (10, 20)
dest = (30,40)


def init_loop():
    global init_done, canvas, matrix, mouse_pressed, quit
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            quit = True
        elif event.type == pygame.KEYDOWN:          # only for test
            if event.key == pygame.K_w:
                color = (0, 128, 255) 
                canvas.fill(color)
            if event.key == pygame.K_s:
                color = (255, 128, 0) 
                canvas.fill(color)
            if event.key == pygame.K_RETURN:
                init_done = 1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # mouse left click
                print("Left mouse button clicked at", event.pos)
                mouse_pressed = 1
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mouse_pressed = 0
    if (mouse_pressed):
        mouse_pos = pygame.mouse.get_pos()
        x = mouse_pos[0] // 10
        y = mouse_pos[1] // 10
        if(matrix[y][x] == 0):
            matrix[y][x] = WALL

    



def main():
    pygame.init() 
    global init_done, canvas, rows, cols, matrix
    
    pygame.display.set_caption("Maze runner") 

    clock = pygame.time.Clock()
    
    init_maze()

    while(init_done == False and quit == False):
        init_loop()
        draw_matrix()
        pygame.display.update() 
        clock.tick(60)


def draw_matrix():
    global rows, cols, matrix, canvas, colors
    square_size = 10
    for i in range (rows):
        for j in range (cols):
            position = (j*square_size, i*square_size)
            if matrix[i][j] == 0:
                color = colors["white"]
            if matrix[i][j] == WALL:
                color = colors["green"]
            if matrix[i][j] == DEST:
                color = colors["red"]
            if matrix[i][j] == START:
                color = colors["blue"]
            pygame.draw.rect(canvas, color, (*position, square_size, square_size))


def init_maze():
    global start, dest, matrix, rows, cols
    x = random.randint(1, rows-1)
    x2 = random.randint(1, rows-1)
    while (abs(x2-x) < 5):
        x2 = random.randint(1, rows-1)
    
    y = random.randint(1, cols-1)
    y2 = random.randint(1, cols-1)
    while (abs(y2-y) < 5):
        y2 = random.randint(1, cols-1)

    start = (x, y)
    dest = (x2, y2)

    matrix[x][y] = START
    matrix[x2][y2] = DEST




if __name__ == "__main__":
    main()