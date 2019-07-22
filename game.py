import pygame
pygame.init()

win = pygame.display.set_mode((1040,480))

pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('1.png'), pygame.image.load('4.png'), pygame.image.load('5.png'), pygame.image.load('6.png'), pygame.image.load('7.png'), pygame.image.load('8.png'), pygame.image.load('9.png'), pygame.image.load('10.png'), pygame.image.load('11.png')]
walkLeft = [pygame.image.load('13.png'), pygame.image.load('14.png'), pygame.image.load('15.png'), pygame.image.load('16.png'), pygame.image.load('17.png'), pygame.image.load('18.png'), pygame.image.load('19.png'), pygame.image.load('20.png'), pygame.image.load('21.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

bulletSound = pygame.mixer.Sound('bullet.ogg')
hitSound = pygame.mixer.Sound('hit.ogg')

music = pygame.mixer.music.load('secuestro.mp3')
pygame.mixer.music.play(-1)

score = 0

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def hit(self):
        self.isJump = False
        self.jumpCount = 10
        self.x = 200
        self.y = 207
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('-5', 1, (255,0,0))
        win.blit(text, (250 - (text.get_width()/2),200))
        pygame.display.update()
        i = 0
        while i < 20:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 20
                    pygame.quit()
                


class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)


class enemy(object):
    
    walkLeft = [pygame.image.load('a.png'), pygame.image.load('b.png'), pygame.image.load('c.png'), pygame.image.load('d.png'), pygame.image.load('e.png'), pygame.image.load('f.png'), pygame.image.load('g.png'), pygame.image.load('h.png'), pygame.image.load('i.png'), pygame.image.load('j.png'), pygame.image.load('k.png'),pygame.image.load('l.png'),pygame.image.load('m.png'),pygame.image.load('n.png'),pygame.image.load('o.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True

    def draw(self,win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 45:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(win, (255,0,0), (self.hitbox[0]-20, self.hitbox[1] + 5, 50, 2))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0]-20, self.hitbox[1] + 5, 50 - (5 * (10 - self.health)), 2))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x -= self.vel
            

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print('hit')

        

def redrawGameWindow():
    win.blit(bg, (0,0))
    text = font.render('Score: ' + str(score), 1, (0,0,0))
    win.blit(text, (390, 10))
    man.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    
    pygame.display.update()


#mainloop
