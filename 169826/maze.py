from pygame import *

'''Необходимые классы'''
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset (self):
        window.blit(self.image, (self.rect.x, self.rect.y))



class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


class Enemy(GameSprite):

    naprav = 'left'
    def update(self):
        if self.rect.x <= win_width - 230:
            self.naprav = 'right'
        if self.rect.x >= win_width - 85:
            self.naprav = 'left'

        if self.naprav == 'left':
            self.rect.x -= self.speed
        if self.naprav == 'right':
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3

        self.width = wall_width
        self.height = wall_height
        
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))

        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

win_width = 700
win_height = 500
window = display.set_mode((win_width,win_height))
display.set_caption('labirint')

background = transform.scale(image.load('cat.jpg'),(win_width,win_height))


player = Player('lol.png', 5, win_height - 80, 5)

monstr = Enemy('aga.png', win_width - 80, 280, 2)

final = GameSprite('erre.png', win_width-120, win_height-80, 0)

w1 = Wall(200,70,90,  100,20,  650,20)

w2 = Wall(200,70,90,  100,20,  20,300)

w3 = Wall(200,70,90,  200,300,  20,300)

w4 = Wall(200,70,90,  300,20,  20,300)

mixer.init()
mixer.music.load('papa.mp3')
mixer.music.play()


game = True
clock = time.Clock()

font.init()
font = font.Font(None, 70)
win = font.render('УРА ПОБЕДА!', True, (255, 215, 0))
lose = font.render('НЕЕЕЕЕЕЕЕЕТ!', True, (180, 0, 0))

ydar = mixer.Sound('kick.ogg')
pobed = mixer.Sound('money.ogg')

while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background,(0,0))
    player.reset()
    monstr.reset()
    final.reset()
    w1.draw_wall()
    w2.draw_wall()
    w3.draw_wall()
    w4.draw_wall()
    if game:
        player.update()
        monstr.update()

    if sprite.collide_rect(player,w1) or sprite.collide_rect(player,w2) or sprite.collide_rect(player,w3) or sprite.collide_rect(player,w4) or sprite.collide_rect(player,monstr):
        game = False
        window.blit(lose, (200,200))
        ydar.play()

    if sprite.collide_rect(player,final):
        game = False
        window.blit(win, (200,200))
        pobed.play()

    display.update()
    clock.tick(60)