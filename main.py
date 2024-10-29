import pygame 
import random
from queue import Queue, LifoQueue

colors = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "red": (255, 0, 0),
    "green": (20, 100, 20),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "cyan": (0, 180, 180),
    "magenta": (255, 0, 255),
    "gray": (128, 128, 128),
    "orange": (255, 165, 0),
    "purple": (128, 0, 128),
    "pink": (255, 192, 203),
    "brown": (139, 69, 19),
}

WIDTH = 300
HEIGHT = 150
DEST = 3
FRONTIER = 2
WALL = 1
PATH = -3
START = -2
VISITED = -1
FREE = 0
cols = WIDTH // 10
rows = HEIGHT // 10
matrix = [[0 for _ in range(cols)] for _ in range(rows)]

init_done = False
quit = False
canvas = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock() 
mouse_pressed = 0
start = (1, 2)
dest = (3,4)
mode = 'b'

def valid_neighbours(point):
    global cols, rows
    x = point[0]
    y = point[1]
    list = []
    if(x-1 >=0):
        list.append((x-1, y))
    if(y+1 < cols):
        list.append((x, y+1))
    if(x+1 < rows):
        list.append((x+1, y))
    if(y-1 >= 0):
        list.append((x, y-1))
    return list

def matrix_of(index):
    global matrix
    return matrix[index[0]][index[1]]

def matrix_assign(index, value):
    global matrix
    matrix[index[0]][index[1]] = value

def reconstruct_path(parent):
    current = dest
    while current != start:
        current = parent[current]
        matrix_assign(current, PATH)
    draw_matrix()
    pygame.display.update()

def dfs(current):
    global clock
    st = LifoQueue()
    matrix_assign(current, FRONTIER)
    st.put(current)
    parent = {current:None}
    while not st.empty():
        current = st.get()
        nb = valid_neighbours(current)
        found = False
        for x in nb:
            if matrix_of(x) == DEST:
                found = True
                parent[x] = current
                break
            if matrix_of(x) == FREE:
                matrix_assign(x, FRONTIER)
                parent[x] = current
                st.put(x)
        matrix_assign(current, VISITED)
        draw_matrix()
        pygame.display.update()
        clock.tick(60)
        if(found):
            break
    reconstruct_path(parent)


def bfs(current):
    global clock
    q = Queue()
    matrix_assign(current, FRONTIER)
    q.put(current)
    parent = {current:None}
    while not q.empty():
        current = q.get()
        nb = valid_neighbours(current)
        found = False
        for x in nb:
            if matrix_of(x) == DEST:
                found = True
                parent[x] = current
                break
            if matrix_of(x) == FREE:
                matrix_assign(x, FRONTIER)
                parent[x] = current
                q.put(x)
        matrix_assign(current, VISITED)
        draw_matrix()
        pygame.display.update()
        clock.tick(60)
        if(found):
            break
    reconstruct_path(parent)
        


def init_loop():
    global init_done, canvas, matrix, mouse_pressed, quit, mode
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            quit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                mode = 'd'
                print("Mode changed to DFS")
            if event.key == pygame.K_b:
                mode = 'b'
                print("Mode changed to BFS")
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

def end_loop():
    global quit
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            quit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                quit = True
            if event.key == pygame.K_RETURN:
                quit = True
    
def main():
    pygame.init() 
    global init_done, canvas, rows, cols, matrix, start, clock
    
    pygame.display.set_caption("Maze runner") 
    
    init_maze()

    while(init_done == False and quit == False):
        init_loop()
        if(quit == True):
            return
        draw_matrix()
        pygame.display.update() 
        clock.tick(60)

    if mode == 'd':
        dfs(start)
    elif mode == 'b':
        bfs(start)

    while(quit == False):
        end_loop()
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
            if matrix[i][j] == VISITED:
                color = colors["gray"]
            if matrix[i][j] == FRONTIER:
                color = colors["orange"]
            if matrix[i][j] == PATH:
                color = colors["cyan"]
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