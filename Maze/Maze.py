from pygame import *

window = display.set_mode((1000, 1000))
display.set_caption("THE LABIRINT")

background = transform.scale(image.load("background.png"), (1000, 1000))

class GameSprite(sprite.Sprite):
    def __init__(self, PlayerImage, x, y, speed):
        super().__init__()
        self.PlayerImage = transform.scale(image.load(PlayerImage), (65, 65))
        self.rect = self.PlayerImage.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        window.blit(self.PlayerImage, (self.rect.x, self.rect.y))
    
class Screamer(sprite.Sprite):
    def __init__(self, PlayerImage, x, y):
        super().__init__()
        self.PlayerImage = transform.scale(image.load(PlayerImage), (1000, 1000))
        self.rect = self.PlayerImage.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.PlayerImage, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
    
        if keys[K_RIGHT] and self.rect.x < 995:
            self.rect.x += self.speed

        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_DOWN] and self.rect.y < 995:
            self.rect.y += self.speed
    
class Enemy(GameSprite):
    direction = "l"
    direction2 = "0"
    def update(self):
        if self.rect.x <= 170:
            self.direction = "r"
        if self.rect.x >=850:
            self.direction = "l"
        if self.direction == "l":
            self.rect.x -= 2
        if self.direction == "r":
            self.rect.x += 2
        if self.rect.y <= 0:
            self.direction2 = "u"
        if self.rect.y >= 800:
            self.direction2 = "d"
        if self.direction2 == "d":
            self.rect.y -= 2
        if self.direction2 == "u":
            self.rect.y += 2
        direction2 = "u"

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
        

sprite1 = Player("sprite1.png", 930, 820, 2)
sprite2 = Enemy("sprite2.png", 430, 300, 5)
enemy2 = Enemy("sprite2.png", 270, 100, 3)
enemy2.direction2 = "u"
enemy2.direction = "a"
sprite3 = GameSprite("sprite3.png", 930, 300, 5)
screamer = Screamer("screamer.png", 0, 0)
wall_1 = Wall(196, 0, 1, 260, 5, 10, 800)
wall_2 = Wall(196, 0, 1, 350, 472, 640, 10)
wall_3 = Wall(196, 0, 1, 350, 372, 640, 10)
wall_4 = Wall(196, 0, 1, 350, 272, 640, 10)
wall_5 = Wall(196, 0, 1, 0, 472, 270, 10)
wall_6 = Wall(196, 0, 1, 350, 472, 10, 330)


game = True
FPS = 60
timer = time.Clock()
mixer.init()
mixer.music.load("OST.mp3")
mixer.music.play()
scream = mixer.Sound('scream.mp3')

font.init()
font = font.SysFont("Arial", 50)
win = font.render("Ти багатий!", True, (0, 0, 255))
lose = font.render("Ти програв!", True, (255, 0, 0))
finish = False

while game:
    if finish == False:
        window.blit(background, (0,0))
        sprite1.update()
        sprite2.update()
        enemy2.update()
        sprite1.reset()
        sprite2.reset()
        enemy2.reset()
        sprite3.reset()
        wall_1.draw_wall()
        wall_2.draw_wall()
        wall_3.draw_wall()
        wall_4.draw_wall()
        wall_5.draw_wall()
        wall_6.draw_wall()
      

    for e in event.get():
        if e.type == QUIT:
            game = False
    if sprite.collide_rect(sprite1, sprite3):
        finish = True
        window.blit(win, (500, 400))

    if sprite.collide_rect(sprite1, sprite2):
        finish = True
        window.blit(lose, (500, 400))
        screamer.reset()
        mixer.music.stop()
        scream.play()

    if sprite.collide_rect(sprite1, enemy2):
        finish = True
        window.blit(lose, (500, 400))
        screamer.reset()
        mixer.music.stop()
        scream.play()

    if sprite.collide_rect(sprite1, wall_1):
        finish = True
        window.blit(lose, (500, 400))

    if sprite.collide_rect(sprite1, wall_2):
        finish = True
        window.blit(lose, (500, 400))
    if sprite.collide_rect(sprite1, wall_3):
        finish = True
        window.blit(lose, (500, 400))

    if sprite.collide_rect(sprite1, wall_4):
        finish = True
        window.blit(lose, (500, 400))
        
    if sprite.collide_rect(sprite1, wall_5):
        finish = True
        window.blit(lose, (500, 400))

    if sprite.collide_rect(sprite1, wall_6):
        finish = True
        window.blit(lose, (500, 400))
    
    
    display.update()
    timer.tick(FPS)

