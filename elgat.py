import pygame, sys
import time
import random
from pygame.locals import*
from pygame import mixer


#Set up pygame.
pygame.init()


#Setup Audio
music = mixer.music.load("res/petit.wav")
crash = mixer.Sound("res/lose.wav")
pt = mixer.Sound("res/point.wav")
mixer.music.set_volume(0.5)
def audio_track():
    mixer.music.play(-1)
def lose():
    mixer.Sound.play(crash)
    time.sleep(0.5)
def point():
    mixer.Sound.play(pt)


#Set up the window.
winSurf = pygame.display.set_mode((400,400), 0, 0)
pygame.display.set_caption("elgato game")


#Set up the colors. 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)


#Set up the fonts. 
basicFont = pygame.font.SysFont("Comic Sans MS", 26)


#Setup text for game counter
text = basicFont.render("Score: 0", True, BLACK)
textRect = text.get_rect()
textRect.centerx = winSurf.get_rect().centerx - 135
textRect.centery = winSurf.get_rect().centery - 175


#Draw the white background onto the surface.
winSurf.fill(WHITE)


#Setup Image and Icon
img = pygame.image.load("res/el.png").convert_alpha()
img2 = pygame.transform.scale(img, (64,64))
appl = pygame.image.load("res/appl.png").convert_alpha()
pygame.display.set_icon(img)


#Get a pixel array of the surface. 
pixArray = pygame.PixelArray(winSurf)
pixArray[399][399] = BLACK
del pixArray


#Setup game variables, functions, and audio.
x=168
xdrift=0
y=336
audio_track()
pts = 0
xs1 = random.randint(0, 400)
ys1 = 0
xs2 = random.randint(0, 400)
ys2 = -200

#Draw the window onto the screen.
pygame.display.update()


#Run the game loop.
while True:
    
    #Handle window close.
    for event in pygame.event.get():       
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    #Key events.
    key=pygame.key.get_pressed()
    if key[K_LEFT]:
        x=x-1
    elif key [K_RIGHT]:
        x=x+1
    if x == 336:
        x=x-1
    elif x == 0:
        x=x+1
    #Refresh
    pygame.display.update()
    time.sleep(0.001)

    #Draw Image
    winSurf.fill(WHITE)
    imgbox = pygame.draw.rect(winSurf, WHITE , (x,y,64,64))
    loserect = pygame.draw.rect(winSurf, WHITE , (0,396,400,4))
    scman = "Score: " + str(pts)
    text = basicFont.render((scman), True, BLACK)
    winSurf.blit(img2,(x,y))
    winSurf.blit(text,textRect)

    #Squares
    ys1=ys1+0.5
    ys2=ys2+0.5
    if ys1 == 0:
        xs1 = random.randint(0, 400)
    elif ys1 == 400:
        ys1 = -1
    if ys2 == 0:
        xs2 = random.randint(0, 400)
    elif ys2 == 400:
        ys2 = -1
    s1 = pygame.draw.rect(winSurf, WHITE , (xs1,ys1,16,16))
    s2 = pygame.draw.rect(winSurf, WHITE , (xs2,ys2,16,16))
    winSurf.blit(appl, (xs1,ys1))
    winSurf.blit(appl, (xs2,ys2))

    if imgbox.colliderect(s1):
        ys1 = -1
        pts+=1
        point()
    if imgbox.colliderect(s2):
        ys2 = -1 
        pts+=1
        point()
    if s1.colliderect(loserect) or s2.colliderect(loserect):
        lose()
        pygame.quit()
        sys.exit()
    pygame.display.update()
    