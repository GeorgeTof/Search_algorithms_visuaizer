import pygame 

colors = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "red": (255, 0, 0),
    "green": (0, 255, 0),
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
cols = WIDTH // 10
rows = HEIGHT // 10
matrix = [[0 for _ in range(cols)] for _ in range(rows)]

exit = False
canvas = pygame.display.set_mode((WIDTH, HEIGHT)) 
mouse_pressed = 0


def loop():
    global exit, canvas, matrix, mouse_pressed
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True
        elif event.type == pygame.KEYDOWN:          # only for test
            if event.key == pygame.K_w:
                color = (0, 128, 255) 
                canvas.fill(color)
            if event.key == pygame.K_s:
                color = (255, 128, 0) 
                canvas.fill(color)
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
        print(mouse_pos)
        if(matrix[y][x] == 0):
            matrix[y][x] = 1

    



def main():
    pygame.init() 
    global exit, canvas, rows, cols, matrix
    
    pygame.display.set_caption("Lab 5 AI") 

    clock = pygame.time.Clock()
    

    while(exit == False):
        loop()
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
            if matrix[i][j] == 1:
                color = colors["red"]
            pygame.draw.rect(canvas, color, (*position, square_size, square_size))

        


if __name__ == "__main__":
    main()