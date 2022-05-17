import sys, pygame
BLACK = (0,0,0)
cells = list()
def handle_events(name):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                #toggle display
                pass

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pygame.init()
    size = width, height = 600, 400

    screen = pygame.display.set_mode(size)

    while True:
        handle_events()

        #simulation logic / Cell Movment

        screen.fill(BLACK)
        #draw cells and food
        #draw GUI
        pygame.display.flip()
