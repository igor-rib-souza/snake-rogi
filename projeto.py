"""================7/11
Eu vou precisar modificar a movimentação
para quando a cobra for se mover verticalmente, exemplo:
if event.type == KEYDOWN and event.key == K_w:
   if last_key == "a" or last_key == "d"

Também preciso implementar colisões, pontuação, crescimento após comer, aceleração ao longo do tempo

================8/11
Se a cobra tocar na comida(a hitbox não está perfeita) a comida troca de lugar e são somados 10 pontos(que eu ainda não sei como exibir no jogo)
se a cobra toca a parede ela nasce em outro ponto, preciso implementar a diminuição de pontos caso isso aconteça


================9/11
Eu preciso mudar todo o sistema de movimentação *para dentro de while's, para quando uma tecla for pressionada ele andar nql posição até 
outra tecla ser pressionada

Preciso modificar a movimentação para só mudar para direita/esquerda quando estiver subindo e descendo e vice-versa

Preciso APRENDER(ou descobrir...) como fazer a animação do movimento e como mostrar a pontuação in-game"""

import pygame
import random

pygame.init()

pontos = 0

class snake:  #Aqui eu preciso aprender como usar o __init__ para criar o modo multiplayer
    def __init__(self, cor): 
        self.x = random.randrange(50,850)
        self.y = random.randrange(50,550)
        self.vel = 5
        self.comprimento = 17
        self.largura = 7
        self.cor = cor #RGB

snake1 = snake((255, 0, 0))
snake2 = snake((200, 0, 200)) #isso deve ser usado quando o sonho de um multiplayer for real


class comida:
    x = random.randrange(20,880)
    y = random.randrange(20,580)
    largura = 7
    comprimento = 7
    cor = (0,255,0) #RGB

class borda:
    def __init__(self, x, y, largura, comprimento):
        self.x = x #5
        self.y = y #5
        self.largura = largura #5
        self.comprimento = comprimento #890
        self.cor = (255, 255, 255) #RGB

borda_cima = borda(5, 5, 5, 890) #Borda
borda_baixo = borda(5, 590, 5, 890) #Borda
borda_direita = borda(890, 5, 590, 5) #Borda
borda_esquerda = borda(5, 5, 590, 5) #Borda


pygame.init()
tela = pygame.display.set_mode((900,600)) #Resolução da janela
pygame.display.set_caption("Projeto P1 // Snake") #Nome da janela
pygame.mouse.set_visible(0) #Visibilidade do mouse


last_key = random.choice(["w", "a", "s", "d"])  #Uma ideia para consertar a movimentação
if last_key in ["w", "s"]:
    temp = snake1.comprimento
    snake1.comprimento = snake1.largura
    snake1.largura = temp

aberto = True
while aberto:
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Fechar janela
            aberto = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_w and not last_key in ["s","w"]: #Movimentação
            last_key = "w"
            temp = snake1.comprimento
            snake1.comprimento = snake1.largura
            snake1.largura = temp

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_a and not last_key  in ["d", "a"]: #
            last_key = "a" 
            temp = snake1.comprimento
            snake1.comprimento = snake1.largura
            snake1.largura = temp

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s and not last_key in ["w", "s"]: #
            last_key = "s" 
            temp = snake1.comprimento
            snake1.comprimento = snake1.largura
            snake1.largura = temp

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_d and not last_key in ["a", "d"]: #
            last_key = "d" 
            temp = snake1.comprimento
            snake1.comprimento = snake1.largura
            snake1.largura = temp

    
    #Aqui começa a movimentação, por algum erro que eu **AINDA** não identifiquei o respawn da parte de cima não esta funcionando
    if last_key == "w":
        if snake1.y>15:
            snake1.y -= snake1.vel
        else:
            snake1.x = random.randrange(20,880)
            snake1.y = random.randrange(20,580)
            pontos -= 50
    elif last_key == "a":
        if snake1.x>15:
            snake1.x -= snake1.vel
        else:
            snake1.x = random.randrange(20,880)
            snake1.y = random.randrange(20,580)
            pontos -=50
    elif last_key == "s":
        if snake1.y<580:
            snake1.y += snake1.vel
        else:
            snake1.x = random.randrange(20,880)
            snake1.y = random.randrange(20,580)
            pontos -=50
    elif last_key == "d":
        if snake1.x<870:
            snake1.x += snake1.vel
        else:
            snake1.x = random.randrange(20,880)
            snake1.y = random.randrange(20,580)
            pontos -= 50

    tela.fill((0, 0, 0))
    pygame.draw.rect(tela, comida.cor,(comida.x, comida.y, comida.comprimento, comida.largura)) #Comida
    if abs(comida.x-snake1.x)<=snake1.vel and abs(comida.y-snake1.y)<=snake1.vel:
        comida.x = random.randrange(25, 880)
        comida.y = random.randrange(25, 580)
        pontos += 10
    pygame.draw.rect(tela, snake1.cor, (snake1.x , snake1.y, snake1.comprimento, snake1.largura)) #Cobra
    pygame.draw.rect(tela, borda_cima.cor, (borda_cima.x, borda_cima.y, borda_cima.comprimento, borda_cima.largura)) #Bordas
    pygame.draw.rect(tela, borda_baixo.cor, (borda_baixo.x, borda_baixo.y, borda_baixo.comprimento, borda_baixo.largura))
    pygame.draw.rect(tela, borda_esquerda.cor, (borda_esquerda.x, borda_esquerda.y, borda_esquerda.comprimento, borda_esquerda.largura))
    pygame.draw.rect(tela, borda_direita.cor, (borda_direita.x, borda_direita.y, borda_direita.comprimento, borda_direita.largura))
    pygame.display.update()

pygame.quit()
print(f"VOCÊ FEZ {pontos} PONTOS !!!")
