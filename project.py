from pygame import *
from random import *

x1 = 300
y1 = 300
razmer_zmei = 10
x1_change = 0
y1_change = 0

class snake():
    def __init__(self, player_image, player_x, player_y, player_speed, w = 90, h = 90):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))




class player(snake):
    def update(self):




red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
blue = (150, 255, 255)

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('snake game')
clock = time.Clock()
FPS = 30

font.init()
font = font.Font(None, 70)
lose = font.render('YOU LOSE!', True, (255, 0, 0))

snake = player("Sqr.png",x1,y1,4)


eda_x = randint(0, win_width - razmer_zmei)
eda_y = randint(0, win_height - razmer_zmei)

x_list = []
y_list = []

run = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_LEFT:
                x1_change = -razmer_zmei
                y1_change = 0
            elif e.key == K_RIGHT:
                x1_change = razmer_zmei
                y1_change = 0
            elif e.key == K_UP:
                y1_change = -razmer_zmei
                x1_change = 0
            elif e.key == K_DOWN:
                y1_change = razmer_zmei
                x1_change = 0
    if run != True:
        snake.reset()
        snake.update()
        window.fill(blue)
        clock.tick(FPS)
        draw.rect(window, black, (x1, y1, razmer_zmei, razmer_zmei))
        draw.rect(window, red, (eda_x, eda_y, razmer_zmei, razmer_zmei))
        x1 += x1_change
        y1 += y1_change
    if x1 >= win_width or x1 < 0 or y1 >= win_height or y1 < 0:
        run = True
        window.blit(lose,(200,200))









    display.update()