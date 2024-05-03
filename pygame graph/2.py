import pygame
from sys import exit 
width = 1080
height = 800
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Robot Graph')
clock = pygame.time.Clock()


# main graph inputs for calculating grids num and Area
Grids_Number = 15
X_Area = 750
Y_Area = 750

#calculating origin point
originX = (width - X_Area) / 2
originY = ((height - Y_Area) / 2) + Y_Area

robot = pygame.image.load('car.jpg').convert_alpha()
robot_rect = robot.get_rect(center = (originX,originY))

#Main positive area
X_Area = 1080 - (originX * 2)
Y_Area = -(720 - (2 * originY))
Grid_Area = X_Area / Grids_Number


# calculating the area not in the maon area
X_Remain = width % Grid_Area
X_Grid_Seq = width - X_Remain
X_Numb = X_Grid_Seq / Grid_Area
X_num = int(X_Numb)

Y_Remain = height % Grid_Area
Y_Grid_Seq = height - Y_Remain
Y_Numb = Y_Grid_Seq / Grid_Area
Y_num = int(Y_Numb)


#recieved from serial
Direction = 90
X_Coordinate = 0
Y_Coordinate = 0

#preparing  x & y in graph
X_graph = (0.5 * X_Coordinate) + 165
Y_graph = (-0.5 * Y_Coordinate) +725




def Main_Grids():
    #Main grid properties
    Main_Vert_Bar_W = 3
    Main_Vert_Bar_H = height
    Main_Horiz_Bar_W = width
    Main_Horiz_Bar_H = 3
    #Main vertical grid
    Main_ver_bar = pygame.Rect(originX,0,Main_Vert_Bar_W,Main_Vert_Bar_H)
    pygame.draw.rect(screen,'Black',Main_ver_bar)
    #Main horizontal Grid
    Main_ver_bar = pygame.Rect(0,originY,Main_Horiz_Bar_W,Main_Horiz_Bar_H)
    pygame.draw.rect(screen,'Black',Main_ver_bar)

def Sub_Grids():
    #sub grid properties
    Sub_Vert_Bar_W = 1
    Sub_Vert_Bar_H = height
    Sub_Horiz_Bar_W = width
    Sub_Horiz_Bar_H = 1
    #vertical sub-grids
    ver_grid = X_Remain / 2
    for i in range(X_num+1):
        
        Sub_ver_bar = pygame.Rect(ver_grid,0,Sub_Vert_Bar_W,Sub_Vert_Bar_H)
        pygame.draw.rect(screen,'Black',Sub_ver_bar)
        ver_grid= ver_grid + Grid_Area
        
    #Horizontal sub-grids
    Hor_grid = height - (Y_Remain/2) -25
    for i in range(int(Y_num)):
        ver_bar = pygame.Rect(0,Hor_grid,Sub_Horiz_Bar_W,Sub_Horiz_Bar_H)
        pygame.draw.rect(screen,'Black',ver_bar)
        Hor_grid = Hor_grid - Grid_Area



def Robot_View():
    screen.blit(robot,robot_rect)



while True:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    
    Robot_View()
    Main_Grids()
    Sub_Grids()

    pygame.display.update()
    clock.tick(30)
    
