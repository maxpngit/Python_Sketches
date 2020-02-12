# -*- coding: utf-8 -*-
"""
@author: Manvel Arutiunov
"""


import pygame

pygame.init() # стартовая инициализация

win = pygame.display.set_mode((500, 500)) # окно 500 х 500 для перерисовки

pygame.display.set_caption("Walking")

##### Подгружаем спрайты для анимации #####
walkRight = [pygame.image.load('anim/right1.png'),      
                   pygame.image.load('anim/right2.png'),      
                   pygame.image.load('anim/right3.png'),    
                   pygame.image.load('anim/right4.png')]    
                                                                          
walkLeft = [pygame.image.load('anim/left1.png'),     
                 pygame.image.load('anim/left2.png'),     
                 pygame.image.load('anim/left3.png'),
                 pygame.image.load('anim/left4.png')]

playerStand = pygame.image.load('anim/stand.png')
bg = pygame.image.load('anim/bg.png')
##################################

x = 100 # стартовая
y = 325 # позиция
width = 100 # ширина картинки спрайта
height = 175 # высота картинки спрайта
speed = 5 # приращение координат X или Y (косвенно - скорость)

run = True # для вечного цикла и выхода из него

isJump = False
JumpCount = 10

left = False
right = False
animCount = 0

Fs = 24 # частота кадров

clock = pygame.time.Clock() # для частоты кадров clock.tick(Fs)

##### функция перерисовки окна win #####
def drawWindow():
    global animCount

    win.blit(bg, (0, 0))
    
    if animCount + 1 > Fs:
        animCount = 0

    if left:
        win.blit (walkLeft[animCount // 8], (x,y))
        animCount += 1
    elif right:
        win.blit (walkRight[animCount // 8], (x,y))
        animCount += 1
    else:
        win.blit (playerStand,(x,y))
        
    
    #pygame.draw.rect(win, (0,0,255), (x,y,width,height))
    pygame.display.update()
################################
    
while run:
    clock.tick(Fs) #задаем частоту кадров

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 500 - width - 5:
        x += speed
        left = False
        right = True
    else:
        left = False
        right = False
        animCount = 0
    if not isJump:
        """
        if keys[pygame.K_UP] and y > 5:
            y -= speed
        if keys[pygame.K_DOWN] and y < 500 - height - 5:
            y += speed
        """    
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if JumpCount >= -10:
            if JumpCount < 0:
                y += (JumpCount ** 2)/2
            else:
                y -= (JumpCount ** 2)/2
            JumpCount -= 1
        else:
            isJump = False
            JumpCount = 10

    drawWindow()

pygame.quit() 
