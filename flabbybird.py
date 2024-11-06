import pygame, sys
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((800, 900))
background = pygame.image.load('background.png')
ground = pygame.image.load('groundpicture.png')
screen.blit(background,(0,0))

x = 0


class Bird(pygame.sprite.Sprite):#Bird is child class, sprite class is the parent class which is a template.
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.birdimages = []
        self.pictures = 0

        for i in range(1,4):
    
            self.birdimages.append(pygame.image.load('bird'+str(i)+'.png'))
        self.image = self.birdimages[self.pictures]
        self.rect = self.image.get_rect()
        self.delay = 0
        self.rect.center = x,y
    def update(self):
        self.delay = self.delay+1
        if self.delay>5:
            self.delay = 0
            self.pictures = self.pictures+1

            if self.pictures == 3:
                self.pictures = 0
            self.image = self.birdimages[self.pictures]
        
        

        
birdgroup = pygame.sprite.Group()
bird = Bird(25,450)
birdgroup.add(bird)#now bird should have the properties of birgroups


pygame.display.set_caption('Hello World!')



clock = pygame.time.Clock()
while True:
    screen.blit(ground,(x,700))
    clock.tick(60)
    x=x-1
    if abs(x) >35:
        x = 0
    birdgroup.draw(screen)
    birdgroup.update()


    for event in pygame.event.get():
       if event.type == QUIT:
           pygame.quit()
           sys.exit()
    pygame.display.update()
