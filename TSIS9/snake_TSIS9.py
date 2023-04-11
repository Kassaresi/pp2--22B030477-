import pygame, random, datetime

pygame.init()


def game():
    class Apple():
        global monitor
        def __init__(self):
            #Даем рандомное значение яблока
            self.weight = random.randint(1, 5)
            # Рандомная позиция яблока
            self.pos = (random.randint(1, monitor.get_width() / 10 - 1) * 10, random.randint(10, monitor.get_height() / 10 - 1) * 10)
            self.spawn = True
        # Обновление после истечении времени
        def updates(self):
            # После окончания таймера яблоко заново регенерируется (если игрок не успел)
            self.pos = (random.randint(1, monitor.get_width() / 10 - 1) * 10, random.randint(10, monitor.get_height() / 10 - 1) * 10)
            self.weight = random.randint(1, 5)
            # До обновления места расположения яблока 10 секунд
            self.lifetime = 10
    # Раширение экрана
    monitor = pygame.display.set_mode((400, 500))
    # Цвета
    white = (255,255,255)
    black = (0,0,0)
    red = (255,0,0)
    # Начало и конец линии которая является четвертой стенкой, благодаря этому мы имеем ровный квадрат (400,400) и место для счетчика
    head_line_start = (0, 100)
    head_line_end = (400, 100)
    # Вызываем класс
    app = Apple()
    # ФПС
    clock = pygame.time.Clock()
    
    running = True
    score = 0
    speed = 1
    # Массив с названиями уровней
    list_of_level = ['easy', 'normal', 'hard', 'very hard', 'impossible', 'impossible x2', 'death']
    score_font = pygame.font.SysFont('lunchtime Doubly So', 32)
    # Направление
    change = 'left'
    direction = 'left'

    player_pos = [220, 200]
    snake = [[220, 200], [230, 200], [240, 200]]
    
    # Событие (таймер)
    minuslife = pygame.USEREVENT + 1
    pygame.time.set_timer(minuslife, 1000)
    
    while running:
        for action in pygame.event.get():
            # Выход
            if action.type == pygame.QUIT:
                return 0
            
            # Управление змейкой
            if action.type == pygame.KEYDOWN:
                if action.key == pygame.K_w or action.key == pygame.K_UP:
                    change = 'up'
                if action.key == pygame.K_s or action.key == pygame.K_DOWN:
                    change = 'down'
                if action.key == pygame.K_a or action.key == pygame.K_LEFT:
                    change = 'left'
                if action.key == pygame.K_d or action.key == pygame.K_RIGHT:
                    change = 'right'
                    
            # Таймер 
            if action.type == minuslife:
                print(1)
                app.lifetime -= 1
                if app.lifetime == 0:
                    app.updates()
                    
        # Изменение направления змейки
        if direction != 'up' and change == 'down':
            direction = 'down'
        if direction != 'down' and change == 'up':
            direction = 'up'
        if direction != 'left' and change == 'right':
            direction = 'right'
        if direction != 'right' and change == 'left':
            direction = 'left'
            
        # Скорость змейки
        if direction == 'up':
            player_pos[1] -= 10
        if direction == 'down':
            player_pos[1] += 10
        if direction == 'left':
            player_pos[0] -= 10
        if direction == 'right':
            player_pos[0] += 10
            
        # Обновление яблока, при поглощении его
        while app.spawn:
            app.updates()
            if app.pos not in snake:
                app.spawn = False

        snake.insert(0, list(player_pos))
        # Когда координаты яблока и змейки совпадают, то это защитывается как змея съело яблоко
        if player_pos[0] == app.pos[0] and player_pos[1] == app.pos[1]:
            score += app.weight
            app.spawn = True
            speed = score // 4 + 1
        else:
            snake.pop()
        # Обновляем фон
        monitor.fill(white)
        # Рисуем линию которая будет являться верхней границой
        pygame.draw.line(monitor, black, head_line_start, head_line_end, 1)

        # Death
        if ((player_pos[0] < -5 or player_pos[0] > monitor.get_width() - 5) or (
                player_pos[1] < 100 or player_pos[1] > monitor.get_height() - 5)):
            break
        if player_pos in snake[1:]:
            break
        
        # Рисование объектов
        for pos in snake:
            pygame.draw.rect(monitor, black, pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(monitor, red, pygame.Rect(app.pos[0],app.pos[1], 10, 10))
        
        monitor.blit(score_font.render(f'Score: {score}', True, 'black'), (20, 38))
        if speed <= 7:
            monitor.blit(score_font.render(f'Speed: {list_of_level[speed - 1]}', True, 'black'), (20, 58))
        else:
            monitor.blit(score_font.render(f'Speed: death', True, 'black'), (20, 58))
        pygame.display.update()
        
        # ФПС
        clock.tick(10 + speed*2)
        
        
    # При проигрыше, мы имеем право заново запустить игру или выйти, а так же увидеть наш счет
    while running:
        for action in pygame.event.get():
            if action.type == pygame.QUIT:
                running = False
            # При нажатии на r(restart) игра обновляется, а при нажатии q(quit) выходим из игры
            if action.type == pygame.KEYDOWN:
                if action.key == pygame.K_r:
                    game()
                if action.key == pygame.K_q:
                    running = False
        monitor.fill(white)
        
        # Надписи после проигрыша
        monitor.blit(score_font.render('Press R for restart or Q for quit', True, 'black'), (35, 200))
        monitor.blit(score_font.render(f'Score: {score}', True, black), (35,225))
        pygame.display.update()


game()
pygame.quit()