import pygame
import random

pygame.init()

class snake:
    start_x = random.randrange(50.850)
    start_y = random.randrange(50,550)
    vel = 5
    comprimento = 17
    largura = 7
    cor = (255,0,0)

class comida:
    x = random.randrange(20,880)
    y = random.randrange(20,580)
    largura = 5
    comprimento = 5
    cor = (0,0,255)


