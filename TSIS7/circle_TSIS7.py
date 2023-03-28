import pygame
pygame.init()
W = 800
H = 600
sc = pygame.display.set_mode((W,H))
pygame.display.set_caption("Game")
pygame.display.set_icon(pygame.image.load("data_for_TSIS7/icon_for_game.png"))

white = (255,255,255)
fps = 60
clock = pygame.time.Clock()

x = W // 2
y = H // 2

speed = 5

bool = True
while bool:
   
    for action in pygame.event.get(): 
        
        if action.type == pygame.QUIT:
            bool = False
            pygame.quit()
        
    keys = pygame.key.get_pressed()  
    
       
          
          
    if keys[pygame.K_LEFT]:
        if x >= 25:
            x -= speed
            
    elif keys[pygame.K_RIGHT]:
        if x <= 775:
            x += speed
    elif keys[pygame.K_UP]:
        if y >= 25:
            y -= speed
    elif keys[pygame.K_DOWN]:
        if y <= 575:
            y += speed
            
    sc.fill((0,0,0))
    pygame.draw.circle(sc,white,(x,y),20)
    pygame.display.update()   
         
    clock.tick(fps)