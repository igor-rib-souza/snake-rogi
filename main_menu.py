from survival import survival
from singleplayer import singleplayer
import sys
import pygame

pygame.init()
pygame.display.set_caption("Snake")
tela = pygame.display.set_mode((900, 600))
font2 = pygame.font.Font("freesansbold.ttf", 20)
font = pygame.font.Font('freesansbold.ttf', 32) 
text = font.render('Snake, the Game', True, (255,255,255), (0,0,0)) 
single = font2.render("Singleplayer",True,(200,0,200),(0,0,0))
survive = font2.render("Survival mode",True,(0,200,200),(0,0,0))

def menu():
    while True:
        pygame.mouse.set_visible(1)

        tela.blit(text,(340,40)) 
        
        tela.blit(single,(340,250))

        tela.blit(survive,(340,300))



        ("Snake main menu", font, (255, 255, 255), tela, 450, 30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if pos[0] in range(340,465) and pos[1] in range(250,265):
                    singleplayer()
                elif pos[0] in range(340, 480) and pos[1] in range(300, 315):
                    survival()
        

        pygame.display.update()

menu()
