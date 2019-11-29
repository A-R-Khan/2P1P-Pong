import pygame,random,time,math

pygame.init()
font=pygame.font.Font(pygame.font.get_default_font(),30)
screen=pygame.display.set_mode((1280,600))

WHITE=(255,255,255)

class players(pygame.sprite.Sprite):
    def __init__(self,x):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((20,100))
        self.image.fill(WHITE)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=10

    def move(self,dist):
        self.rect.y+=dist

    @staticmethod
    def checkkeys():
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_w:
                    player1.move(-50)
                elif event.key==pygame.K_s:
                    player1.move(50)
                elif event.key==pygame.K_i:
                    player2.move(-50)
                elif event.key==pygame.K_k:
                    player2.move(50)
                elif event.key==pygame.K_q:
                    pygame.quit()
            elif event.type==pygame.QUIT:
                    pygame.quit()

class Ball(pygame.sprite.Sprite):
    ballist=[]
    def __init__(self,dirn):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((20,20))
        self.image.fill(WHITE)
        self.rect=self.image.get_rect()
        self.rect.x=640
        self.rect.y=300
        self.y_vc=random.randint(4,7)*random.choice([1,-1])
        self.x_vc=random.randint(4,7)*dirn
        Ball.ballist.append(self)
        self.dirn=dirn
        
    def moveball(self):
        self.rect.x += self.x_vc
        self.rect.y += self.y_vc
                
    def hit(self,changed):
        if changed=='x':
            self.x_vc=-self.x_vc
        elif changed=='y':
            self.y_vc=-self.y_vc            

    @staticmethod
    def check_points():
        for ball in Ball.ballist:
            if ball.rect.x>1300:
                return 2
            elif ball.rect.x<=0:
                return 1
            else:
                return False

    def reset(self):
        self.rect.y=random.randrange(200,400)
        self.rect.x=random.randrange(620,660)
        self.y_vc=random.randint(4,7)*random.choice([1,-1])
        self.x_vc=random.randint(4,7)*self.dirn
        
player1=players(20)
player2=players(1240)
ball=Ball(1)
ball2=Ball(-1)

group=pygame.sprite.Group()
group.add(player1)
group.add(player2)
group.add(ball)
group.add(ball2)

playergroup=pygame.sprite.Group()
playergroup.add(player1)
playergroup.add(player2)

clock=pygame.time.Clock()
resultset=[0,0]

while True:
    group.draw(screen)
    ball.moveball()
    ball2.moveball()
    result = Ball.check_points()
    if result:
        resultset[result-1]+=1
        ball.reset()
        ball2.reset()
        time.sleep(1)
    if ball.rect.y<0 or ball.rect.y>580:
        ball.hit('y')
    if ball2.rect.y<0 or ball2.rect.y>580:
        ball2.hit('y')
    elif pygame.sprite.spritecollide(ball,playergroup,False):
        ball.hit('x')
    elif pygame.sprite.spritecollide(ball2,playergroup,False):
        ball2.hit('x')

    fontsurf=font.render(str(resultset[1])+"-"+str(resultset[0]),False,WHITE)
    screen.blit(fontsurf,(600,10))
    players.checkkeys()
    clock.tick(60)
    pygame.display.flip()
    screen.fill((0,0,0))
        
    
    





