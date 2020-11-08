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
    largura = 7
    comprimento = 7
    cor = (0,255,0) #RGB

class borda:
    x = 5
    y = 5
    largura = 5
    comprimento = 890
    cor = (255, 255, 255) #RGB

borda_cima = borda() #Borda
borda_baixo = borda() #Borda
borda_baixo.y = 590
borda_direita = borda() #Borda
borda_direita.x = 890
borda_direita.y = 5
borda_direita.largura = 590
borda_direita.comprimento = 5
borda_esquerda = borda() #Borda
borda_esquerda.x = 5
borda_esquerda.y = 5
borda_esquerda.largura = 590
borda_esquerda.comprimento = 5

pygame.init()
tela = pygame.display.set_mode((900,600)) #Resolução da janela
pygame.display.set_caption("Projeto P1 // Snake") #Nome da janela
pygame.mouse.set_visible(0) #Visibilidade do mouse

aberto = True
while aberto:
    pygame.time.delay(100)

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
    
    tela.fill((0, 0, 0))
    pygame.draw.rect(tela, snake.cor, (snake.x_atual , snake.y_atual, snake.comprimento, snake.largura)) #Cobra
    pygame.draw.rect(tela, comida.cor,(comida.x, comida.y, comida.comprimento, comida.largura)) #Comida
    pygame.draw.rect(tela, borda.cor, (borda_cima.x, borda_cima.y, borda_cima.comprimento, borda_cima.largura)) #Bordas
    pygame.draw.rect(tela, borda.cor, (borda_baixo.x, borda_baixo.y, borda_baixo.comprimento, borda_baixo.largura))
    pygame.draw.rect(tela, borda.cor, (borda_esquerda.x, borda_esquerda.y, borda_esquerda.comprimento, borda_esquerda.largura))
    pygame.draw.rect(tela, borda.cor, (borda_direita.x, borda_direita.y, borda_direita.comprimento, borda_direita.largura))
    pygame.display.update()

pygame.quit()
