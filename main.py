import pygame
from  pygame.sprite import Sprite
import sys
import numpy as np

val = 150
grey = val,val,val

class Square(Sprite):

    def __init__(self, SCREEN, border_colour=grey,center_colour=grey,*groups):
        super().__init__(*groups)
        # super().__init__(self)
        self.SCREEN = SCREEN
        self.length = 100
        self.width = self.length
        self.height = self.width
        self.image = pygame.Surface([self.width , self.height])
        self.image.fill(border_colour)
        self.rect = self.image.get_rect()

        self.border_size = 20
        self.middleBlock = pygame.Surface([int(self.width-self.border_size), int(self.height-self.border_size)])
        self.middleBlock.fill(center_colour)
        self.middleBlockRect = self.middleBlock.get_rect()
        self.middleBlockRect.centerx = self.rect.centerx
        self.middleBlockRect.centery = self.rect.centery

        self.image.blit(self.middleBlock, self.middleBlockRect)

    
    def update(self, x,y):
        # return super().update(*args)
        # self.rect.x = int(x)
        # self.rect.y = int(y)
        self.rect.centerx = int(x)
        self.rect.centery = int(y)
    
    def draw(self):
        self.SCREEN.blit(self.image, self.rect)


class White(Square):

    def __init__(self, SCREEN, *groups):
        border_colour=(255,255,255)
        center_colour=255,255,0
        super().__init__(SCREEN, border_colour=border_colour, center_colour=center_colour, *groups)


class Black(Square):
    def __init__(self, SCREEN,*groups):
        border_colour=(0,0,0)
        center_colour=255,255,0
        super().__init__(SCREEN, border_colour=border_colour, center_colour=center_colour, *groups)
def exit():
    pygame.quit()
    sys.exit()   


class Circle():

    def __init__(self, number, radius):
        super().__init__()
        self.N = number
        self.r = radius
        self.coords = []
        self.calc()

    def calc(self):
        delta_theta = float(2*np.pi/self.N)
        theta = float(0)
        colour = True
        for i in range(0, self.N):
            x = self.r*np.cos(theta)
            y = self.r*np.sin(theta)
            element = []
            element.append(x)
            element.append(y)
            element.append(colour)
            self.coords.append(element)
            colour = not colour
            theta += delta_theta
            print(element)
        


if __name__ == '__main__':
    pygame.init()
    width, height = 500,500
    size = width, height
    # val = 150
    # grey = val,val,val
    SCREEN = pygame.display.set_mode(size)

    # sq = Square(SCREEN)
    # wh = White(SCREEN)
    bl = Black(SCREEN)

    cir = Circle(16, 5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    exit()

        SCREEN.fill(grey)          
        # bl.update(width/2, height/2)
        # bl.draw()
        # pygame.draw.rect(SCREEN, (255,0,0), sq.rect)
        pygame.display.flip() 

    