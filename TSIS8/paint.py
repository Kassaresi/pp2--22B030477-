import pygame

#functions
def erase():
    rect_pos = pygame.mouse.get_pos()
    rect_width = 30
    rect_height = 30
    pygame.draw.rect(monitor, white, (rect_pos, (rect_width, rect_height)))

def cirlce():
    circle_pos = pygame.mouse.get_pos()
    circle_radius = 30
    pygame.draw.circle(monitor, color, circle_pos, circle_radius)

def rectangle():
    rect_pos = pygame.mouse.get_pos()
    rect_width = 50
    rect_height = 50
    pygame.draw.rect(monitor, color, (rect_pos, (rect_width, rect_height)))

#Функция считывает передвижение кисти, без нее линия будет обрывчитывой, а с ней прямая и аккуратная
def roundline(canvas, color, start, end, radius=1) :
    Xaxis = end[0] - start[0]
    Yaxis = end[1] - start[1]
    dist = max(abs(Xaxis), abs(Yaxis))
    for i in range(dist) :
        x = int(start[0] + float(i) / dist * Xaxis)
        y = int(start[1] + float(i) / dist * Yaxis)
        pygame.draw.circle(canvas, color, (x, y), radius)
    
pygame.init()
#Монитор, название и иконка
monitor = pygame.display.set_mode((800,600))
pygame.display.set_caption("Paint")
pygame.display.set_icon(pygame.image.load("/Users/kassi/TSIS8/data_for_paint/icon_for_paint.webp"))

#Доп файлы для TSIS 9 
# erase = pygame.image.load("/Users/kassi/TSIS8/data_for_paint/image_eraser.png")
# brush = pygame.image.load("/Users/kassi/TSIS8/data_for_paint/image_brush.png")
# rectangle = pygame.image.load("/Users/kassi/TSIS8/data_for_paint/icon_rectangle.png")
# circle = pygame.image.load("/Users/kassi/TSIS8/data_for_paint/icon_circle.png")

#Colors
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
yellow = (255,255,0)
light_blue = (0,255,255)
pink = (255,0,255)

#Начальные значания или константы
color = red
last_pos = (0,0)
mouse_down = False
monitor.fill(white)
pygame.display.update()
radius = 5


#FPS
clock = pygame.time.Clock()
check = True

while check:
    action = pygame.event.wait()
    
    #Exit
    if action.type == pygame.QUIT:
        check = False
        pygame.quit()
        
    #Keybord
    if action.type == pygame.KEYDOWN:
        #Переключение цветов
        if action.key == pygame.K_r:
            color = red
            radius = 5
        elif action.key == pygame.K_b:
            color = blue
            radius = 5
        elif action.key == pygame.K_g:
            color = green
            radius = 5
            
        #Erase
        if action.key == pygame.K_e:
            erase()
        
        #erase (pressed)
        if action.key == pygame.K_w:
            color = white
            radius = 20
        
        #Rectange (p - от слова прямоугольник)
        if action.key == pygame.K_p:
            rectangle()
            
        #Circle
        if action.key == pygame.K_c:
            cirlce()
            
    #Mouse (brush) При нажатии мыши значение mouse_down меняется на True, что означает мышь активирована
    if action.type == pygame.MOUSEBUTTONDOWN:
        pygame.draw.circle(monitor, color, action.pos, 5)
        mouse_down = True
    
    #При отпускании мыши значение mouse_down меняется на False, что означает мышь диактивирована
    if action.type == pygame.MOUSEBUTTONUP:
        mouse_down = False
    
    
    if action.type == pygame.MOUSEMOTION:
        if mouse_down:
            pygame.draw.circle(monitor,color,action.pos,radius)
            roundline(monitor,color,action.pos,last_pos,radius)
        last_pos = action.pos
        
    pygame.display.update()
    #ФПС
    clock.tick(60)