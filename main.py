import sys, pygame
BLACK = (0,0,0)

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
        handle_events('PyCharm')
        screen.fill(BLACK)
        #draw stuff
        #draw GUI
        pygame.display.flip()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
