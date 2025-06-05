from pygame import *
from random import *

window = display.set_mode((700,700))
display.set_caption("Змейка")
font.init()
font = font.SysFont("Arial", 36)
win = font.render('Ты выйграл!' , 1, (33, 168, 19))
lose = font.render('Ты проиграл!' , 1, (186, 17, 17))

# основные параметры игры
cell_size = 20 #размер пикселя(ячейки)
snake_speed = 5 
snake_length = 3 #начальня длина змейки
snake_body = [] #список хранящий сьеденные яблоки(тело змейки)

for i in range(snake_length):
    snake_body.append(Rect(350 - (20 * i), 350, 20, 20)) #добавление в список сьеденнные яблоки
snake_direction = "right"
new_direction = "right"
apple_position = Rect(randint(0, 680), randint(0, 680), 20, 20)

clock = time.Clock()
game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_w and snake_direction != "down":
                new_direction = "up"
            elif e.key == K_s and snake_direction != "up":
                new_direction = "down"
            elif e.key == K_a and snake_direction != "right":
                new_direction = "left"
            elif e.key == K_d and snake_direction != "left":
                new_direction = "right"


    if not finish:
        # новое направление движения
        snake_direction = new_direction
        # управление змейкой
        if snake_direction == "up":
            snake_body.insert(0, Rect(snake_body[0].left, snake_body[0].top - 20, 20, 20))
        elif snake_direction == "down":
            snake_body.insert(0, Rect(snake_body[0].left, snake_body[0].top + 20, 20, 20))
        elif snake_direction == "left":
            snake_body.insert(0, Rect(snake_body[0].left - 20, snake_body[0].top, 20, 20))
        elif snake_direction == "right":
            snake_body.insert(0, Rect(snake_body[0].left + 20, snake_body[0].top, 20, 20))

        # проверяем, съела ли змея яблоко
        if snake_body[0].colliderect(apple_position):
            apple_position = Rect(randint(0, 680), randint(0, 680), 20, 20)
            snake_length += 1

        if len(snake_body) > snake_length:
            snake_body.pop()
            
        window.fill((25, 25, 112))
        # проверка столкновения со стенами
        if snake_body[0].left < 0 or snake_body[0].right > 700 or snake_body[0].top < 0 or snake_body[0].bottom > 700:
            finish = True
            window.blit(lose, (250,250))
        # проверка столкновения с собственным телом
        for i in range(1, len(snake_body)):
            if snake_body[0].colliderect(snake_body[i]):
                finish = True
                window.blit(lose, (250,250))
        
        # рисуем змейку
        for i in range(len(snake_body)):
            if i == 0:
                draw.circle(window, (0, 200, 0), snake_body[i].center, 20 / 2)
            else:
                draw.circle(window, (0, 200, 0), snake_body[i].center, 20 / 2)
                draw.circle(window, (0, 200, 0), snake_body[i].center, 20 / 4)

        # рисуем яблоко
        draw.circle(window, (255, 0, 0), apple_position.center, cell_size / 2)

        # выводим количество яблок
        score_text = font.render(f"Съедено яблок: {snake_length - 3}", True, (255, 255, 255))
        window.blit(score_text, (10, 10))

        display.update()
        clock.tick(snake_speed)


