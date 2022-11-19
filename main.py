import pygame

# ----------
# DISPLAY SETUP
# ----------
pygame.init()
WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
ICON = pygame.image.load('Asset\\Icon.jpg')
pygame.display.set_icon(ICON)
pygame.display.set_caption('Word Game')

# ----------,
# CLOCK
# ----------
clock = pygame.time.Clock()
fps = 15

# ----------
# COLORS
# ----------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# ----------
# FONTS
# ----------
titlefont = pygame.font.SysFont("CopperPlate Gothic", 25)

# ----------
# IMAGE LOAD
# ----------
gametitle = pygame.image.load(
    'Asset\\title.png')


def draw_window():
    """ update game's look """
    WINDOW.fill(BLACK)
    pygame.display.update()

# MAIN MENU


def startscreen():
    ''' start game main menu'''

    clock.tick(1)
    OnStartScreen = True

    WINDOW.fill(BLACK)
    pygame.display.update()
    clock.tick(1)

    WINDOW.blit(gametitle, [100, 100])
    pygame.display.update()
    clock.tick(1)

    while OnStartScreen:
        WINDOW.fill(BLACK)
        WINDOW.blit(gametitle, [100, 100])

        
        pygame.event.get()                      # will crash if not continuously call event, serve as place holder

        cursor = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()


# MAIN GAME
def main():
    ''' main function that run the game'''
    startscreen()                               # Game Start

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


if __name__ == '__main__':
    main()
