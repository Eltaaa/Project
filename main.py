import pygame
from pygame import mixer
import time

# ----------
# DISPLAY SETUP
# ----------


pygame.init()
width, height = 800, 600
window = pygame.display.set_mode((width, height))
icon = pygame.image.load('Asset\\Icon.jpg')
pygame.display.set_icon(icon)
pygame.display.set_caption('Word Game')
background = pygame.image.load('Asset\\Backgroundimg.png')

# ----------,
# CLOCK
# ----------
clock = pygame.time.Clock()

# ----------
# COLORS
# ----------
white = (255, 255, 255)
lightGray = (100, 100, 100)
black = (0, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)

# ----------
# FONTS
# ----------
# menu font use for PLAYS SETTING & QUIT buttons
mainmenufont = pygame.font.SysFont("Comic Sans MS", 25)

# ----------
# IMAGE LOAD
# ----------
gametitle = pygame.image.load('Asset\\title.png')

# ----------
# SOUND
# ----------
titleBGM = mixer.music.load('Asset\\backgroundsound.wav')
pygame.mixer.music.set_volume(0.01)
clicknoise = mixer.Sound('Asset\\Click.wav')
pygame.mixer.Sound.set_volume(clicknoise, 0.01)


# MAIN MENU


def startscreen():
    ''' start game main menu'''

    clock.tick(60)
    OnStartScreen = True

    mixer.music.play(-1)
    window.blit(background, (0, 0))
    pygame.display.update()
    clock.tick(60)

    window.blit(gametitle, [100, 100])
    pygame.display.update()
    clock.tick(60)

    while OnStartScreen:
        window.blit(background, (0, 0))
        window.blit(gametitle, [100, 100])

        pygame.event.get()                                               # will crash if not continuously call event, serve as place holder

        cursor = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()

        # DISPLAY BUTTON
        playButtonText = mainmenufont.render('PLAY', True, white)
        settingsButtonText = mainmenufont.render('SETTINGS', True, white)
        quitButtonText = mainmenufont.render('QUIT', True, white)

        window.blit(playButtonText, (350, 300))                         # display PLAY
        window.blit(settingsButtonText, (315, 400))                     # display SETTINGS
        window.blit(quitButtonText, (350, 500))                         # display QUIT
        pygame.display.update()

        # PLAY BUTTON
        if 300 <= cursor[1] <= 300+50 and 330 <= cursor[0] <= 430:      # Cursor on PLAY BUTTON level
            playOnHover = mainmenufont.render('PLAY', True, green)
            window.blit(playOnHover, (350, 300))
            pygame.display.update()
            clock.tick(60)

            if clicked[0] == 1:
                clicknoise.play()

        # SETTINGS
        elif 400 <= cursor[1] <= 400+50:                                # Cursor on SETTINGS BUTTON level
            settingsOnHover = mainmenufont.render('SETTINGS', True, green)

            window.blit(settingsOnHover, (315, 400))
            pygame.display.update()
            clock.tick(60)

            if clicked[0] == 1:
                clicknoise.play()

        # QUIT
        elif 400 <= cursor[1] <= 500+50:                                # Cursor on SETTINGS BUTTON level
            quitOnHover = mainmenufont.render('QUIT', True, green)

            window.blit(quitOnHover, (350, 500))
            pygame.display.update()
            clock.tick(60)

            if clicked[0] == 1:
                clicknoise.play()
                time.sleep(0.6)
                pygame.quit()
                quit()

# MAIN GAME


def main():
    ''' main function that run the game'''
    startscreen()                                                       # Game Start

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


if __name__ == '__main__':
    main()
