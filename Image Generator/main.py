import pygame
import math
from time import sleep
import os

# Init pygame
pygame.init()

# Create a clock
clock = pygame.time.Clock()

# Colors
colors = [
    (0, 0, 0),  # Black
    (255, 0, 0),  # Red
    (0, 0, 255),  # Blue
    (0, 255, 0),  # Green
    (255, 0, 255),  # Purple
]

shapeToggle = 0

# Set up window
wn_width = 500
wn_height = 386
wn = pygame.display.set_mode((wn_width, wn_height))
pygame.display.set_caption("Image Shape Drawer(Buckeye Vertical)")

max_type = 3

def mainLoop():
    state = True
    i = 0
    j = 0
    c = 48

    while state:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = False

        wn.fill((255,255,255))

        drawShape(i, colors[j])

        font = pygame.font.Font('freesansbold.ttf', 250)
        letterColor = colors[0]
        if j == 0 or j == 2:
            letterColor = (255,255,255)
        text = font.render(chr(c), True, letterColor)
        textRect = text.get_rect()
        if i == 2 :
            textRect.center = (wn_width // 2,  (3 * wn_height) // 4)
        else:
            textRect.center = (wn_width // 2, wn_height // 2)

        if(c == 90 and j == len(colors) - 1 and i == max_type):
            state = False

        wn.blit(text, textRect)

        fileLocation = "images/" + str(i) + str(j) + str(c) + ".png"
        pygame.image.save(wn, fileLocation)

        if(c == 90):
            c=48
            if(j == len(colors) - 1):
                i += 1
                j = 0
            else:
                j += 1
        elif(c==57):
            c = 65
        else:
            c+=1
        

        print("i: " + str(i))
        print("j: " + str(j))
        print("c: " + str(c))

        pygame.display.update()
        clock.tick(300)

    # End pygame
    pygame.quit()
    quit()

def drawShape(type, color):
    if type == 0:
        #Rectangle
        rect_width = 500
        rect_height = 300
        pygame.draw.rect(wn, color, (wn_width/2-rect_width/2, wn_height/2-rect_height/2, rect_width, rect_height))
    elif type == 1:
        #Circle
        pygame.draw.circle(wn, color, (wn_width/2, wn_height/2), wn_height/2)
    elif type == 2:
        # Triangle
        # Put 5 at the end if you want it to be an empty triangle as another parameter
        pygame.draw.polygon(wn, color, [[wn_width/2 - wn_height/math.tan(math.pi/3), wn_height], [wn_width/2,0], [wn_width/2 + wn_height/math.tan(math.pi/3), wn_height]])
    elif type == 3:
        #Square
        square_length = 500
        pygame.draw.rect(wn, color, (wn_width/2-square_length/2, wn_height/2-square_length/2, square_length, square_length))

    '''elif type == 2:
        #Semicircle
    elif type == 3:
        #Quarter circle'''

    '''elif type == 5:
        #Square
    elif type == 6:
        #Trapezoid'''

mainLoop()