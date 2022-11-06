import pygame
import sys
from menu import Menu
from configuracao import Config

pygame.init()

janela_menu = Menu()
janela_config = Config()

while True:
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    if not janela_menu.menu_ativo:
        if janela_config.config_ativo:
            janela_config.desenhar_janela()
    else:
        janela_menu.update()


    #Atualizar o jogo
    pygame.display.update()
