# -*- coding: utf-8 -*-
"""
@author: Manvel Arutiunov
"""

import pygame
import random

WHITE = (255, 255, 255)

pygame.init()

screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption("Crazy Balls")
mousedown = False

run = True

clock = pygame.time.Clock ()

pic = pygame.image.load("ball.png")
colorkey = pic.get_at((0,0))
pic.set_colorkey (colorkey)

sprite_list = pygame.sprite.Group()

class Ball (pygame.sprite.Sprite):
    pos = (0, 0)
    xvel = 1
    yvel = 1
    scale = 100

    def __init__(self, pos, xvel, yvel):
        pygame.sprite.Sprite.__init__(self)
        self.image = pic
        self.scale = random.randrange(50, 100)
        self.image = pygame.transform.scale(self.image, (self.scale, self.scale))
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.x = pos[0] - self.scale/2
        self.rect.y = pos[1] - self.scale/2
        self.xvel = xvel
        self.yvel = yvel

    def update(self):
        self.rect.x += self.xvel
        self.rect.y += self.yvel
        if self.rect.x <= 0 or self.rect.x > screen.get_width() - self.scale:
            self.xvel = -self.xvel
        if self.rect.y <= 0 or self.rect.y > screen.get_height() - self.scale:
            self.yvel = -self.yvel

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if event.type == pygame.MOUSEBUTTONDOWN:
        if pygame.mouse.get_pressed()[2]:
            mousedown = True
        elif pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            clicked_balls = [s for s in sprite_list if s.rect.collidepoint(pos)] #short form
            sprite_list.remove(clicked_balls)
    if event.type == pygame.MOUSEBUTTONUP:
        mousedown = False

    screen.fill (WHITE)
    sprite_list.update ()
    sprite_list.draw(screen)
    clock.tick(60)
    pygame.display.update()

    if mousedown:
        speedx = random.randint(-5, 5)
        speedy = random.randint(-5, 5)
        newBall = Ball(pygame.mouse.get_pos(), speedx, speedy)
        sprite_list.add(newBall)
        
pygame.quit()
        
