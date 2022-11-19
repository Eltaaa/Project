import pygame

# ----------
# DISPLAY SETUP
# ----------
pygame.init()
width, height = 800, 600
window = pygame.display.set_mode((width, height))
icon = pygame.image.load('Asset\\Icon.jpg')
pygame.display.set_icon(icon)
pygame.display.set_caption('Word Game')

# ----------,
# CLOCK
# ----------
clock = pygame.time.Clock()
fps = 60

# ----------
# COLORS
# ----------
white = (255, 255, 255)
lightGray = (100, 100, 100)
black = (0, 0, 0)
yellow = (255, 255, 0)

# ----------
# FONTS
# ----------
# menu font use for PLAYS SETTING & QUIT buttons
mainmenufont = pygame.font.SysFont("Comic Sans MS", 25)

# ----------
# IMAGE LOAD
# ----------
gametitle = pygame.image.load(
    'Asset\\title.png')


# MAIN MENU


def startscreen():
    ''' start game main menu'''

    clock.tick(60)
    OnStartScreen = True

    window.fill(black)
    pygame.display.update()
    clock.tick(60)

    window.blit(gametitle, [100, 100])
    pygame.display.update()
    clock.tick(60)

    while OnStartScreen:
        window.fill(black)
        window.blit(gametitle, [100, 100])

        # will crash if not continuously call event, serve as place holder
        pygame.event.get()

        cursor = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()

        # DISPLAY BUTTON
        playButtonText = mainmenufont.render('PLAY', True, white)
        settingsButtonText = mainmenufont.render('SETTINGS', True, white)
        quitButtonText = mainmenufont.render('QUIT', True, white)

        window.blit(playButtonText, (350, 300))
        window.blit(settingsButtonText, (315, 400))
        window.blit(quitButtonText, (350, 500))
        pygame.display.update()

        if cursor[0] >= 750 and cursor[1] <= 50 and clicked[0]:                 # Click top right to close (temporaly)
            pygame.quit()

        # PLAY BUTTON
        if 300 <= cursor[1] <= 300+50:                                          # Cursor on PLAY BUTTON level
            pygame.draw.rect(window, lightGray, [0, 300, 800, 40])
            window.blit(playButtonText, (350, 300))
            pygame.display.update()
            clock.tick(60)

        # SETTINGS
        elif 400 <= cursor[1] <= 400+50:                                          # Cursor on SETTINGS BUTTON level
            pygame.draw.rect(window, lightGray, [0, 400, 800, 40])
            window.blit(settingsButtonText, (315, 400))
            pygame.display.update()
            clock.tick(60)

        # QUIT
        elif 400 <= cursor[1] <= 500+50:                                          # Cursor on SETTINGS BUTTON level
            pygame.draw.rect(window, lightGray, [0, 500, 800, 40])
            window.blit(quitButtonText, (350, 500))
            pygame.display.update()
            clock.tick(60)
            if clicked[0] == 1:
                pygame.quit()

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
