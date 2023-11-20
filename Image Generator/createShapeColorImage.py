import pygame
import math
from math import sin,cos,radians
from time import sleep
import os
from PIL import Image

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
    #(255, 0, 255),  # Pink
    (254,254,254), # White
    (128,0,128), # Purple
    (150,75,0), # Brown
    (255,165,0), # Orange
]

shapeToggle = 0

# Set up window
wn_width = 500
wn_height = 386
wn = pygame.display.set_mode((wn_width, wn_height))

pygame.display.set_caption("Image Shape Drawer(Buckeye Vertical)")

max_type = 7

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
        # Makes text white (254,254,254) sometimes, differentiated from the (255,255,255) background
        if j == 0 or j == 2:
            letterColor = (254,254,254)
        text = font.render(chr(c), True, letterColor)
        textRect = text.get_rect()
        if i == 2 :
            textRect.center = (wn_width // 2,  (3 * wn_height) // 4)
        else:
            textRect.center = (wn_width // 2, wn_height // 2)

        if(c == 90 and j == len(colors) - 1 and i == max_type):
            state = False

        wn.blit(text, textRect)

        fileLocation = "BuckeyeVerticalObjectDetection\BuckeyeVerticalObjectDetection\Image Generator\images" + str(i) + str(j) + str(c) + ".png"
        pygame.image.save(wn, fileLocation)
        # Converts white pixels to transparent
        convertImage(fileLocation)


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

        pygame.display.update()
        clock.tick(300)

    # End pygame
    pygame.quit()
    quit()
# Converts White Pixels (255,255,255) to Transparent
def convertImage(path):
    img = Image.open(path)
    img = img.convert("RGBA")
 
    datas = img.getdata()
 
    newData = []
 
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
 
    img.putdata(newData)
    img.save(path, "PNG")
    print("Successful")

def drawShape(type, color):
    radius = wn_width/2
    center = [wn_width/2, wn_height/2]
    if type == 6:
        #Rectangle
        rect_width = 500
        rect_height = 300
        pygame.draw.rect(wn, color, (wn_width/2-rect_width/2, wn_height/2-rect_height/2, rect_width, rect_height))
    elif type == 5:
        #Circle
        pygame.draw.circle(wn, color, (wn_width/2, wn_height/2), wn_height/2)
    elif type == 4:
        # Triangle
        # Put 5 at the end if you want it to be an empty triangle as another parameter
        pygame.draw.polygon(wn, color, [[wn_width/2 - wn_height/math.tan(math.pi/3), wn_height], [wn_width/2,0], [wn_width/2 + wn_height/math.tan(math.pi/3), wn_height]])
    
    elif type == 1:
        #Semicircle
        pie(wn,color,[center[0],center[1]-150],radius,0,180)
        
    elif type == 0:
        #Quarter circle
        pie(wn,color,[70,0],wn_height,0,90)
    elif type == 2:
        #Pentagon
        sides = 5
        fit_radius = radius / (1.283)
        pentagon_points = generate_ngon_points(sides,fit_radius,[center[0],center[1]+10])
        pygame.draw.polygon(wn,color,pentagon_points)
    elif type == 3:
        #Star
        star_points = generate_star_points(radius, center)
        pygame.draw.polygon(wn,color,star_points)
    '''elif type == 8:
        #Cross
        '''

def generate_star_points(outer_radius, center):
    # Golden ratio
    phi = (1 + math.sqrt(5)) / 2
    
    # Calculate the inner radius
    inner_radius = outer_radius / phi

    # The points of the star
    points = []

    # The angle between the star's points
    angle_between_points = math.pi / 5

    # Generate the points for the star
    for i in range(5):
        # Outer point (tip of the star)
        outer_angle = 2 * math.pi * i / 5 - math.pi / 2
        outer_x = center[0] + outer_radius * math.cos(outer_angle)
        outer_y = center[1] + outer_radius * math.sin(outer_angle)
        points.append((outer_x, outer_y))
        
        # Inner point (inner corner of the star)
        inner_angle = outer_angle + angle_between_points
        inner_x = center[0] + inner_radius * math.cos(inner_angle)
        inner_y = center[1] + inner_radius * math.sin(inner_angle)
        points.append((inner_x, inner_y))

    return points

def generate_ngon_points(sides, radius, center):
    points = []
    offset_angle = (3 * math.pi / 2) + (math.pi / sides)  # Start at the top of the screen
    
    for k in range(sides):
        # Calculate each point of the n-gon starting from the top
        angle = 2 * math.pi * k / sides - offset_angle
        x = center[0] + radius * math.cos(angle)
        y = center[1] + radius * math.sin(angle)  # Pygame's y-axis increases downwards
        points.append((x, y))

    return points
    
def pie(scr,color,center,radius,start_angle,stop_angle):
    theta=start_angle
    while theta <= stop_angle:
        pygame.draw.line(scr,color,center, 
        (center[0]+radius*cos(radians(theta)),center[1]+radius*sin(radians(theta))),2)
        theta+=0.01

mainLoop()