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
    def update1(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= speed
        if key_pressed[K_DOWN] and self.rect.y < 800 - 130 - 5:
            self.rect.y += speed
    def update2(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= speed
        if key_pressed[K_s] and self.rect.y < 800 - 130 - 5:
            self.rect.y += speed

class Ball(GameSprite):
    def update(self):
        self.rect.x += self.speed
        self.rect.y += self.speed

raketka1 = Player('raketka.png', 1000, 300, speed, 150, 150)
raketka2 = Player('raketka.png', 80, 300, speed, 150, 150)

myach = Ball('myach.png', 500, 300, speed, 150, 150)

lose = font.render('Игрок 1 проиграл', True, (255, 255, 255))
lose2 = font.render('Игрок 2 проиграл', True, (255, 255, 255))

clock = time.Clock()
fps = 60
game = True
finish = False

speedx = 6
speedy = 6
while game:
    if finish != True:
        myach.rect.x += speedx
        myach.rect.y += speedy
        background.fill((0, 255, 255))
        raketka1.reset()
        raketka1.update1()
        raketka2.reset()
        raketka2.update2()
        myach.reset()
        if myach.rect.y > 800 - 130 or myach.rect.y < 0:
            speedy *= -1
        if myach.rect.x > 1200 - 130:
            finish = True
            background.blit(lose2, (500, 300))
        if myach.rect.x < 0:
            finish = True
            background.blit(lose, (500, 300))
        if sprite.collide_rect(myach, raketka1) or sprite.collide_rect(myach, raketka2):
            speedx *= -1
    for e in event.get():
        if e.type == QUIT:
            game = False



    clock.tick(fps)
    display.update()
