import pygame
from pygame.sprite import Sprite



class Bala(Sprite):
    """Uma classe que administra projeteis disparados pela espaçonave. """

    def __init__(self, config, screen, nave):
        # Cria um objeto para o projetil na posição atual da espaçonave
        
        super(Bala, self).__init__()
        self.screen =screen

        # Cria um retângulo para o projetil em (0, 0) e, em seguida, define a
        # posição correta
        self.rect = pygame.Rect(0, 0, config.bala_width,
                                config.bala_height)
        self.rect.centerx = nave.rect.centerx
        self.rect.top = nave.rect.top



        #Armazena a posicao do projetil como um valor decimal
        self.y = float(self.rect.y)


        self.color = config.bala_color
        self.speed_factor = config.bala_speed_factor


    def update(self):
        """Move o projetil para cima na tela."""
        # Atualiza a posição decimal do projetil
        self.y -= self.speed_factor

        #Atualiza a posição de rect
        self.rect.y = self.y

    def draw_bala(self):
        """Desenha o projetil na tela."""
        pygame.draw.rect(self.screen, self.color, self.rect)
        
