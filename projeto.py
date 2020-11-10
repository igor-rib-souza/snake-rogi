import pygame
import random

pygame.init()

pontos = 0

class snake:  #Aqui eu preciso aprender como usar o __init__ para criar o modo multiplayer
    def __init__(self, cor): 
        self.x = random.randrange(50,850)
        self.y = random.randrange(50,550)
        self.vel = 5
        self.comprimento = 16
        self.largura = 8
        self.cor = cor #RGB
        self.pre_x = self.x
        self.pre_y = self.y
        self.size = 1

snake1 = snake((255, 0, 0))
snake2 = snake((200, 0, 180)) #isso deve ser usado quando o sonho de um multiplayer for real


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
previous_key = last_key
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
            previous_key = last_key
            last_key = "w"
            temp = snake1.comprimento
            snake1.comprimento = snake1.largura
            snake1.largura = temp

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_a and not last_key  in ["d", "a"]: #
            previous_key = last_key
            last_key = "a" 
            temp = snake1.comprimento
            snake1.comprimento = snake1.largura
            snake1.largura = temp

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s and not last_key in ["w", "s"]: #
            previous_key = last_key
            last_key = "s" 
            temp = snake1.comprimento
            snake1.comprimento = snake1.largura
            snake1.largura = temp

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_d and not last_key in ["a", "d"]: #
            previous_key = last_key
            last_key = "d" 
            temp = snake1.comprimento
            snake1.comprimento = snake1.largura
            snake1.largura = temp

    
    #Aqui começa a movimentação, por algum erro que eu **AINDA** não identifiquei o respawn da parte de cima não esta funcionando
    if last_key == "w":
        if snake1.y>15:
            snake1.pre_y = snake1.y
            snake1.y -= snake1.vel
        else:
            snake1.x = random.randrange(20,880)
            snake1.y = random.randrange(20,580)
            pontos -= 50
            snake1.size = 1
    elif last_key == "a":
        if snake1.x>15:
            snake1.pre_x = snake1.x
            snake1.x -= snake1.vel
        else:
            snake1.x = random.randrange(20,880)
            snake1.y = random.randrange(20,580)
            pontos -=50
            snake1.size = 1
    elif last_key == "s":
        if snake1.y<580:
            snake1.pre_y = snake1.y
            snake1.y += snake1.vel
        else:
            snake1.x = random.randrange(20,880)
            snake1.y = random.randrange(20,580)
            pontos -=50
            snake1.size = 1
    elif last_key == "d":
        if snake1.x<870:
            snake1.pre_x = snake1. x
            snake1.x += snake1.vel
        else:
            snake1.x = random.randrange(20,880)
            snake1.y = random.randrange(20,580)
            pontos -= 50
            snake1.size = 1
    
    tela.fill((0, 0, 0))
    pygame.draw.rect(tela, comida.cor,(comida.x, comida.y, comida.comprimento, comida.largura)) #Comida
    if abs(comida.x-snake1.x)<=snake1.vel and abs(comida.y-snake1.y)<=snake1.vel:
        comida.x = random.randrange(25, 880)
        comida.y = random.randrange(25, 580)
        pontos += 10
        snake1.size += 1
    pygame.draw.rect(tela, snake1.cor, (snake1.x , snake1.y, snake1.comprimento, snake1.largura)) #Cobra
    if snake1.size>1:
        for i in range(snake1.size-1):
            if last_key in ["w", "s"] and previous_key in ["w", "s"]:   #MOVIMENTAÇÃO SEM CURVA   #OK
                if last_key == "w":
                    pygame.draw.rect(tela, snake1.cor, (snake1.x, snake1.y+(i+1)*2*snake1.vel, snake1.comprimento, snake1.largura))
                else:
                    pygame.draw.rect(tela, snake1.cor, (snake1.x, snake1.y-(i+1)*2*snake1.vel, snake1.comprimento, snake1.largura))
            elif last_key in ["a", "d"] and previous_key in ["a", "d"]:  #OK
                if last_key == "a":
                    pygame.draw.rect(tela, snake1.cor, (snake1.x+(i+1)*2*snake1.vel, snake1.y, snake1.comprimento, snake1.largura))
                elif last_key =="d":
                    pygame.draw.rect(tela, snake1.cor, (snake1.x-(i+1)*2*snake1.vel, snake1.y, snake1.comprimento, snake1.largura))
             


            else:      #MOVIMENTAÇÃO COM CURVA
                temp = snake1.comprimento
                snake1.comprimento = snake1.largura
                snake1.largura = temp
                if last_key == "w" and previous_key == "a":
                    pygame.draw.rect(tela, snake1.cor, (snake1.x+(i)*snake1.largura, snake1.y+snake1.comprimento, snake1.comprimento, snake1.largura))  #ok

                elif last_key == "w" and previous_key == "d":
                    pygame.draw.rect(tela, snake1.cor, (snake1.x-(i+1)*snake1.largura, snake1.y+snake1.comprimento, snake1.comprimento, snake1.largura))  #OK
                elif last_key == "s" and previous_key == "a":
                    pygame.draw.rect(tela, snake1.cor, (snake1.x+i*snake1.largura, snake1.y-snake1.comprimento/2, snake1.comprimento, snake1.largura)) #OK
                elif last_key == "s" and previous_key == "d":
                    pygame.draw.rect(tela, snake1.cor, (snake1.x-(i+1)*snake1.largura, snake1.y-snake1.comprimento/2, snake1.comprimento, snake1.largura)) #OK
                elif last_key == "a" and previous_key == "w":
                    pygame.draw.rect(tela, snake1. cor, (snake1.x+1*snake1.largura, snake1.y+(i)*snake1.comprimento, snake1.comprimento, snake1.largura)) #OK
                elif last_key == "a" and previous_key == "s":
                    pygame.draw.rect(tela, snake1. cor, (snake1.x+1*snake1.largura, snake1.y-(i+1)*snake1.comprimento, snake1.comprimento, snake1.largura)) #OK
                elif last_key == "d" and previous_key == "w":
                    pygame.draw.rect(tela, snake1. cor, (snake1.x-snake1.comprimento, snake1.y+(i)*snake1.comprimento, snake1.comprimento, snake1.largura))
                
                elif last_key == "d" and previous_key == "s":
                    pygame.draw.rect(tela, snake1. cor, (snake1.x-snake1.comprimento, snake1.y-(i+1)*snake1.comprimento, snake1.comprimento, snake1.largura)) #OK

                if snake1.size>2:
                snake1.largura = snake1.comprimento
                snake1.comprimento = temp
                 

    pygame.draw.rect(tela, borda_cima.cor, (borda_cima.x, borda_cima.y, borda_cima.comprimento, borda_cima.largura)) #Bordas
    pygame.draw.rect(tela, borda_baixo.cor, (borda_baixo.x, borda_baixo.y, borda_baixo.comprimento, borda_baixo.largura))
    pygame.draw.rect(tela, borda_esquerda.cor, (borda_esquerda.x, borda_esquerda.y, borda_esquerda.comprimento, borda_esquerda.largura))
    pygame.draw.rect(tela, borda_direita.cor, (borda_direita.x, borda_direita.y, borda_direita.comprimento, borda_direita.largura))
    pygame.display.update()
    previous_key = last_key

pygame.quit()
print(f"VOCÊ FEZ {pontos} PONTOS !!!")
