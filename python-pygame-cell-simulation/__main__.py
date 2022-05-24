import random
import sys, pygame

from .Cell import Cell
from .Food import Food

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

def random_color():
    return [random.randint(0,255) for x in range(3)]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pygame.init()
    size = width, height = 600, 400
    boundary = (width * 0.02, height * 0.02, width * 0.98, height * 0.98,)

    screen = pygame.display.set_mode(size)
    # create Cells etc.

    cells.append(Cell((random.randrange(boundary[0], boundary[2]), random.randrange(boundary[1], boundary[3])),
                       (182, 255, 0), (38, 127, 0)))
    for x in range(50):
        cells.append(Cell((random.randrange(boundary[0], boundary[2]), random.randrange(boundary[1], boundary[3])),
                          random_color(), random_color()))

    for x in range(5):
        cells.append(Food((random.randrange(boundary[0], boundary[2]), random.randrange(boundary[1], boundary[3])),
                          (182, 255, 0), (38, 127, 0)))
        pass

    while True:
        handle_events()
        pygame.time.delay(10)
        # simulation logic / Cell Movment
        screen.fill(BLACK)
        for c in cells:
            c.update(screen, cells, height, width)

        # draw GUI
        pygame.display.flip()
