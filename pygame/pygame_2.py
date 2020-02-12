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

bullets = [] # пустой список
lastDirect = "right" # последнее направление полета снаряда

isJump = False
JumpCount = 10

left = False
right = False
animCount = 0

Fs = 30 # частота кадров

#####создаем класс СНАРЯД#####
class missile():
    def __init__(self, x, y, radius, color, toward):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.toward = toward
        self.velocity = 8 * toward

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
########################

clock = pygame.time.Clock() # для частоты кадров clock.tick(Fs)

##### функция перерисовки окна win #####
def drawWindow():
    global animCount

    win.blit(bg, (0, 0))
    
    if animCount + 1 > Fs:
        animCount = 0

    if left:
        win.blit (walkLeft[animCount // 10], (x,y))
        animCount += 1
    elif right:
        win.blit (walkRight[animCount // 10], (x,y))
        animCount += 1
    else:
        win.blit (playerStand,(x,y))
        
    for bullet in bullets:
        bullet.draw(win)
        
    #pygame.draw.rect(win, (0,0,255), (x,y,width,height))
    pygame.display.update()
################################
    
while run:
    clock.tick(Fs) #задаем частоту кадров

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.velocity
        else:
            bullets.pop(bullets.index(bullet))
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_f]:
        if lastDirect == "right":
            toward = 1
        else:
            toward = -1
            
        if len(bullets) < 5:
            bullets.append(missile(round(x + width // 2), round(y + height // 2), 5, (255,0,0), toward))

    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False
        lastDirect = "left"
    elif keys[pygame.K_RIGHT] and x < 500 - width - 5:
        x += speed
        left = False
        right = True
        lastDirect = "right"
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
