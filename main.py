import pygame 

WIDTH = 1000
HEIGHT = 600

exit = False
canvas = pygame.display.set_mode((WIDTH, HEIGHT)) 


def loop():
    global exit, canvas
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                # Change color when 'w' is pressed
                color = (0, 128, 255)  # New color (e.g., light blue)
                canvas.fill(color)
    



def main():
    pygame.init() 
    global exit, canvas
    
    # TITLE OF CANVAS 
    pygame.display.set_caption("Lab 5 AI") 

    # Set up clock for frame rate control
    clock = pygame.time.Clock()

    while(exit == False):
        loop()
        pygame.display.update() 
        clock.tick(60)


if __name__ == "__main__":
    main()