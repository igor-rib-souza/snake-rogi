import pygame
import random

pygame.init()

class snake:
    start_x = random.randrange(50,850)
    start_y = random.randrange(50,550)
    vel = 5
    comprimento = 17
    largura = 7
    cor = (255,0,0) #RGB
    x_atual = start_x
    y_atual = start_y

class comida:
    x = random.randrange(20,880)
    y = random.randrange(20,580)
    largura = 5
    comprimento = 5
    cor = (0,0,255) #RGB


pygame.init()
tela = pygame.display.set_mode((900,600)) #Resolução da janela
pygame.display.set_caption("Projeto P1 // Snake")
pygame.mouse.set_visible(0)

aberto = True
while aberto:
    pygame.time.delay(100)
    pygame.draw.rect(tela, snake.cor, (snake.x_atual , snake.y_atual, snake.comprimento, snake.largura))

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Fechar janela
            aberto = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_w: #Movimentação
            snake.y_atual -= snake.vel

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            snake.x_atual -= snake.vel

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            snake.y_atual += snake.vel

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            snake.x_atual += snake.vel
    pygame.display.update()

pygame.quit()
