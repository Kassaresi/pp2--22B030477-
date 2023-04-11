import pygame
import math
pygame.init()
clock = pygame.time.Clock()
width, height = 800, 700
monitor = pygame.display.set_mode((width, height))
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)

def FindVerticesOfEquilateralTriangle(x0,y0,x,y):

    # Calculate the angle between the center and vertex
    theta1 = math.atan2(y - y0, x - x0)

    # Calculate the length of r using the formula we derived earlier
    r = math.sqrt((x - x0)**2 + (y - y0)**2) * 2 / math.sqrt(3)

    # Calculate the coordinates of the other two vertices using the polar coordinate formula
    # with angles of theta1 + 120 degrees and theta1 - 120 degrees
    x1 = x0 + r * math.cos(theta1 + math.radians(120))
    y1 = y0 + r * math.sin(theta1 + math.radians(120))
    x2 = x0 + r * math.cos(theta1 - math.radians(120))
    y2 = y0 + r * math.sin(theta1 - math.radians(120))

    # Return the coordinates of all three vertices
    return [(x, y), (x1, y1), (x2, y2)]


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class GameObject:
    def draw(self):
        return

    def update(self, current_pos):
        return
# Кисточка кнопка
class ButtonPen(GameObject):
    #Создание иконки кисточки
    def __init__(self):
        self.size = 40
        self.pen = pygame.transform.scale(pygame.image.load("/Users/kassi/TSIS9/data_for_snake_TSIS9/penbuttonimages.png"),(40,40))
        self.rect = pygame.draw.rect(monitor,(0, 0, 0),(width // 2 - 150 - self.size // 2,20, self.size, self.size,))
          
    def draw(self):
        monitor.blit(self.pen,(width // 2 - 150 - self.size // 2,20))

    def update(self, current_pos):
        pass


# Правильный треугольник кнопка
class ButtonRightTriangle(GameObject):
    # Создание иконки
    def __init__(self):
        self.size = 40
        self.pen = pygame.transform.scale(pygame.image.load("/Users/kassi/TSIS9/data_for_snake_TSIS9/righttriangle.png"),(40,40))
        self.rect = pygame.draw.rect(monitor, (0, 0, 0), (width // 2 +80 - self.size // 2, 20, self.size, self.size))

    def draw(self):
        monitor.blit(self.pen,(width // 2 +80 - self.size // 2,20))

    def update(self, current_pos):
        pass


# Резинка (ластик) кнопка
class ButtonEraser(GameObject):
    # Создание иконки
    def __init__(self):
        self.size = 40
        self.pen = pygame.transform.scale(pygame.image.load("/Users/kassi/TSIS9/data_for_snake_TSIS9/eraserbutton.png"),(40,40))
        self.rect = pygame.draw.rect(monitor, (0, 0, 0), (width // 2 - 100 - self.size // 2, 20,self.size, self.size))

    def draw(self):
        monitor.blit(self.pen,(width // 2 - 100 - self.size // 2,20))

    def update(self, current_pos):
        pass

# Ромб кнопка
class ButtonRombus(GameObject):
    # Создание иконки
    def __init__(self):
        self.size = 40
        self.pen = pygame.transform.scale(pygame.image.load("/Users/kassi/TSIS9/data_for_snake_TSIS9/rombus.png"),(40,40))
        self.rect = pygame.draw.rect(monitor,(0, 0, 0), (width // 2 +130 - self.size // 2, 20, self.size, self.size))

    def draw(self):
        monitor.blit(self.pen,(width // 2 +130- self.size // 2,20))

    def update(self, current_pos):
        pass

# Правильный треугольник (60,60,60) кнопка
class ButtonEquileiteral(GameObject):
    # Создание иконки 
    def __init__(self):
        self.size = 40
        self.pen = pygame.transform.scale(pygame.image.load("/Users/kassi/TSIS9/data_for_snake_TSIS9/equileiteral.png"),(40,40))
        self.rect = pygame.draw.rect(monitor, (0, 0, 0), (width // 2 +190 - self.size // 2, 20, self.size,self.size))

    def draw(self):
        monitor.blit(self.pen,(width // 2 +190- self.size // 2,20))

    def update(self, current_pos):
        pass


# Прямоугольник кнопка
class ButtonRect(GameObject):
    # Создание иконки
    def __init__(self):
        self.size = 40
        self.rect = pygame.draw.rect(monitor, (0, 0, 0), (width // 2 - 50 - self.size // 2, 20, self.size+10, self.size-10))

    def draw(self):
        pygame.draw.rect(monitor,(255, 255, 255),pygame.Rect(width // 2 -50 - self.size // 2, 20, self.size+10, self.size-10))

    def update(self, current_pos):
        pass

# Квадрат кнопка
class ButtonSquare(GameObject):
    # Создаем иконку
    def __init__(self):
        self.size = 40
        self.rect = pygame.draw.rect(monitor,(0, 0, 0), (width // 2 + 20 - self.size // 2, 20, self.size, self.size,))

    def draw(self):
        pygame.draw.rect(monitor,(255, 255, 255),pygame.Rect(width // 2 +20  - self.size // 2, 20, self.size, self.size))

    def update(self, current_pos):
        pass

# Круг кнопка
class ButtonCircle(GameObject):
    # Создаем иконку
    def __init__(self):
        self.size = 40
        self.rect = pygame.draw.rect(monitor, (0, 0, 0), (width // 2 -200 - self.size // 2, 20, self.size, self.size))

    def draw(self):
        pygame.draw.rect(monitor,(255, 255, 255), pygame.Rect(width // 2 - 200 - self.size // 2, 20, self.size, self.size),0,-1,20,20,20,20)

    def update(self, current_pos):
        pass


#Ручка
class Pen(GameObject):
    # Создание листа
    def __init__(self,draw_font,draw_color,*args, **kwargs):
        self.points: list[Point] = [] 
        self.draw_font=draw_font
        self.draw_color=draw_color
    # Действие кисточки
    def draw(self):
        for idx, point in enumerate(self.points[:-1]):
            next_point = self.points[idx + 1]
            pygame.draw.line(
                monitor,
                self.draw_color,
                start_pos=(point.x, point.y),
                end_pos=(next_point.x, next_point.y),
                width=self.draw_font
            )

    def update(self, current_pos):
        self.points.append(Point(*current_pos))

# Квадрат
class Square(GameObject):
    # Координаты
    def __init__(self, start_pos, draw_font, draw_color, *args, **kwargs):
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)
        self.draw_font = draw_font
        self.draw_color = draw_color

    # Рисуем квадрат
    def draw(self):
        # Начальные координаты
        start_pos_x = self.start_pos.x
        start_pos_y = self.start_pos.y
        # Конечные координаты
        end_pos_x = self.end_pos.x
        end_pos_y = self.end_pos.y
        
        distance = ((start_pos_x-end_pos_x)**2+(end_pos_y-start_pos_y)**2)**0.5
        start_pos_x=start_pos_x-(distance*(2**0.5))/2
        start_pos_y=start_pos_y-(distance*(2**0.5))/2
        # Рисуем
        pygame.draw.rect(
            monitor,
            self.draw_color,
            (
                start_pos_x,
                start_pos_y,
                (distance*(2**0.5)),
                (distance*(2**0.5))

            ),
            width=self.draw_font,
        )

    def update(self, current_pos):
        self.end_pos.x, self.end_pos.y = current_pos

# Правильный треугольник
class EquilateralTriangle(GameObject):
    # Кординаты
    def __init__(self, start_pos,draw_font,draw_color, *args, **kwargs):
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)
        self.draw_font=draw_font
        self.draw_color=draw_color
    # Рисуем
    def draw(self):
        pygame.draw.polygon(monitor,self.draw_color,FindVerticesOfEquilateralTriangle(self.start_pos.x,self.start_pos.y,self.end_pos.x,self.end_pos.y),draw_font)
        
    def update(self, current_pos):
        self.end_pos.x,self.end_pos.y = current_pos

# Прямой треугольник
class RightTriangle(GameObject):
    # Координаты
    def __init__(self, start_pos,draw_font,draw_color, *args, **kwargs):
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)
        self.draw_font=draw_font
        self.draw_color=draw_color
    # Рисуем
    def draw(self):
        third_pos_x=self.end_pos.x
        third_pos_y=self.start_pos.y
        pygame.draw.polygon(monitor,self.draw_color,[(self.start_pos.x,self.start_pos.y),(self.end_pos.x,self.end_pos.y),(third_pos_x,third_pos_y)],self.draw_font)

    def update(self, current_pos):
        self.end_pos.x,self.end_pos.y = current_pos

# Прямоугольник
class Rectangle(GameObject):
    # Координаты
    def __init__(self, start_pos,draw_font,draw_color, *args, **kwargs):
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)
        self.draw_font=draw_font
        self.draw_color=draw_color

    def draw(self):
        # Начальные координаты
        start_pos_x =min(self.start_pos.x, self.end_pos.x)
        start_pos_y = min(self.start_pos.y, self.end_pos.y)
        # Конечные координаты
        end_pos_x = max(self.start_pos.x, self.end_pos.x)
        end_pos_y = max(self.start_pos.y, self.end_pos.y)

        pygame.draw.rect(
            monitor,
            self.draw_color,
            (
                start_pos_x, start_pos_y,
                end_pos_x - start_pos_x,
                end_pos_y - start_pos_y,
            ),
            width=self.draw_font,
        )

    def update(self, current_pos):
        self.end_pos.x,self.end_pos.y = current_pos


# Ромб
class Rombus(GameObject):
    # Координаты
    def __init__(self, start_pos,draw_font,draw_color, *args, **kwargs):
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)
        self.draw_font=draw_font
        self.draw_color=draw_color
        
    def draw(self):
        # Начальные координаты
        start_pos_x =self.start_pos.x
        start_pos_y = self.start_pos.y
        # Конечные координаты
        end_pos_x = self.end_pos.x
        end_pos_y = self.end_pos.y
        distance = ((start_pos_x-end_pos_x)**2+(end_pos_y-start_pos_y)**2)**0.5
        next_pos_x=start_pos_x-(distance*(2**0.5))/2
        next_pos_y=start_pos_y-(distance*(2**0.5))/2

        pygame.draw.polygon(monitor,self.draw_color,
                            [(start_pos_x,abs(start_pos_y-(start_pos_y-end_pos_y)) ),
                             (abs( start_pos_x+(start_pos_x-end_pos_x)),start_pos_y),
                             (start_pos_x,abs(start_pos_y+(start_pos_y-end_pos_y)) ),
                             (abs( start_pos_x-(start_pos_x-end_pos_x)),start_pos_y)],
                             draw_font)

    def update(self, current_pos):
        self.end_pos.x,self.end_pos.y = current_pos

# Круг
class Circle(GameObject):
    # Координаты
    def __init__(self,start_pos,draw_font,draw_color,*arg,**kwarg):
        self.start_pos = Point(*start_pos)
        self.end_pos = Point(*start_pos)
        self.draw_font=draw_font
        self.draw_color=draw_color
    
    def draw(self):
        # Начальные координаты
        center_x=self.start_pos.x
        center_y=self.start_pos.y
        # Конечные координаты
        end_pos_x=self.end_pos.x
        end_pos_y=self.end_pos.y
        print(23)
        # Радиус
        radius=(abs(end_pos_x-center_x)**2+abs(end_pos_y-center_y)**2)**0.5
        pygame.draw.circle(
            monitor,
            self.draw_color,
            (center_x,center_y),
            radius,
            self.draw_font
        )
    
    def update(self, current_pos):
        self.end_pos.x,self.end_pos.y=current_pos
        

def main():
    running = True
    global draw_font
    draw_font=5
    draw_color=white
    # вызов классов
    game_object = GameObject()
    active_obj = game_object
    current_shape = Pen # current_shape()
    button_pen=ButtonPen()
    button_eraser = ButtonEraser()
    button_rect = ButtonRect()
    button_circle=ButtonCircle()
    button_cube=ButtonSquare()
    button_rombus=ButtonRombus()
    button_equileiteral=ButtonEquileiteral()
    button_right_triangle=ButtonRightTriangle()

    objects = [
        (button_pen,0,draw_color),
        (button_rect,0,draw_color),
        (button_eraser,0,draw_color),
        (button_circle,0,draw_color),
        (button_cube,0,draw_color),
        (button_right_triangle,0,draw_color),
        (button_rombus,0,draw_color),
        (button_equileiteral,0,draw_color)
    ]

    while running:
        monitor.fill(black)
        # Выход
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            #При нажатии иконки вызывается класс по картинке, сверху мы их привязали
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.rect.collidepoint(event.pos):
                    current_shape = Rectangle
                    draw_color= white
                elif button_circle.rect.collidepoint(event.pos):
                    current_shape = Circle
                    draw_color= white
                elif button_pen.rect.collidepoint(event.pos):
                    current_shape = Pen
                    draw_color= white
                elif button_cube.rect.collidepoint(event.pos):
                    current_shape = Square
                    draw_color= white
                elif button_eraser.rect.collidepoint(event.pos):
                    current_shape = Pen
                    draw_color=(0,0,0)
                elif button_right_triangle.rect.collidepoint(event.pos):
                    current_shape = RightTriangle
                    draw_color=white
                elif button_rombus.rect.collidepoint(event.pos):
                    current_shape = Rombus
                    draw_color=white
                elif button_equileiteral.rect.collidepoint(event.pos):
                    current_shape = EquilateralTriangle
                    draw_color=white
                else:
                    active_obj = current_shape(start_pos=pygame.mouse.get_pos(),draw_font=draw_font,draw_color=draw_color)
                    objects.append((active_obj,draw_font,draw_color))
                    
            # Движение мыши
            if event.type == pygame.MOUSEMOTION:
                active_obj.update(current_pos=pygame.mouse.get_pos())
            # При отпускании мыши, смена конечной координаты останавливается и накладывается рисунок, точнее пиксели принимают определенный цвет
            if event.type == pygame.MOUSEBUTTONUP:
                active_obj = game_object
            
            # Нажатия на клавиша
            if event.type == pygame.KEYDOWN:
                # Увеличивает толщину
                if event.key == pygame.K_UP:
                    draw_font=min(100,draw_font+3)
                # Уменьшает толщину
                if event.key == pygame.K_DOWN:
                    draw_font=max(1,draw_font-3)
                # Меняет цвет
                if event.key == pygame.K_r:
                    draw_color=(255,0,0)
                elif event.key == pygame.K_g:
                    draw_color=(0,255,0)
                elif event.key == pygame.K_b:
                    draw_color=(0,0,255)
                
        
        for obj in objects:
            obj[0].draw_font=obj[1]
            obj[0].draw_color=obj[2]
            obj[0].draw()
        # ФПС
        clock.tick(60)
        pygame.display.flip()


if __name__ == '__main__':
    main()