import pygame
pygame.init()
monitor=pygame.display.set_mode((612,382))
pygame.display.set_caption("Game")
pygame.display.set_icon(pygame.image.load("data_for_TSIS7/icon_for_game.png"))

rectangle = pygame.Surface((200,100))
background = pygame.image.load("data_for_TSIS7/background.png")
sound = pygame.mixer.Sound("data_for_TSIS7")
sound.play()
clock = pygame.time.Clock()
check=True
while check:
    # monitor.fill((25,125,225))
    # monitor.blit(rectangle,(40,40))
    monitor.blit(background,(0,0))
    pygame.display.update()
    
    for action in pygame.event.get():
        if action.type==pygame.QUIT:
            check=False
            pygame.quit()
    clock.tick(60)

