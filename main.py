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
wordwin = pygame.font.SysFont("Calibri", 75)
clicktocon = pygame.font.SysFont("Comic Sans MS", 25)
answerfont = pygame.font.SysFont("Juice ITC", 35)
# ----------
# IMAGE LOAD
# ----------
gametitle = pygame.image.load('title.png')
scorebutton = pygame.image.load("score.png")
wordframe = pygame.image.load("backframe.jpg")
inputtext = pygame.image.load("input.png")
heart = pygame.image.load("heart.jpg")
gameoverbg = pygame.image.load('gameoverbg.jpg')
wingamebg = pygame.image.load('wingamebg4.jpg')
# ----------
# SOUND
# ----------
clicknoise = mixer.Sound('Click.wav')

# Word list
lst1 = ["apple","banana","guava","watermelon","grape","mango","lichi","strawberry","pear","kiwi"]
lst2 = ["rose","jasmine","lavender","daisy","marigold","lily","sunflower","lotus"]
lst3 = ["buffalo","tiger","giraffe","elephant","kangaroo","koala","chimpanzee","squirrel"]
lst4 = ["eagle","nightingale","ostrich","sparrow","vulture","dove","peacock","pigeon","swan"]
lst5 = ["butterfly","centipede","grasshopper","honeybee","wasp","earthworm","termite","spider","leech","locust","mosquito"]
global alllist
alllist = lst1+lst2+lst3+lst4+lst5

# Choose word
def chooseword(randomwords):
    while True:
        word = random.choice(alllist)
        if word in lst1:
            hint = 'Fruit'
        elif word in lst2:
            hint = 'Flower'
        elif word in lst3:
            hint = 'Animal'
        elif word in lst4:
            hint = 'Bird'
        elif word in lst5:
            hint = 'Insect'
        
        
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

# Transition
def transition():
    pygame.mixer.music.set_volume(0.3) # Fade sound while using transition
    for i in range(0,610,10):
        pygame.draw.rect(window, black, [0,600-(i),800,50+(i)])
        pygame.display.update()
        clock.tick(50)

    start = wordguessfont.render("GAME START", True, white)             
    window.blit(start, [225,250])                                         
    pygame.display.update()
    time.sleep(1)
    pygame.mixer.music.set_volume(1) # Set volume to default after transition
    clock.tick(1)

def transitionend():
    pygame.mixer.music.set_volume(0.1) # Fade sound while using transition
    for i in range(0,610,10):
        pygame.draw.rect(window, black, [0,600-(i),800,50+(i)])
        pygame.display.update()
        clock.tick(50)

    end = wordguessfont.render("THIS IS THE END...", True, white)             
    window.blit(end, [170,250])                                         
    pygame.display.update()
    time.sleep(2)
    
    clock.tick(1)

def transitionwin():
    pygame.mixer.music.set_volume(0.1) # Fade sound while using transition
    for i in range(0,610,10):
        pygame.draw.rect(window, black, [0,600-(i),800,50+(i)])
        pygame.display.update()
        clock.tick(50)

    win = wordguessfont.render("YOU MADE IT", True, white)             
    window.blit(win, [225,250])                                         
    pygame.display.update()
    time.sleep(2)
    clock.tick(1)

# Display correct answer
def printanswer(word):
    msgAnswer = answerfont.render("The correct answer is: "+word[0], True, white)
    window.blit(msgAnswer, [220,0])
    pygame.display.update()
    time.sleep(2)

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

        pygame.event.get()                                              # will crash if not continuously call event, serve as place holder

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
                transition()
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
    letters = []      #Letters guessed by user
    chances = 5         #Chances per match
    score = 0           #Score

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
                    string = ""                     #Every time enter is pressed, string is reseted
                    chances -= 1   
                    if chances == 0:
                        transitionend()             # Use transition
                        time.sleep(1)
                        gameover(score, word)             # Call game over screen
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
            if len(randomwords) != len(alllist):
                word = chooseword(randomwords)
            elif len(randomwords) == len(alllist):
                transitionwin()
                time.sleep(1)
                gamewin(score)                         # Call win screen
            Total += 1
            string = ""
            letters = []
        


        window.fill(black)                     #Back color to background
        window.blit(scorebutton, [0,0])
        displayscore(score)                    #Display score
        window.blit(wordframe, [0,165])        #Display the background for the to be guessed word
        displayword(word[0],letters)           #DisplayC the to be guessed word
        displayhint(word[1])  
        window.blit(inputtext, [0,370])        #Displaying the input

        for i in range(chances):                    #Displaying the hearts
            window.blit(heart, [20+(i*50),500])

        typechar(string)   
        pygame.display.update()

# Game Over screen

def gameover(score, word):
    pygame.mixer.music.set_volume(1) # Set volume to default after transition
    gameoversound = mixer.music.load('GameOver.wav')
    mixer.music.play(-1)
    window.blit(gameoverbg, [0, 0])
    itover = wordover.render('GAME OVER', True, white)
    continu = clicktocon.render('Click anywhere to return to continue...', True, white)
    finalscore = hintfont.render('Your score : '+str(score), True, white )
    answer = hintfont.render('Answer is '+word[0], True, white)
    window.blit(answer, (48,85))
    window.blit(finalscore, (50, 35))
    window.blit(itover, (155, 200))
    window.blit(continu, (180, 500))
    pygame.display.update()
    while True:
        pygame.event.get()
        cursor = pygame.mouse.get_pos()                                              
        clicked = pygame.mouse.get_pressed()
        if (0 <= cursor[1] <= 600 and 0 <= cursor[0] <= 800) and not(300 <= cursor[1] <= 300+50 and 330 <= cursor[0] <= 430): # Return to main menu and prevent double click at play button
            if clicked[0] == 1:
                main()

# Game winning screen

def gamewin(score):
    pygame.mixer.music.set_volume(1) # Set volume to default after transition
    gamewinsound = mixer.music.load('winsong.wav')
    mixer.music.play(-1)
    window.blit(wingamebg, [0, 0])
    itover = wordwin.render('CONGRATULATION !!!', True, white)
    continu = clicktocon.render('Click anywhere to return to continue...', True, white)
    finalscore = hintfont.render('Your score : '+str(score), True, white )
    window.blit(finalscore, (50, 50))
    window.blit(itover, (85, 200))
    window.blit(continu, (180, 300))
    pygame.display.update()
    while True:
        pygame.event.get()
        cursor = pygame.mouse.get_pos()                                              
        clicked = pygame.mouse.get_pressed()
        if (0 <= cursor[1] <= 600 and 0 <= cursor[0] <= 800) and not(300 <= cursor[1] <= 300+50 and 330 <= cursor[0] <= 430): # Return to main menu and prevent double click at play button
            if clicked[0] == 1:
                main()

if __name__ == '__main__':
    main()

