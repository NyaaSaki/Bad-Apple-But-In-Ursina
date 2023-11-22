print("hi")
import pygame

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

road = pygame.Rect((0,330,1000,40))
clock = pygame.time.Clock()

pygame.display.set_caption("aHAHAHAH")
truck = pygame.transform.scale2x(pygame.image.load("FoodTruck.png"))
#_____________________ Game Loop _________________________________
position = [300,300]
run = True
v=0
poly = [
        (340,100),
        (250,200),
        (200,350),
        (500,350)
    ]
inpoly = [
        (430,300),
        (400,260),
        (370,350),
        (450,350),
    ]

lightpoly = [
        (340,100),
        (250,200),
        (180,350),
        (250,350),
        (280,200)
    ]
while run:
    screen.fill((30,50,30))
    
    
    key = pygame.key.get_pressed()
    
    if key[pygame.K_d] == True:
        v = 2
    elif key[pygame.K_a] ==True :
        v = -5
    else:
        v = v - (0.1*v)
    position[0] = position[0] + v
    
    pygame.draw.polygon(screen,(30,20,30),poly)
    pygame.draw.polygon(screen,(20,10,20),inpoly)
    pygame.draw.polygon(screen,(130,100,130),lightpoly)
    pygame.draw.rect(screen,(10,10,20),road)
    screen.blit(truck,tuple(position))
    

    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    clock.tick(60)

pygame.quit()
    