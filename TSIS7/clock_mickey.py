import pygame
from datetime import datetime
import math


pygame.init()

monitor = pygame.display.set_mode((800,600))
pygame.display.set_caption("Clock")
pygame.display.set_icon(pygame.image.load("/Users/kassi/TSIS7/data_for_clock/clock_icon.webp"))
clock = pygame.time.Clock()

#Time
time = datetime.now()
time_sec = time.second
time_min = time.minute

background = pygame.image.load("/Users/kassi/TSIS7/data_for_clock/mickey.jpeg")
background = pygame.transform.scale(background,(800,600))

second = pygame.image.load("/Users/kassi/TSIS7/data_for_clock/hand.png")
second = pygame.transform.scale(second, (300, 75))
sec_rect = second.get_rect()
sec_rect.center = (400,300)

minut = pygame.image.load("/Users/kassi/TSIS7/data_for_clock/hand.png")
minut = pygame.transform.scale(minut,(250,50))
min_rect = minut.get_rect()
min_rect.center = (400,300)


check = True
while check:
    monitor.fill(0)
    monitor.blit(background,(0,0))
    
    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            check == False
            pygame.quit()
    
    rotate_min = pygame.transform.rotate(minut, -1 * (6 * time_min) - 160)
    rotate_min_rect = rotate_min.get_rect()
    rotate_min_rect.center = min_rect.center
    monitor.blit(rotate_min,rotate_min_rect)
    
    rotate_sec = pygame.transform.rotate(second, -1 * (6 * time_sec) + 90)
    rotate_sec_rect = rotate_sec.get_rect()
    rotate_sec_rect.center = sec_rect.center
    monitor.blit(rotate_sec, rotate_sec_rect)
    
    time = datetime.now()
    time_min = time.minute
    time_sec = time.second
    
    
    pygame.display.update()
    clock.tick(60)