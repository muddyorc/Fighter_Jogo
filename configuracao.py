import pygame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

class Config():
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Config")


        #Botões

        #Botão para Voltar
        self.button_voltar = pygame.image.load('funcao/Backgrounds/botao.png').convert_alpha()
        self.button_voltar = pygame.transform.rotozoom(self.button_voltar, 0, 0.6)
        self.button_voltar_rect = self.button_voltar.get_rect(topleft=(500, 100))
    
        #menu de configuração
        self.config_menu = pygame.Surface((1000*(80/100), 600*(85/100))) # the size of your rect
        self.config_menu.set_alpha(200)                # alpha level
        self.config_menu.fill((36,36,36))
        self.config_menu_rect = self.config_menu.get_rect(topleft=(1000*(10/100),600*(10/100)))

        #barra de Botões
        self.button_bar = pygame.Surface((1000*(80/100), 600*(15/100)))
        self.button_bar.set_alpha(200)
        self.button_bar.fill((40,40,40))
        self.button_bar_rect = self.button_bar.get_rect(topleft=(1000*(10/100),600*(10/100)))
        
        self.config_ativo = True

        #Background de fundo
        self.fundo_menu = pygame.image.load("funcao/Backgrounds/menu.png").convert_alpha()

    def desenhar_janela(self):
        #Desenhar o fundo
        self.screen.blit(self.fundo_menu,(0, 0))
        
        #Fundo configuração
        self.screen.blit(self.config_menu,self.config_menu_rect)
        self.screen.blit(self.button_bar,self.button_bar_rect)

        #Desenhar botão

        #voltar
        self.screen.blit(self.button_voltar, self.button_voltar_rect)
