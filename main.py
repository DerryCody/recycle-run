import pygame,random,time

pygame.init()

WIDTH=1000
HEIGHT=768
TITLE="RECYCLE RUN"

running=True
go=False
screen=pygame.display.set_mode((WIDTH,HEIGHT))
score=0
font=pygame.font.SysFont("TimesNewRoman",25)
total_rc=36
time_up=False
time_left=300
lives_left=4
start_time=time_now=pygame.time.get_ticks()
total_time=0


bg1=pygame.image.load("Background.png")
bg1=pygame.transform.scale(bg1,(1000,768))
bg2=pygame.image.load("box.png")
bg3=pygame.image.load("paperimg.png")
bg4=pygame.image.load("pencil.png")
bg5=pygame.image.load("plastic bag.png")
bg6=pygame.image.load("BINC.png")
bg6=pygame.transform.scale(bg6,(50,75))

class Recyclable(pygame.sprite.Sprite):
    def __init__(self,x,y,image):
        super().__init__()
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y


class Nonrecyclable(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=bg5
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y


class Bin(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=bg6
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def move(self,vx,vy):
      self.rect.x+=vx
      self.rect.y+=vy
      

images=[bg2,bg3,bg4]
rcs=pygame.sprite.Group()
nrcs=pygame.sprite.Group()
bingroup=pygame.sprite.Group()
for i in range(36):
    pi=random.choice(images)
    rc1=Recyclable(random.randint(50,950),random.randint(50,716),pi)
    rcs.add(rc1)
for i in range(25):
    nr1=Nonrecyclable(random.randint(50,950),random.randint(50,716))
    nrcs.add(nr1)
binchar=Bin(25,25)
bingroup.add(binchar)

def bincheck():
    global score,total_rc,lives_left
    for rc in rcs:
        if binchar.rect.colliderect(rc.rect):
            rc.kill()
            score=score+25
            total_rc=total_rc-1
    for nr in nrcs:
        if binchar.rect.colliderect(nr.rect):
            nr.kill()
            score=score-75
            lives_left=lives_left-1

while running==True: 
  current_time=pygame.time.get_ticks()
  total_time=current_time-start_time
  for event in pygame.event.get(): 
    if event.type==pygame.QUIT:
      running=False       
  time_left=time_left-1/60
  
  ks=pygame.key.get_pressed()
  if ks[pygame.K_w]:
      binchar.move(0,-2)
  if ks[pygame.K_s]:
      binchar.move(0,2)
  if ks[pygame.K_d]:
      binchar.move(2,0)
  if ks[pygame.K_a]:
      binchar.move(-2,0)
  if total_rc==0:
      running=False


  score_message=font.render("Score is: "+str(score),True,"black")
  time_message=font.render("Time left: "+str(round(300-total_time/1000,1)),True,"black")
  lives_message=font.render("Lives left is: "+str(lives_left),True,"black") 
  screen.blit(bg1,(0,0))
  screen.blit(time_message,(20,40))
  screen.blit(lives_message,(400,40))
  screen.blit(score_message,(800,40))  
  rcs.draw(screen)
  nrcs.draw(screen)
  bingroup.draw(screen)
  bincheck()
  if 300-total_time/1000<=0 or lives_left<=0:
      running=False
  pygame.display.update()   