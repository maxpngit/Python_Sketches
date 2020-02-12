# -*- coding: utf-8 -*-

import pygame

BROWN = (150, 75, 0)
WHITE = (255, 255, 255)

paddlew = 200
paddleh = 25
paddlex = 300
paddley = 550

scores = 0
lives = 5

picx = 0
picy = 0

picw = 100
pich = 100

speedx = 5
speedy = 5

pygame.init()

screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption("Pong")
font = pygame.font.SysFont("Arial", 24)
pygame.mouse.set_visible(False)

pic = pygame.image.load("ball.png")
bg = pygame.image.load("wall.png")
colorkey = pic.get_at((0,0))
pic.set_colorkey (colorkey)

pygame.mixer.init()
pong = pygame.mixer.Sound("pong.wav")
fault = pygame.mixer.Sound("fault.wav")

clock = pygame.time.Clock ()

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                scores = 0
                lives = 5
                picx = 0
                picy = 0
                speedx = 5
                speedy = 5
                pygame.mouse.set_visible(False)

    picx += speedx
    picy += speedy

    if picx <= 0 or picx >= 700:
        speedx = -speedx * 1.1
        if speedx > 12:
            speedx = 12
    if picy <= 0:
        speedy = -speedy + 1
        if speedy > 12:
            speedy = 12
    if picy >=500:
        fault.play()
        lives -= 1
        speedy = -5
        speedx = 5
        picy = 499

    screen.blit(bg, (0, 0))
    screen.blit(pic, (picx, picy))

    if lives >= 1:
        paddlex = pygame.mouse.get_pos()[0]
        paddlex -= paddlew/2
        pygame.draw.rect(screen, BROWN, (paddlex, paddley, paddlew, paddleh))

    if picy + pich >= paddley and picy + pich <= paddley + paddleh and speedy > 0:
        if picx + picw/2 >= paddlex and picx + picw/2 <= paddlex + paddlew:
            speedy = -speedy
            pong.play()
            scores += 1
        
    draw_string = "Попытки: " + str(lives) + "    Очки: " + str(scores)

    if lives < 1:
        speedx = speedy = 0
        draw_string = "Игра закончена! Ваши очки: " + str(scores) + "!"
        draw_string += " Нажмите F1, чтобы сыграть еще раз!"
        pygame.mouse.set_visible(True)

    text = font.render(draw_string, True, BROWN)
    text_rect = text.get_rect()
    text_rect.centerx = screen.get_rect().centerx
    text_rect.y = 10
    pygame.draw.rect(screen, WHITE, (10, 10, 780, 30))
    screen.blit(text, text_rect)

    pygame.display.update()
    clock.tick(60)
            
pygame.quit()
        
