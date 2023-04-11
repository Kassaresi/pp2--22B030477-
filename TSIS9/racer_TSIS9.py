#Imports
import pygame, sys
from pygame.locals import *
import random, time
 
#Initialzing 
pygame.init()
 
#Setting up FPS 
fps = 60
clock = pygame.time.Clock()
 
#Creating colors
blue  = (0, 0, 255)
red   = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
 
#Other Variables for use in the program
scr_width = 565
scr_height = 650
speed = 5
score = 0
coins = 0
 
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, black)
scoring = font.render("Score",True,black)

background = pygame.image.load("/Users/kassi/TSIS9/data_for_racer_TSIS9/background_racer.jpg")
 
#Create a white screen 
monitor= pygame.display.set_mode((scr_width,scr_height))
monitor.fill(white)
pygame.display.set_caption("Game")
score_font = pygame.font.SysFont('lunchtime Double So',32)

# Это генераторы, в них входят враждебные машины, монетки и сам игрок
class Enemy(pygame.sprite.Sprite):
    #Генерация вражеской машины, которая появляется на верху карты, также имеет картинку 
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("/Users/kassi/TSIS9/data_for_racer_TSIS9/enemy_car.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, scr_width-10), 0)  
    #Движение вражеской машины, движение происходит с верху в вниз. Если мы смогли уклониться от машины, то получаем очко и скорость вражеской машины увеличивается
      def move(self):
        self.rect.move_ip(0,speed)
        if (self.rect.top > scr_height):
            self.rect.top = 0
            self.rect.center = (random.randint(40, scr_width - 10), 0)
 

class Player(pygame.sprite.Sprite):
    #Генерация нашей машины
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("/Users/kassi/TSIS9/data_for_racer_TSIS9/player_car.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    #Движение нашей машины, которая может передвигаться на 360 градусов
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < scr_width:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                  
class Coin(pygame.sprite.Sprite):
    #Генерация монеток
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/kassi/TSIS9/data_for_racer_TSIS9/coin_for_racer.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, 360), random.randint(-100, 0))
        self.weight = 1
        self.mask = pygame.mask.from_surface(self.image)

    #Движение монеток схожи с движением вражеской машины. Количество монеток можно изменить ниже
    def move(self):
        global score,coins
        if self.rect.top > scr_height:
            self.rect.top = 0
            self.rect.center = (random.randint(40, 450), 0)
        elif pygame.sprite.spritecollide(self, player , False, pygame.sprite.collide_mask):
            coins += self.weight
            score += self.weight
            self.rect.top = 0
            self.rect.center = (random.randint(40,450), 0)
        elif pygame.sprite.spritecollideany(self, enemies, pygame.sprite.collide_mask):
            self.rect.center = (random.randint(40,450), 0)

        self.rect.move_ip(0, speed)
        
class pikachu(pygame.sprite.Sprite):
    #Генерация монеток
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/kassi/TSIS9/data_for_racer_TSIS9/pokemon_coin_racer.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, 360), random.randint(-100, 0))
        self.weight = 3
        self.mask = pygame.mask.from_surface(self.image)

    #Движение монеток схожи с движением вражеской машины. Количество монеток можно изменить ниже
    def move(self):
        global score
        #Когда мы пропускаем монетку, чтобы она не ушла вне экрана, мы даем границу. Когда монетка проходит границу она обновляется заново
        if self.rect.top > scr_height:
            self.rect.top = 0
            self.rect.center = (random.randint(40, 450), 0)
        elif pygame.sprite.spritecollide(self, player , False, pygame.sprite.collide_mask):
            score += self.weight
            self.rect.top = 0
            self.rect.center = (random.randint(40,450), 0)
        elif pygame.sprite.spritecollideany(self, enemies, pygame.sprite.collide_mask):
            self.rect.center = (random.randint(40,450), 0)

        self.rect.move_ip(0, speed)
#Setting up Sprites        
p1 = Player()
e1 = Enemy()
 
#Creating Sprites Groups
player = pygame.sprite.Group()
player.add(p1)
coins_group = pygame.sprite.Group()
pikachu_group = pygame.sprite.Group()
enemies = pygame.sprite.Group()
enemies.add(e1)
all_sprites = pygame.sprite.Group()
all_sprites.add(p1)
all_sprites.add(e1)
 
#Adding a new User event 
inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 1000)

#Numbers coins
for i in range(3):
    c1 = Coin()
    coins_group.add(c1)
    all_sprites.add(c1)
    
for i in range(1):
    pika = pikachu()
    coins_group.add(pika)
    all_sprites.add(pika)
 
#Game Loop
while True:
       
    #Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == inc_speed:
            if coins % 5 == 0 and coins >= 5:
                speed = speed + 1   
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #Декарации и счетчик очков и монеток во время игры
    monitor.blit(background, (0,0))
    scores = font_small.render((f'Score: {score}'), True, black)
    coins_view = font_small.render(f'Coins: {coins}',True,black)
    monitor.blit(scores, (10,10))
    monitor.blit(coins_view,(460,10))
    
 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        monitor.blit(entity.image, entity.rect)
        entity.move()
 
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(p1, enemies):
        # При столкновении с вражеской машиной, происходит музыкальное сопровождение
          pygame.mixer.Sound('/Users/kassi/TSIS9/data_for_racer_TSIS9/crash.wav').play()
          time.sleep(0.5)
        # При поражении выходит красный экран с надписью (Game Over)
          monitor.fill(red)
          monitor.blit(game_over, (100,250))
          monitor.blit(score_font.render(f'Score: {score}', True,black), (110,320))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
    pygame.display.update()
    #Частота кадров (60 стандарт)
    clock.tick(fps)