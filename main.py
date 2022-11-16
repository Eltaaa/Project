import pygame
# from category import *
# display setup
WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
ICON = pygame.image.load('Asset\Icon.png')
fps = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def draw_window():
    """ update game's look """
    WINDOW.fill(BLACK)
    pygame.display.set_icon(ICON)
    pygame.display.update()

# game loop


def main():
    ''' main function that run the game'''
    tickspeed = pygame.time.Clock()
    run = True
    while run:
        tickspeed.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.set_caption('Word Game')
        draw_window()

    pygame.quit()


if __name__ == '__main__':
    main()
