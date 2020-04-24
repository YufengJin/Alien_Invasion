import pygame
from pygame.sprite import Group

class Ship():
    def __init__(self, screen):
        
        self.screen = screen

        self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.scale(self.image,(16,32))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # moving Flag, continue moving when it comes to True
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.moving_speed = 1

    def update(self):
        #防止飞机飞出边界
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.moving_speed
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= self.moving_speed
        elif self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.bottom -= self.moving_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.bottom += self.moving_speed

    def blitme(self):
        #draw the ship at bottom of screen
        #blit: draw one image onto another
        self.screen.blit(self.image,self.rect)
