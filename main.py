import random
import sys, pygame

from Cell import Cell
from Food import Food

BLACK = (0, 0, 0)
cells = list()
food = list()


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
    boundary = (width * 0.02, height * 0.02, width * 0.98, height * 0.98,)

    screen = pygame.display.set_mode(size)
    # create Cells etc.
    for x in range(50):
        cells.append(Cell((random.randrange(boundary[0], boundary[2]), random.randrange(boundary[1], boundary[3])),
                          200.0, 10.0, 500, 1, (182, 255, 0), (38, 127, 0), 0, 0.20, (0, 0), 2, 2))

    for x in range(5):
        f = Food((random.randrange(boundary[0], boundary[2]), random.randrange(boundary[1], boundary[3])),
                  200.0, 5.0, 500, 1, (0, 148, 255), (0, 74, 127))

    while True:
        handle_events()
        pygame.time.delay(10)
        # simulation logic / Cell Movment
        screen.fill(BLACK)
        for c in cells:
            c.move(cells, height, width)
            c.draw(screen)

        for f in food:
            f.draw(screen)
        # draw GUI
        pygame.display.flip()
