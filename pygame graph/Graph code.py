import pygame
from sys import exit

width = 900
height = 675
origin_width = 50
origin_height = 637.5
pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Robot Graph')
clock = pygame.time.Clock()
ground_surface = pygame.image.load('background.jpg').convert()
robot = pygame.image.load('car.jpg').convert_alpha()
robot_rect = robot.get_rect(center = (origin_width,origin_height))
test_font = pygame.font.Font(None,40)
robot_direction = 90


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    


    X = 0
    Y = 0
    x_coordinate = -X+50
    y_coordinate = -Y+637.5
    screen.blit(ground_surface,(0,0))
    screen.blit(robot,robot_rect)

    robot_rect.center


    ver_bars_width = 1
    ver_bars_height = 600
    hor_bars_width = 800
    hor_bars_height = 1
    start_x = 50
    start_y = 36
    
    for i  in range(17):
        #0
        l = 640
        #1
        test_surface = test_font.render('1', False, 'Black')
        screen.blit(test_surface,(45 + 50 ,l))
        #2
        test_surface = test_font.render('2', False, 'Black')
        screen.blit(test_surface,(45 + 2*50,l))
        #3
        test_surface = test_font.render('3', False, 'Black')
        screen.blit(test_surface,(45 + 3*50,l))
        #4
        test_surface = test_font.render('4', False, 'Black')
        screen.blit(test_surface,(45 + 4*50,l))
        #5
        test_surface = test_font.render('5', False, 'Black')
        screen.blit(test_surface,(45 + 5*50,l))
        #6
        test_surface = test_font.render('6', False, 'Black')
        screen.blit(test_surface,(45 + 6*50,l))
        #7
        test_surface = test_font.render('7', False, 'Black')
        screen.blit(test_surface,(45 + 7*50,l))
        #8
        test_surface = test_font.render('8', False, 'Black')
        screen.blit(test_surface,(45 + 8*50,l))
        #9
        test_surface = test_font.render('9', False, 'Black')
        screen.blit(test_surface,(45 + 9*50,l))
        #10
        test_surface = test_font.render('10', False, 'Black')
        screen.blit(test_surface,(40 + 10*50,l))
        #11
        test_surface1= test_font.render('11', False, 'Black')
        screen.blit(test_surface,(40 + 11*50,l))
        #12
        test_surface = test_font.render('12', False, 'Black')
        screen.blit(test_surface,(40 + 12*50,l))
        #13
        test_surface = test_font.render('13', False, 'Black')
        screen.blit(test_surface,(40 + 13*50,l))
        #14
        test_surface = test_font.render('14', False, 'Black')
        screen.blit(test_surface,(40 + 14*50,l))
        #15
        test_surface = test_font.render('15', False, 'Black')
        screen.blit(test_surface,(40 + 15*50,l))
       


        ver_bar = pygame.Rect(start_x,start_y,ver_bars_width,ver_bars_height)
        pygame.draw.rect(screen,'Black',ver_bar)
        start_x = start_x + 50

    start_x = 50
    start_y = 36


    for x in range(17):
        #0
        test_surface = test_font.render('0', False, 'Black')
        screen.blit(test_surface,(35,640))
        #1
        test_surface = test_font.render('1', False, 'Black')
        screen.blit(test_surface,(35 ,627.5 - 1*37.5))
        #2
        test_surface = test_font.render('2', False, 'Black')
        screen.blit(test_surface,(35,627.5 - 2*37.5))
        #3
        test_surface = test_font.render('3', False, 'Black')
        screen.blit(test_surface,(35,627.5 - 3*37.5))
        #4
        test_surface = test_font.render('4', False, 'Black')
        screen.blit(test_surface,(35,627.5 - 4*37.5))
        #5
        test_surface = test_font.render('5', False, 'Black')
        screen.blit(test_surface,(35,627.5 - 5*37.5))
        #6
        test_surface = test_font.render('6', False, 'Black')
        screen.blit(test_surface,(35,627.5 - 6*37.5))
        #7
        test_surface = test_font.render('7', False, 'Black')
        screen.blit(test_surface,(35,627.5 - 7*37.5))
        #8
        test_surface = test_font.render('8', False, 'Black')
        screen.blit(test_surface,(35,627.5 - 8*37.5))
        #9
        test_surface = test_font.render('9', False, 'Black')
        screen.blit(test_surface,(35,627.5 - 9*37.5))
        #10
        test_surface = test_font.render('10', False, 'Black')
        screen.blit(test_surface,(20,627.5 - 10*37.5))
        #11
        test_surface = test_font.render('11', False, 'Black')
        screen.blit(test_surface,(20,627.5 - 11*37.5))
        #12
        test_surface = test_font.render('12', False, 'Black')
        screen.blit(test_surface,(20,627.5 - 12*37.5))
        #13
        test_surface = test_font.render('13', False, 'Black')
        screen.blit(test_surface,(20,627.5 - 13*37.5))
        #14
        test_surface = test_font.render('14', False, 'Black')
        screen.blit(test_surface,(20,627.5 - 14*37.5))
        #15
        test_surface = test_font.render('15', False, 'Black')
        screen.blit(test_surface,(20,627.5 - 15*37.5))


        hor_bar=pygame.Rect(start_x,start_y,hor_bars_width,hor_bars_height)
        pygame.draw.rect(screen,'Black',hor_bar)
        start_y = start_y + 37.5

    
    pygame.display.update()
    clock.tick(30)

