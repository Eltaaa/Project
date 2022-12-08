import pygame
from pygame import mixer
import time
import random

# ----------
# DISPLAY SETUP
# ----------


pygame.init()
width, height = 800, 600
window = pygame.display.set_mode((width, height))
icon = pygame.image.load('Icon.jpg')
pygame.display.set_icon(icon)
pygame.display.set_caption('Word Game')
background = pygame.image.load('Backgroundimg.png')

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
blue = (40, 53, 88)
# ----------
# FONTS
# ----------
# menu font use for PLAYS SETTING & QUIT buttons
mainmenufont = pygame.font.SysFont("Comic Sans MS", 25)
wordguessfont = pygame.font.SysFont("CopperPlate Gothic", 50)
hintfont = pygame.font.SysFont("Comic Sans MS", 25)
scorefont = pygame.font.SysFont("Comic Sans MS", 25)
wordtype = pygame.font.SysFont("Calibri", 50)
wordover = pygame.font.SysFont("Calibri", 100)
clicktocon = pygame.font.SysFont("Comic Sans MS", 25)
# ----------
# IMAGE LOAD
# ----------
gametitle = pygame.image.load('title.png')
scorebutton = pygame.image.load("score.png")
wordframe = pygame.image.load("backframe.jpg")
inputtext = pygame.image.load("input.png")
heart = pygame.image.load("heart.jpg")
# ----------
# SOUND
# ----------
#pygame.mixer.music.set_volume(0.01)
clicknoise = mixer.Sound('Click.wav')

# Word list
lst1 = ["apple","banana","guava","watermelon","grape","mango","lichi","strawberry","pear","kiwi"]
lst2 = ["rose","jasmine","lavender","daisy","marigold","lily","sunflower","lotus"]
lst3 = ["buffalo","tiger","giraffe","elephant","kangaroo","koala","chimpanzee","squirrel"]
global alllist
alllist = lst1+lst2+lst3

# Choose word
def chooseword(randomwords):
    while True:
        word = random.choice(alllist)
        if word in lst1:
            hint = 'Fruit'
        elif word in lst2:
            hint = 'Flower'
        elif word in lst3:
            hint = 'Animals'
        
        if word in randomwords:
            continue
        else:
            break
    randomwords.append(word)
    return [word, hint]

# Display guessword on screen
def displayword(word, letters): 
    hiddenword = ""
    for i in range(len(word)):
        if (i == 0) or (i == len(word)-1):
            hiddenword += " "+word[i]+" "
        elif word[i] in letters:
            hiddenword += " "+word[i]+" "
        else:
            hiddenword += " ? "

    wordText = wordguessfont.render(hiddenword, True, yellow)
    window.blit(wordText, [20,200])

# Display hint
def displayhint(hint):
    hintText = hintfont.render("Hint: "+hint, True, blue)
    window.blit(hintText, [50,300])

# Display score
def displayscore(score):
    scoreText = scorefont.render("Score: "+str(score), True, black)
    window.blit(scoreText, [25,20])

# Display user entered letters
def typechar(char):
    typechar = wordtype.render(char, True, green)
    window.blit(typechar, [50,395])
    pygame.display.update()

# MAIN MENU
def startscreen():
    ''' start game main menu'''

    clock.tick(60)
    OnStartScreen = True
    titleBGM = mixer.music.load('backgroundsound.wav')
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
                window.fill(black)
                pygame.display.update()
                break

        # SETTINGS
        elif 400 <= cursor[1] <= 400+50 and 310 <= cursor[0] <= 450:                                # Cursor on SETTINGS BUTTON level
            settingsOnHover = mainmenufont.render('SETTINGS', True, green)

            window.blit(settingsOnHover, (315, 400))
            pygame.display.update()
            clock.tick(60)

            if clicked[0] == 1:
                clicknoise.play()

        # QUIT
        elif 400 <= cursor[1] <= 500+50 and 345 <= cursor[0] <= 420:                                # Cursor on SETTINGS BUTTON level
            quitOnHover = mainmenufont.render('QUIT', True, green)

            window.blit(quitOnHover, (350, 500))
            pygame.display.update()
            clock.tick(60)

            if clicked[0] == 1:
                clicknoise.play()
                time.sleep(0.55)
                pygame.quit()
                quit()

# MAIN GAME


def main():
    ''' main function that run the game'''
    startscreen()  
    BGMwhenplay = mixer.music.load('PlayBGM.wav')
    mixer.music.play(-1) 
    string = ""         #The answer of user is stored in "string"
    letters = []        #Letters guessed by user
    chances = 5         #Chances per word
    score = 0           #Score

    correctanswers = 0.0    #Correct Answers
    Total = 0.0             #Total words

    randomwords = []        #Words already displayed

    firstWord = True        # Game Start
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if len(string) < 16:
                    char = (chr(event.key))
                    string += char
                
                if event.key == pygame.K_RETURN:
                    if len(string) == 2:                #If there is only one letter, it is added into letters (\n is also counted)
                        letters.extend(string[0])
                    string = ""
                    chances -= 1                    #Every time enter is pressed, string is reseted
                    if chances == 0:
                        gameover()
                        break                                            
    

                if event.key == pygame.K_BACKSPACE:
                    if string[-1] != chr(8):            #When Backspace is pressed
                        string = string[:-1]            #If string's length is equal to the limit, one character from end is deleted
                    else:                               #else two are deleted as when the string is less than the limit, backspace
                        string = string[:-2]            #char is also added in the end

        if firstWord == True:                           #print word
            word = chooseword(randomwords)
            displayword(word[0],letters)
            displayhint(word[1])
            firstWord = False

        if word[0] == string:                           #If the answer is correct
            typechar(string)
            pygame.display.update()
            score += 100
            word = chooseword(randomwords)
            Total += 1
            string = ""
            letters = []


        window.fill(black)                     #Back color to background
        window.blit(scorebutton, [0,0])
        window.blit(wordframe, [0,165])        #Displaying the background for the to be guessed word
        displayword(word[0],letters)           #Displaying the to be guessed word
        displayhint(word[1])  
        window.blit(inputtext, [0,370])        #Displaying the input

        for i in range(chances):                    #Displaying the hearts
            window.blit(heart, [20+(i*50),500])

        typechar(string)   
        pygame.display.update()

# Display GameOver screen
def gameover():
    gameoversound = mixer.music.load('GameOver.wav')
    mixer.music.play(-1)
    window.fill(black)
    itover = wordover.render('GAME OVER', True, white)
    continu = clicktocon.render('Click anywhere to return to continue...', True, white)
    window.blit(itover, (150, 175))
    window.blit(continu, (180, 500))
    pygame.display.update()
    while True:
        pygame.event.get()
        cursor = pygame.mouse.get_pos()                                              
        clicked = pygame.mouse.get_pressed()
        if (0 <= cursor[1] <= 600 and 0 <= cursor[0] <= 800) and not(300 <= cursor[1] <= 300+50 and 330 <= cursor[0] <= 430)\
            and not(400 <= cursor[1] <= 500+50 and 345 <= cursor[0] <= 420)\
            and not(400 <= cursor[1] <= 400+50 and 310 <= cursor[0] <= 450): # Return to main menu and prevent double click at play setting and quit button
            if clicked[0] == 1:
                main()
if __name__ == '__main__':
    main()
