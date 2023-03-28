import pygame


pygame.init()
monitor = pygame.display.set_mode((1000,751))
pygame.display.set_caption("mp3")
pygame.display.set_icon(pygame.image.load("/Users/kassi/TSIS7/data_for_TSIS7/icon_for_mp3.png"))

background = pygame.image.load("/Users/kassi/TSIS7/data_for_TSIS7/background_for_mp3.jpeg")

def next():
    global song
    song = song[1:] + [song[0]]
    pygame.mixer.music.stop()
    pygame.mixer.music.load(song[0])
    pygame.mixer.music.play()

def previous():
    global song
    song = song[-1:] + song[:-1]
    pygame.mixer.music.stop()
    pygame.mixer.music.load(song[0])
    pygame.mixer.music.play()

song = [
    "/Users/kassi/TSIS7/mp3/Franz_Gordon_-_Togetherless.mp3",
    "/Users/kassi/TSIS7/mp3/George_Davidson_-_Mariage_DAmour.mp3",
    "/Users/kassi/TSIS7/mp3/Ludovico_Einaudi_-_Einaudi_I_Giorni.mp3"
]



check = True
while check:
    monitor.blit(background,(0,0))
    pygame.display.update()
    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            check = False
            pygame.quit()
        #Next or previous
        if action.type == pygame.KEYDOWN and action.key == pygame.K_LEFT:
            next()
        if action.type == pygame.KEYDOWN and action.key == pygame.K_RIGHT:
            previous()
        #Pause and continuos
        if action.type == pygame.KEYDOWN and action.key == pygame.K_s:
            pygame.mixer.music.pause()
        if action.type == pygame.KEYDOWN and action.key == pygame.K_c:
            pygame.mixer.music.unpause()
    pygame.display.flip()