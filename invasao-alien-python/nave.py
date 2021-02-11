import pygame
from pygame.sprite import Sprite

class Nave(Sprite):

    def __init__(self, config, screen):
        """ Inicializa a espaçonave e define sua posição inicial. """
        super(Nave, self).__init__()
        self.screen = screen
        self.config = config

        # Carrega a imagem da espaçonave e obtem seu rect

        self.image = pygame.image.load("images/nave-4.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()


        # Inicializa cada nova espaçonave naparte inferior central da tela

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

        # Armazenar um valor decimal parao centro da espaçonave
        self.center = float(self.rect.centerx)


        # Flag de movimento
        self.mover_direita = False
        self.mover_esquerda = False


    def update(self):
        """Atualiza a posição da espaçonave de acordo com a flag de movimento."""
        # Atualiza o valor do centro da espaçonave, e não o retângulo
        if self.mover_direita and self.rect.right < self.screen_rect.right:
            self.center += self.config.nave_speed_factor           
        if self.mover_esquerda and self.rect.left > 0:
            self.center -= self.config.nave_speed_factor

        #Atualizaro objeto rect de acordo com self.center
        self.rect.centerx = self.center
            
    def blitme(self):
        """ Desenha a espaçonave em sua posição atual. """

        self.screen.blit(self.image,self.rect)


    def center_nave(self):
        # Centraliza a espaçonave na tela.
        self.center = self.screen_rect.centerx
        
