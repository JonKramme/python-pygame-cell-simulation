import sys, pygame

from Cell import Cell
from Food import Food

BLACK = (0, 0, 0)
cells = list()


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # toggle display
                pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pygame.init()
    size = width, height = 600, 400

    screen = pygame.display.set_mode(size)
    # create Cells etc.
    f = Food((200, 200), 200.0, 20.0, 500, 1, (0, 148, 255), (0, 74, 127))
    c = Cell((300, 300), 200.0, 20.0, 500, 1, (182, 255, 0), (38, 127, 0), 0, 2, (0, 0), 2, 2)

    while True:
        handle_events()

        # simulation logic / Cell Movment

        screen.fill(BLACK)
        f.draw(screen)
        c.draw(screen)
        # draw cells and food
        # draw GUI
        pygame.display.flip()
