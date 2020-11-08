#================7/11
#Eu vou precisar modificar a movimentação
#para quando a cobra for se mover verticalmente, exemplo:
#if event.type == KEYDOWN and event.key == K_w:
#   if last_key == "a" or last_key == "d"

#Também preciso implementar colisões, pontuação, crescimento após comer, aceleração ao longo do tempo

#================8/11
#Eu implementei colisões para a cobra parar caso bata na parede, mas pq? Ela vai morrer de qlqr forma...
#Eu preciso entender melhor POO para criar um modo de dois jogadores no futuro, melhor estudar logo isso para não ter de
#refazer todo o código depois...  >>> FEITO
#Se a cobra tocar na comida(a hitbox não está perfeita) a comida troca de lugar e são somados 10 pontos(que eu ainda não sei como exibir no jogo)

import pygame
import random

pygame.init()

pontos = 0

class snake:  #Aqui eu preciso aprender como usar o __init__ para criar o modo multiplayer
    def __init__(self, cor): 
        self.start_x = random.randrange(50,850)
        self.start_y = random.randrange(50,550)
        self.vel = 5
        self.comprimento = 17
        self.largura = 7
        self.cor = cor #RGB
        self.x_atual = self.start_x
        self.y_atual = self.start_y


snake1 = snake((255, 0, 0))
snake2 = snake((200, 0, 200)) #isso deve ser usado quando o sonho de um multiplayer for real


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

last_key = None  #Uma ideia para consertar a movimentação
aberto = True
while aberto:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Fechar janela
            aberto = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_w and snake1.y_atual>15: #Movimentação
            snake1.y_atual -= snake1.vel
            last_key = "w"
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_a and snake1.x_atual>15: #
            snake1.x_atual -= snake1.vel
            last_key = "a"
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s and snake1.y_atual<580: #
            snake1.y_atual += snake1.vel
            last_key = "s"
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_d and snake1.x_atual<870: #
            snake1.x_atual += snake1.vel
            last_key = "d"

    tela.fill((0, 0, 0))
    pygame.draw.rect(tela, snake1.cor, (snake1.x_atual , snake1.y_atual, snake1.comprimento, snake1.largura)) #Cobra
    pygame.draw.rect(tela, comida.cor,(comida.x, comida.y, comida.comprimento, comida.largura)) #Comida
    if abs(comida.x-snake1.x_atual)<=snake1.vel and abs(comida.y-snake1.y_atual)<=snake1.vel:
        comida.x = random.randrange(20, 880)
        comida.y = random.randrange(20, 580)
        pontos += 10
    pygame.draw.rect(tela, borda.cor, (borda_cima.x, borda_cima.y, borda_cima.comprimento, borda_cima.largura)) #Bordas
    pygame.draw.rect(tela, borda.cor, (borda_baixo.x, borda_baixo.y, borda_baixo.comprimento, borda_baixo.largura))
    pygame.draw.rect(tela, borda.cor, (borda_esquerda.x, borda_esquerda.y, borda_esquerda.comprimento, borda_esquerda.largura))
    pygame.draw.rect(tela, borda.cor, (borda_direita.x, borda_direita.y, borda_direita.comprimento, borda_direita.largura))
    pygame.display.update()

pygame.quit()
print(pontos)
