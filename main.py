from pygame import *

font.init()
font = font.Font(None, 70)

background = display.set_mode((1200, 800))
display.set_caption('Пинг-понг')


speed = 10

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_height):
        super().__init__()
        self.width = player_width
        self.height = player_height
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        background.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_RIGHT] and self.rect.x < 1200 - 130 - 5:
            self.rect.x += speed
        if key_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= speed



lose = font.render('Ты не выиграл', True, (255, 255, 255))

clock = time.Clock()
fps = 60
game = True
finish = False

while game:
    if finish != True:
        background.fill((0, 255, 255))
    for e in event.get():
        if e.type == QUIT:
            game = False




    clock.tick(fps)
    display.update()
