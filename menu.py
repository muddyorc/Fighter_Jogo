import pygame
import sys

pygame.init()

#criar a Janela

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600


#Padrão da Fonte
fonts = pygame.font.get_fonts()
default_font = pygame.font.Font("funcao/Fontes/turok.ttf", 30)

class Menu():
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Menu")

        #Botões

        #Start
        self.button_start = pygame.image.load('funcao/Backgrounds/botao.png').convert_alpha()
        self.button_start = pygame.transform.rotozoom(self.button_start, 0, 0.6)
        self.button_start_rect = self.button_start.get_rect(center=(500, 300))

        #Opções
        self.button_opcao = pygame.image.load('funcao/Backgrounds/botao.png').convert_alpha()
        self.button_opcao = pygame.transform.rotozoom(self.button_opcao, 0, 0.6)
        self.button_opcao_rect = self.button_opcao.get_rect(center=(500, 400))

        #Exit
        self.button_exit = pygame.image.load('funcao/Backgrounds/botao.png').convert_alpha()
        self.button_exit = pygame.transform.rotozoom(self.button_exit, 0, 0.6)
        self.button_exit_rect = self.button_exit.get_rect(center=(500, 500))
        
        #Verificar se o Menu foi selecionado
        self.menu_ativo = True

        #Background de fundo
        self.fundo_menu = pygame.image.load("funcao/Backgrounds/menu.png").convert_alpha()
        
    #Pegar eventos
    def eventos(self):
        cursor = pygame.mouse.get_pos()
        mouse_press = pygame.mouse.get_pressed()

        if mouse_press[0]:
            #Jogar
            if self.button_start_rect.collidepoint(cursor):
                pass

            #Configurações
            if self.button_opcao_rect.collidepoint(cursor):
                self.menu_ativo = False
                
            #Sair do Game
            if self.button_exit_rect.collidepoint(cursor):
                pygame.quit()
                sys.exit()

    def desenhar_janela(self):
        #Desenhar o fundo
        self.screen.blit(self.fundo_menu,(0, 0))

        #Desenhar botão
        self.screen.blit(self.button_start, self.button_start_rect)
        self.screen.blit(self.button_opcao, self.button_opcao_rect)
        self.screen.blit(self.button_exit, self.button_exit_rect)
    
    def update(self):
        self.eventos()
        self.desenhar_janela()