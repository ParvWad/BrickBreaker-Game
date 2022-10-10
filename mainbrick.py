import pygame
import random


BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
GOLD=(212,175,55)
PINK=(255,192,203)
ORANGE=(255, 165, 0)    
BROWN=(165,42,42)
pygame.init()
font = pygame.font.Font(None,50)

screen_width= 1000
screen_height= 500
screen=screen = pygame.display.set_mode([screen_width,screen_height])

random_x=random.randint(-5,5)
random_y=random.randint(2,5)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image=pygame.Surface([60,20])
        self.image.fill(RED)

        self.rect=self.image.get_rect()
        self.rect.x = 50
        self.rect.y=400
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x-=5
        if keys[pygame.K_d]:
            self.rect.x+=5
        if self.rect.x<0:
            self.rect.x=0
        if self.rect.x>440:
            self.rect.x=439
            
class Player2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([60,20])
        self.image.fill(BLUE)

        self.rect=self.image.get_rect()
        self.rect.x = 650
        self.rect.y=400
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x-=5
        if keys[pygame.K_RIGHT]:
            self.rect.x+=5
        if self.rect.x>980:
            self.rect.x=980
        if self.rect.x<520:
            self.rect.x=520
      

class Ball1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.score=0
        self.life=3
        self.image=pygame.image.load("ball.png")
        self.image=pygame.transform.scale(self.image,[40,40])
        self.random_x=random.randint(-5,5)
        self.random_y=random.randint(2,5)
        self.rect=self.image.get_rect()
        self.rect.x=150 
        self.rect.y=200
    def update(self):
        self.rect.x+=self.random_x
        self.rect.y+=self.random_y
        if self.rect.y<10:
            self.random_y=self.random_y*-1
        if self.rect.y>450:
            self.rect.x=150
            self.rect.y=200
            self.random_x=random.randint(-5,5)
            self.random_y=random.randint(2,5)
            self.life-=1
        if self.rect.x<10:
            self.random_x=random.randint(1,5)
            self.random_y=random.randint(-5,5)
        if self.rect.x>450:
            self.random_x=random.randint(1,5)
            self.random_y=random.randint(-5,5)
            self.random_x=self.random_x*-1
            self.random_y=self.random_y*-1
        if pygame.sprite.spritecollide(self,player1_list,False):
            self.random_x=random.randint(-5,5)
            self.random_y=random.randint(1,5)
            self.random_x=self.random_x*-1
            self.random_y=self.random_y*-1
        if pygame.sprite.spritecollide(self,brick_list,True):
            self.random_y+=-1
            self.random_x=self.random_x*-1
            self.random_x=self.random_y*-1
            self.random_y=self.random_y*-1
            self.score+=1
        if pygame.sprite.spritecollide(self,brick_list1,True):
            self.random_y+=-1
            self.random_x=self.random_x*-1
            self.random_x=self.random_y*-1
            self.random_y=self.random_y*-1
            self.score+=1
        if self.random_y == 0:
            self.random_y=random.randint(-5,5)
        if self.random_x==0:
            self.random_x=random.randint(-5,5)

class Ball2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.score=0
        self.life=3
        self.image=pygame.image.load("ball.png")
        self.image=pygame.transform.scale(self.image,[40,40])
        self.random_x=random.randint(-5,5)
        self.random_y=random.randint(2,5)
        self.rect=self.image.get_rect()
        self.rect.x=650 
        self.rect.y=200
    def update(self):
        self.rect.x+=self.random_x
        self.rect.y+=self.random_y
        if self.rect.y<10:
            self.random_y=self.random_y*-1
        if self.rect.y>450:
            self.rect.x=650
            self.rect.y=200
            self.random_x=random.randint(-5,5)
            self.random_y=random.randint(2,5)
            self.life-=1
        if self.rect.x<520:
            self.random_x=random.randint(1,5)
            self.random_y=random.randint(-5,5)
        if self.rect.x>960:
            self.random_x=random.randint(1,5)
            self.random_y=random.randint(-5,5)
            self.random_x=self.random_x*-1
            self.random_y=self.random_y*-1
        if pygame.sprite.spritecollide(self,player2_list,False):
            self.random_x=random.randint(-5,5)
            self.random_y=random.randint(1,5)
            self.random_x=self.random_x*-1
            self.random_y=self.random_y*-1
        if pygame.sprite.spritecollide(self,brick_list,True):
            self.random_y+=-1
            self.random_x=self.random_x*-1
            self.random_x=self.random_y*-1
            self.random_y=self.random_y*-1
            self.score+=1
        if pygame.sprite.spritecollide(self,brick_list1,True):
            self.random_y+=-1
            self.random_x=self.random_x*-1
            self.random_x=self.random_y*-1
            self.random_y=self.random_y*-1
            self.score+=1
        if self.random_y == 0:
            self.random_y=random.randint(-5,5)
        if self.random_x==0:
            self.random_x=random.randint(-5,5)

class boundry(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([20,500])
        self.image.fill(GOLD)
        
        self.rect=self.image.get_rect()
        self.rect.x=500
        self.rect.y=10
class Brick(pygame.sprite.Sprite):
    def __init__(self,colour,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([60,20])
        self.image.fill(colour)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def update(self):
        if level_one == False and level_two == True:
            all_sprites_list.remove(b1)
            all_sprites_list.remove(b2)
            all_sprites_list.remove(b3)
            all_sprites_list.remove(b4)
            all_sprites_list.remove(b5)
            all_sprites_list.remove(b6)
            all_sprites_list.remove(b7)
            all_sprites_list.remove(bb1)
            all_sprites_list.remove(bb2)
            all_sprites_list.remove(bb3)
            all_sprites_list.remove(bb4)
            all_sprites_list.remove(bb5)
            all_sprites_list.remove(bb6)
            all_sprites_list.remove(bb7)
        
        
    

all_sprites_list=pygame.sprite.Group()
boundry_list=pygame.sprite.Group()
ball1_list=pygame.sprite.Group()
ball2_list=pygame.sprite.Group()
brick_list=pygame.sprite.Group()
player1_list=pygame.sprite.Group()
player2_list=pygame.sprite.Group()
brick_list1=pygame.sprite.Group()
brick_list2=pygame.sprite.Group()
ball3_list=pygame.sprite.Group()

b1 = Brick(ORANGE,75,50)
all_sprites_list.add(b1)
brick_list.add(b1)

b2 = Brick(GREEN,125,100)
all_sprites_list.add(b2)
brick_list.add(b2)

b3 = Brick(PINK,175,50)
all_sprites_list.add(b3)
brick_list.add(b3)

b4 = Brick(BROWN,225,100)
all_sprites_list.add(b4)
brick_list.add(b4)

b5 = Brick(GOLD,275,50)
all_sprites_list.add(b5)
brick_list.add(b5)

b6 = Brick(ORANGE,325,100)
all_sprites_list.add(b6)
brick_list.add(b6)

b7 = Brick(BROWN,375,50)
all_sprites_list.add(b7)
brick_list.add(b7)

#bricks for second player
bb1 = Brick(ORANGE,575,50)
all_sprites_list.add(bb1)
brick_list.add(bb1)

bb2 = Brick(GREEN,625,100)
all_sprites_list.add(bb2)
brick_list.add(bb2)

bb3 = Brick(PINK,675,50)
all_sprites_list.add(bb3)
brick_list.add(bb3)

bb4 = Brick(BROWN,725,100)
all_sprites_list.add(bb4)
brick_list.add(bb4)

bb5 = Brick(GOLD,775,50)
all_sprites_list.add(bb5)
brick_list.add(bb5)

bb6 = Brick(ORANGE,825,100)
all_sprites_list.add(bb6)
brick_list.add(bb6)

bb7 = Brick(BROWN,875,50)
all_sprites_list.add(bb7)
brick_list.add(bb7)



bound=boundry()
all_sprites_list.add(bound)
boundry_list.add(bound)

player=Player()
all_sprites_list.add(player)
player1_list.add(player)

player2=Player2()
all_sprites_list.add(player2)
player2_list.add(player2)

bal1=Ball1()
all_sprites_list.add(bal1)
ball1_list.add(bal1)

bal2=Ball2()
all_sprites_list.add(bal2)
ball2_list.add(bal2)

done = False
clock = pygame.time.Clock()
font = pygame.font.Font(None,36)
level_one=True
level_two=False
while not done and level_one:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(BLACK)
    all_sprites_list.update()
    text = font.render("Lives: " + str(bal1.life), True, WHITE)
    screen.blit(text,[10,80])
    all_sprites_list.draw(screen)
    Score=font.render("Score:"+str(bal1.score),True,WHITE)
    screen.blit(Score,[10,150])

    text = font.render("Lives: " + str(bal2.life), True, WHITE)
    screen.blit(text,[520,80])
    all_sprites_list.draw(screen)
    Score=font.render("Score:"+str(bal2.score),True,WHITE)
    screen.blit(Score,[520,150])

    if bal1.score ==7 or bal2.score == 7 or bal1.life ==0 or bal2.life ==0:
        level_one = False
        level_two = True
                    
    pygame.display.flip()
    clock.tick(60)
if bal1.score>bal2.score or bal2.life==0:
    bal3=Ball1()
    all_sprites_list.add(bal3)
    ball1_list.add(bal3)
elif bal2.score>bal1.score or bal1.life==0:
    bal4=Ball2()
    all_sprites_list.add(bal4)
    ball2_list.add(bal4)
bal1.life=3
bal1.score=0
bal2.life=3
bal2.score=0

pygame.sprite.Group.remove(brick_list)
all_sprites_list.remove(b1)
all_sprites_list.remove(b2)
all_sprites_list.remove(b3)
all_sprites_list.remove(b4)
all_sprites_list.remove(b5)
all_sprites_list.remove(b6)
all_sprites_list.remove(b7)
all_sprites_list.remove(bb1)
all_sprites_list.remove(bb2)
all_sprites_list.remove(bb3)
all_sprites_list.remove(bb4)
all_sprites_list.remove(bb5)
all_sprites_list.remove(bb6)
all_sprites_list.remove(bb7)


b8 = Brick(ORANGE,75,50)
all_sprites_list.add(b8)
brick_list1.add(b8)

b9 = Brick(GREEN,125,100)
all_sprites_list.add(b9)
brick_list1.add(b9)

b10 = Brick(PINK,175,50)
all_sprites_list.add(b10)
brick_list1.add(b10)

b11 = Brick(BROWN,225,100)
all_sprites_list.add(b11)
brick_list1.add(b11)

b12 = Brick(GOLD,275,50)
all_sprites_list.add(b12)
brick_list1.add(b12)

b13 = Brick(ORANGE,325,100)
all_sprites_list.add(b13)
brick_list1.add(b13)

b14 = Brick(BROWN,375,50)
all_sprites_list.add(b14)
brick_list1.add(b14)

#bricks for second player
bb8 = Brick(ORANGE,575,50)
all_sprites_list.add(bb8)
brick_list1.add(bb8)

bb9 = Brick(GREEN,625,100)
all_sprites_list.add(bb9)
brick_list1.add(bb9)

bb10 = Brick(PINK,675,50)
all_sprites_list.add(bb10)
brick_list1.add(bb10)

bb11 = Brick(BROWN,725,100)
all_sprites_list.add(bb11)
brick_list1.add(bb11)

bb12 = Brick(GOLD,775,50)
all_sprites_list.add(bb12)
brick_list1.add(bb12)

bb13 = Brick(ORANGE,825,100)
all_sprites_list.add(bb13)
brick_list1.add(bb13)

bb14  = Brick(BROWN,875,50)
all_sprites_list.add(bb14)
brick_list1.add(bb14)

  


while not done and level_two:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill(BLACK)
    all_sprites_list.update()
    text = font.render("Lives: " + str(bal1.life), True, WHITE)
    screen.blit(text,[10,80])
    all_sprites_list.draw(screen)
    Score=font.render("Score:"+str(bal1.score),True,WHITE)
    screen.blit(Score,[10,150])

    text = font.render("Lives: " + str(bal2.life), True, WHITE)
    screen.blit(text,[520,80])
    all_sprites_list.draw(screen)
    Score=font.render("Score:"+str(bal2.score),True,WHITE)
    screen.blit(Score,[520,150])

    if bal1.score ==7 or bal2.score == 7 or bal1.life ==0 or bal2.life ==0:
        level_two = False
        level_three = True
                    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()


