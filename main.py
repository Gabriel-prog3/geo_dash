import pygame
pygame.font.init()
FPS=60
speed_x=-6
speed_y=0
GRAVITY=0.6
WIDTH, HEIGHT = 700, 584
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

FLOOR_COLOR = (255, 200, 222)
BLACK = (0, 0, 0)
PLAYER_COLOR = (155, 255, 200)
IMPELLER_COLOR=(200,255,200)
OBSTACLES_COLOR=(46,132,255)


clock = pygame.time.Clock()
player=pygame.Rect(2,HEIGHT-16,8,8) 

floors=[pygame.Rect(0,HEIGHT,WIDTH,1)] 
impellers=[pygame.Rect(0,HEIGHT-50,3,8)]
obstacles=[]

for i in range(8):
    if i%2==0:
        obstacles.append(pygame.Rect(WIDTH- 64*(i+1),-72*i+HEIGHT-8,8,8))
        obstacles.append(pygame.Rect(256 +16*i,-72*i+HEIGHT-8,8,8))
        floors.append(pygame.Rect(64,HEIGHT-(i+1)*72,WIDTH-64,1))
        impellers.append(pygame.Rect(WIDTH-3,HEIGHT-40-(i+1)*72,3,8))
    else:
        obstacles.append(pygame.Rect(WIDTH- 64*(i+1),-72*i+HEIGHT-8,8,8))
        obstacles.append(pygame.Rect(256 +16*i,-72*i+HEIGHT-8,8,8))
        floors.append(pygame.Rect(0,HEIGHT-(i+1)*72,WIDTH-64,1))
        impellers.append(pygame.Rect(0,HEIGHT-30-(i+1)*72,3,8))



def draw_update():
    clock.tick(FPS)
    
    pygame.display.flip()
    WIN.fill(BLACK)




while 1:
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break


    player.x+=speed_x
    player.y+=speed_y
    speed_y+=GRAVITY


    for i in floors:
        pygame.draw.rect(WIN,FLOOR_COLOR,i)
        if player.colliderect(i):
            speed_y=0
            player.y-=1
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                speed_y=-7

    for i in obstacles:
        pygame.draw.rect(WIN,OBSTACLES_COLOR,i)
        if player.colliderect(i):
            player.x=2
            player.y=HEIGHT-16

    
    for i in impellers:
        pygame.draw.rect(WIN,IMPELLER_COLOR,i)
        if player.colliderect(i):
            speed_y=-8


    pygame.draw.rect(WIN,PLAYER_COLOR,player)



    

    if player.x>=WIDTH-7 or player.x<=0:
        speed_x=-speed_x
    
    if player.y<8:
        font = pygame.font.SysFont(None, 44)
        img = font.render('game over', True, OBSTACLES_COLOR)
        WIN.blit(img, (20, 20))
    
    draw_update()

    




