import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """ Uma classe que representa um unico alienigena da frota. """


    def __init__(self, config, screen):
        """ Inicializa o alienigena e define sua posição inicial. """

        super(Alien,self).__init__()
        self.screen = screen
        self.config = config


        # Carrega a imagem do alienigena e define seu atributo rect
        self.image = pygame.image.load('images/alienigena.png')
        self.rect = self.image.get_rect()


        # Inicia cada novo alienigena proximo a parte superior esquerda da tela.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height


        # Armazena a posiçãoexta doalienigena.
        self.x = float(self.rect.x)

    def blitme(self):
        """ Desenha o alienigena em sua posição atual. """
        self.screen.blit(self.image,self.rect)


    def check_edges(self):
        """ Devolve True se o alieniginas estiver na borda da tela. """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """ Move o alienigina para a direita ou para esquerda. """
        self.x += (self.config.alien_speed_factor * self.config.fleet_direction)
        self.rect.x = self.x
        
